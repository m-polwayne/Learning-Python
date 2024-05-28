import random


servicesAreUp = True
def getData50():
    if servicesAreUp and random.random()<0.5:
        return 'You get the data! that only happens 50%/ of the time'
def getData25():
    if servicesAreUp and random.random()<0.25:
        return 'You get the data! that only happens 25%/ of the time'
def getData10():
    if servicesAreUp and random.random()<0.1:
        return 'You get the data! that only happens 10%/ of the time'

def getDataRetry(dataFunc):
    for x in range(0,10):
        response=dataFunc()
        if response:
            print(response)

getDataRetry(getData10)