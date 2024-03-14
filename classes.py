texts='Add text using the method add text, which first calls the method clean text to remove the punctuation and make everything lowercase. '



class wordSet:
    def __init__(self):
        self.words=set()

    def addText(self,text):
        text=wordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(text):
        text=text.replace('.','').lower().replace(',','')
        return text

WordSet=wordSet()
WordSet.addText(texts)
WordSet.addText('Him my name isMotshiudisi, I am a man. Screamm')
print(WordSet.words)

myList=list()
class UniqueList(list):
    def append(self,item):
        if item in self:
            return
        super().append(item)

uniqueList=UniqueList()
uniqueList.append('h')
uniqueList.append('h')
print(uniqueList)