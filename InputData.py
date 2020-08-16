def getData(document_name):
    # get the corpus from the file location specified

    # open
    file = open(document_name, "r+", encoding="utf8")
    document = file.read()
    file.close()

    return document
