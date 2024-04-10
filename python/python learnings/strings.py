from string import punctuation


def lowerCase(text):
    return text.lower()


def removepunctuation(text):
    punct = ['.', ',', ';', '-']
    for j in punctuation:
        text = text.replace(j, '\n')
    return text


text = ' The clean text method is a static method because it does not belong to any particular class instance, whereas add text is an instance method that belongs to a particular instance of the class. Static variables like replace puncs can also be added to control which punctuations get replaced. Use either the class name or the class instance to refer to static variables, but cannot be done with instance methods.'
# text = ' '.join([word for word in text.split() if len(word) <= 3])
print(removepunctuation(text))
print(lowerCase(text))
