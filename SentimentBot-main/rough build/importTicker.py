import re
import json

with open('new.txt') as file:
    text = file.read()

userInput = input("Enter ticker symbol you want to retrieve: ")
userInput = userInput.upper()

lines = [line.strip() for line in text.split('\n') if line.strip()]

data = {json.loads(line)["Name"]: json.loads(line) for line in lines}

if userInput in data:
    info = data[userInput]
    print(f"Information for {userInput}: ")
    for key, value in info.items():
        print(f"{key}: {value}")
else:
    print(f"{userInput} not found in file")

