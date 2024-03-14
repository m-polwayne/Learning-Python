
from datetime import datetime


def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")

class Messenger:
    def __init__(self,listeners=[]):
        self.listeners=listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.recieve(message)
           
    
    def recieve(self, message):
        pass

class SaveMessages(Messenger):
    def __init__(self,listeners=[]) -> None:
        super().__init__(listeners)
        self.messages=[]