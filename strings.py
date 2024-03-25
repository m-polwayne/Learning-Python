from string import punctuation


def lowerCase(text):
    return text.lower()


def removepunctuation(text):
    punct = ['.', ',', ';', '-']
    for j in punctuation:
        text = text.replace(j, '')
    return text


text = 'kjjnsjjnjnjjuwuhi iudjjuj jdj mkm k ijiwndin'
text = ' '.join([word for word in text.split() if len(word) <= 3])
print(text)
