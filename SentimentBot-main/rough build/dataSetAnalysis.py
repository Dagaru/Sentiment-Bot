import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.classify import NaiveBayesClassifier
import json
import pickle

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

total_pos_samples = 1921
total_neut_samples = 4237
total_neg_samples = 904

# Define the number of samples for the training and test sets
train_pos_samples = 1500
train_neut_samples = 3000
train_neg_samples = 600

test_pos_samples = 420
test_neut_samples = 1200
test_neg_samples = 300

def Preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [stemmer.stem(token) for token in tokens]
    return {token: True for token in tokens}

def LoadData(files):
    pos_data = []
    neg_data = []
    neut_data = []
    for file in files:
        with open(file, 'r',encoding='utf-8') as f:
            data = json.load(f)
            for d in data:
                if d['sentiment'] == 'positive':
                    pos_data.append((d['Data'], 'positive'))
                elif d['sentiment'] == 'neutral':
                    neut_data.append((d['Data'], 'neutral'))
                elif d['sentiment'] == 'negative':
                    neg_data.append((d['Data'], 'negative'))
    return pos_data, neg_data, neut_data

def ExtractFeatures(pos_data, neg_data, neut_data):
    pos_features = [(Preprocess(sentence), label) for (sentence, label) in pos_data]
    neg_features = [(Preprocess(sentence), label) for (sentence, label) in neg_data]
    neut_features = [(Preprocess(sentence), label) for (sentence, label) in neut_data]
        
    return pos_features, neg_features, neut_features

def BuildClassifier(pos_features, neg_features, neut_features):
    train_set = pos_features[:train_pos_samples] + neg_features[:train_neg_samples] + neut_features[:train_neut_samples]
    test_set = pos_features[total_pos_samples-test_pos_samples:] + neg_features[total_neg_samples-test_neg_samples:] + neut_features[total_neut_samples-test_neut_samples:]
    classifier = NaiveBayesClassifier.train(train_set)
    return classifier, train_set, test_set

def SaveClassifier(classifier):
    with open('classifier.pickle', 'wb') as f:
        pickle.dump(classifier, f)

def LoadClassifier():
    with open('classifier.pickle', 'rb') as f:
        classifier = pickle.load(f)
    return classifier

def Evaluate(classifier, train_set, test_set):
    print ('Training Accuracy is ' + str(nltk.classify.accuracy(classifier,train_set)))
    print ('Testing Accuracy is ' + str(nltk.classify.accuracy(classifier,test_set))) 

def PredictSentiment(text, classifier):
    prediction = classifier.classify(Preprocess(text))
    return prediction

# Load dataset
pos_data, neg_data, neut_data = LoadData(['DataSet.json'])

# Extract features
pos_features, neg_features, neut_features = ExtractFeatures(pos_data, neg_data, neut_data)

# Build classifier
classifier, train_set, test_set = BuildClassifier(pos_features, neg_features, neut_features)

# Evaluate classiffier
Evaluate(classifier, train_set, test_set)

# Save classifier
SaveClassifier(classifier)

#Load classifier
loaded_classifier = LoadClassifier()


#Use classifier to predict sentiment
prediction = PredictSentiment("bad day", loaded_classifier)
print(prediction)