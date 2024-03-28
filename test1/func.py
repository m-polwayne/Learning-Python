class wordset:
    puncs=['.',',','!','\'']
    def __init__(self) -> None:
        self.words=set()

    def addText(self,text):
        text=self.cleanText(text)
        for word in text.split():
            self.words.add(word)
    @staticmethod
    def cleanText(text):
        
        for punc in wordset.puncs:
            text.replace(punc,'')
        return text.lower()

d=wordset()
d.addText('that are we Doing, in his world! well what can we do but thank Him.')
print(d.words)

class word(wordset):
    def __init__(self) -> None:
        super().__init__()

g=word()
g.addText('that are we Doing, in his world! well what can we do but thank Him.')
print(wordset.puncs)