def generateWordList(docWordList, dictionary):
    # get words that are in our dictionary and the new words

    newWordsList = []
    foundWordsList = []
    for word in docWordList:
        if word not in dictionary:
            newWordsList.append(word)
        else:
            foundWordsList.append(word)
    return foundWordsList, newWordsList