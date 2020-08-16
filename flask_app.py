
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

from pilot_aldss import func

import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def legalTextSummariserMain():
    responseDict = dict()
    jsonResponse = request.data.decode(encoding="utf-8")
    parser = json.loads(jsonResponse)
    sourceFile = parser["sourceFile"]
    reviewCheck = sourceFile.split(" ")
    if reviewCheck[0]=="WewReview":
        review = sourceFile.replace("WewReview ","\n")
        reviewFp = open("/home/GuptaGagann/mysite/reviews.txt",'a')
        reviewFp.write(review)
        reviewFp.close()
        return responseDict

    else:
        sortedSentenceList, sortedSentimentList, tncs_dt, paras_list, rankedDictionary = func(sourceFile)

        rankedDictionaryJson = dict()

        for e in rankedDictionary:
            ls=e.split(" ")
            key=""
            for j in range(0,len(ls)-1):
                key = key + ls[j] + " "

            value=ls[-1]
            rankedDictionaryJson[key]=value

        responseDict['sortedSentenceList'] = sortedSentenceList
        responseDict['sortedSentimentList'] = sortedSentimentList
        responseDict['tncs_dt'] = tncs_dt
        responseDict['paras_list'] = paras_list
        responseDict['rankedDictionary'] = rankedDictionaryJson

        return responseDict


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=3000)

