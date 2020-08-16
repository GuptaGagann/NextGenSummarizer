import re

from GetDictionary import getDictionary


def processStopwords(document):
    # looking for all unique stopwords that are present in our corpus

    docWordList = re.split(" |\n", document)
    docWordList = [e.lower() for e in docWordList]
    docWordList = set(docWordList)  # get only unique words

    # Stopwords
    stopWordList = getDictionary('stopwords')

    if '' in docWordList:
        docWordList.remove('')
    if " " in docWordList:
        docWordList.remove(" ")

    # removing stopwords
    for word in stopWordList:
        if word in docWordList:
            docWordList.remove(word)
            pass
        pass
    return docWordList