from GetDictionary import getDictionary


def rankBasedSort(foundWordsList, tncs_list, dictionary):

    rank_dict = {}
    for data in dictionary:
        value = data.split(' ')
        key = value[0]
        for x in value[1:-1]:
            key = key + ' ' + x
        rank_dict[key] = int(value[-1]) - 1
    pass

    rankedSentences_dict = {}
    rankedSentences_data = {}
    rankSet = set()
    for sentence in tncs_list:
        rankList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        wordInSentenceList = sentence.split(' ')

        for word in wordInSentenceList:
            if word.lower() in foundWordsList:
                rankList[rank_dict[word.lower()]] += 1
            pass
        rankedSentences_data[sentence] = rankList
        # rank calculation
        rank = 0
        for i in range(15):
            rank += (rankList[i] * (1 + i))
            pass
        rank //= max(1, (sum(rankList)))
        if len(wordInSentenceList)<=6:
            rank//=4
        rankedSentences_dict[sentence] = rank
        rankSet.add(rank)
        pass

    # testing
    for x in rankedSentences_dict.keys():
        #    print(x[0:10],'  ',rankedSentences_data[x])
        pass

    # sort and return
    rankToSentences_dict = {}

    for rank in rankSet:
        if rank != 0:
            rankToSentences_dict[rank] = []
        pass

    for sentence in rankedSentences_dict.keys():
        if rankedSentences_dict[sentence] != 0:
            rankToSentences_dict[rankedSentences_dict[sentence]].append(sentence)
            pass
        pass

    return rankSet, rankToSentences_dict