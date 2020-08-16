from textblob import TextBlob
def generateSentiments(corpus):
    sentiments = []

    for sentence in corpus:
        testimonial = TextBlob(sentence)
        sentiments.append(str(testimonial.sentiment.polarity)+" | "+str(testimonial.sentiment.subjectivity))

    return sentiments