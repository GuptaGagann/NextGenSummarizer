def getDictionary(type):
    dictionary = []
    if type == 'legal':
        file = open("/home/GuptaGagann/mysite/final_legal_words.txt", "r+")
        data = file.read()
        dictionary = data.split("\n")
        file.close()
    elif type == 'ranked_legal':
        file = open("/home/GuptaGagann/mysite/final_legal_ranks.txt", "r+")
        data = file.read()
        dictionary = data.split("\n")
        file.close()
    elif type == 'stopwords':
        file = open("/home/GuptaGagann/mysite/stopwords.txt", "r+")
        words = file.read()
        dictionary = words.split("\n")
        file.close()

    return dictionary[:-1]