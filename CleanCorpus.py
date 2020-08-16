import re


def getSentences(document):
    # get all the sentences present in the file seperated by different punctuation marks

    # sentences
    paras_list = document.split("\n")
    paras_list = [para for para in paras_list if para!=""]
    paras_list = [para for para in paras_list if para.isspace()==False]
    temp_tncs_list = []
    tncs_list = []
    paras_dt = {}
    tncs_dt = {}
    for i in range(len(paras_list)):
        paras_dt[i] = paras_list[i]
        sentences = re.sub(r'^\d+[\.\d+]+', '\n', paras_list[i])
        sentences = re.sub('\?', '.\n', sentences)
        sentences = re.sub('\!', '.\n', sentences)
        sentences = re.sub('\.', '.\n', sentences)
        sentences = re.sub('\"|\”|\“', '"', sentences)
        temp_tncs_list = sentences.split("\n")
        tncs_list += temp_tncs_list
        for tnc in temp_tncs_list:
            tncs_dt[tnc] = i

    return paras_list, tncs_dt, tncs_list