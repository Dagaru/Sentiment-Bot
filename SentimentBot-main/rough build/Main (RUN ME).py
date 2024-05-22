import json
import dataSetAnalysis
import RedditScraper
import UIMaker
import GetTicketyFinance


sentence = []
usefulSentence = []
tickers = []
companyName = []

results = []
finances = []
def createText(file):
    postList = []
    
    with open(file) as f:
        for jsonObj in f:
            postDict = json.loads(jsonObj)
            postList.append(postDict)

    for post in postList:
        string = post["title"]
        sentence.append(string)


def GetCompanyInfo(file):
    p = []

    with open(file) as f:
        for jsonObj in f:
            pDict = json.loads(jsonObj)
            p.append(pDict)

    with open('new.txt') as j:
        for jObj in j:
            jDict = json.loads(jObj)
            string = jDict["Name"]
            tickers.append(string)

    for post in p:
        s = post["Name"]
        companyName.append(s)

def get_symbol(name):
    with open('500.txt') as f:
        data = f.read().splitlines()
        for company in data:
            company_dict = json.loads(company)
            if company_dict['Name'] == name:
                return company_dict['Symbol']
    # If the given name is not found in the file
    return None


def checkForCompany(string):

    for t in tickers:
        if t in string:
            usefulSentence.append(string)
            selected = GetTicketyFinance.tickerPriceAndDividend(t)
            results.append((string, t, "", selected))



    for c in companyName:
        if string in usefulSentence:
            continue
        else:
            if c in string:
                usefulSentence.append(string)
                
                try:
                    selected = GetTicketyFinance.tickerPriceAndDividend(get_symbol(c))
                    results.append((string, c, "",selected))
                except:
                    print("no data")
                


def analyseText():

    for s in sentence:
        checkForCompany(s)


def testAnalysis():
    RedditScraper.Scrape()
    GetCompanyInfo('500.txt')
    createText('posts.txt')
    analyseText()

    loaded_classifier = dataSetAnalysis.LoadClassifier()

    for us in usefulSentence:
        results.append((us, "", "",""))

    for i, us in enumerate(usefulSentence):
        prediction = dataSetAnalysis.PredictSentiment(us, loaded_classifier)
        results[i] = (us, results[i][1], prediction,results[i][3])

    for r in results:
        if(r[1] == ""):
            results.remove(r)
        elif(r[2] == ""):
            results.remove(r)




if __name__ == "__main__":
    testAnalysis()

    UIMaker.CreateDisplay(results)

    
