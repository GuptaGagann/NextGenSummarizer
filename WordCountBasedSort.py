import operator


def wordCountSort(rankSet, rankToSentences_dict, foundWordsList):
    # sorting same ranked sentences based on word count
    finalSortedSentences_dict = {}
    for rank in rankToSentences_dict.keys():

        termFrequency_dict = {}
        sentenceList = rankToSentences_dict[rank]

        for sentence in sentenceList:
            count = 0
            for word in foundWordsList:
                if word in sentence:
                    count += sentence.count(word)
                    pass
                pass
            termFrequency_dict[sentence] = count / len(sentence.split(' '))
            pass

        sortedSentences = sorted(termFrequency_dict.items(), key=operator.itemgetter(1), reverse=True)
        finalSortedSentences_dict[rank] = [s for s, r in sortedSentences]
        pass

    sortedSentenceList = []
    rankSet.remove(0)
    rankList = list(rankSet)
    rankList.sort(reverse=True)

    for rank in rankList:
        for sentence in finalSortedSentences_dict[rank]:
            sortedSentenceList.append(sentence)
            pass
        # testing
        pass

    # test code
    """for sentence in sortedSentenceList:
        print(sentence)"""

    return sortedSentenceList