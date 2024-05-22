import json
import os
print(os.getcwd())
# Open the text file for reading
with open('12.txt', 'r') as f:
    data = f.readlines()

# Parse the data
parsed_data = []
for line in data:
    elements = line.strip().split('.@')
    Data = elements[0]
    sentiment = int(elements[1])
    parsed_data.append({'Data': Data, 'sentiment': sentiment})

# Write the parsed data to a JSON file
with open('NewDataSet.json', 'w') as f:
    json.dump(parsed_data, f)