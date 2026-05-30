
import csv
import json

import pytest

from utils.jsonhandling import jsonhandling


filePathJson = "testData/credentials.json"


def test_jsonhandling():
    with open(filePathJson) as data:
        creds = json.load(data)
        print(creds["email"])


def test_jsonFromUtils():
    creds = jsonhandling("testData/json2.json")
    print(creds[0]["email"])
    # print(creds["negitiveCreds"]["email"])


def test_jsonFromUtils2():
    print(jsonhandling("testData/credentials.json"))



# =========================================csv===================================
@pytest.mark.datahandling
def test_handlingCsv():
    finalData =[]
    with open("testData/credentails.csv") as data:
        formattedData = csv.DictReader(data)
        for i in formattedData:
            finalData.append(i)

    print(finalData)


    
