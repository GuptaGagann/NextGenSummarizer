from CleanCorpus import getSentences
from ProcessStopwords import processStopwords
from RankBasedSort import getDictionary, rankBasedSort
from WordCountBasedSort import wordCountSort
from WordListGeneration import generateWordList
from SentimentProcessing import generateSentiments


def func(document):
    # document_name=input("Select document to summarize:")
    # document_name='data.txt'
    # document=getData(document_name)
    paras_list, tncs_dt, tncs_list = getSentences(document)
    """for t in tncs_list:
        print(t)"""
    # document_type=input("Select summary type\n1. legal 2.\ntechnical:")
    document_type = 'legal'
    legalDictionary = getDictionary(document_type)
    docWordList = processStopwords(document)
    foundWordsList, newWordsList = generateWordList(docWordList, legalDictionary)

    rankedDictionary = getDictionary('ranked_legal')
    rankSet, rankToSentences_dict = rankBasedSort(foundWordsList, tncs_list, rankedDictionary)

    sortedSentenceList = wordCountSort(rankSet, rankToSentences_dict, foundWordsList)
    sortedSentimentList = generateSentiments(sortedSentenceList)

    # test code
    # for sentence in sortedSentenceList:
    #     print(sentence)

    return sortedSentenceList, sortedSentimentList, tncs_dt, paras_list, rankedDictionary