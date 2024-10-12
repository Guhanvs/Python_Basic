import string


def word_frequency(sentence):
    normalized_sentence = sentence.lower().translate(str.maketrans('','',string.punctuation))
    words = normalized_sentence.split()
    frequency ={}
    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency
sentence = "hello world! hello all World"
print(word_frequency(sentence))