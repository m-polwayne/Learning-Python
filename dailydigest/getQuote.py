import csv
import random


'''def getQuote(quotes_file='quotes.csv'):
    try:
        with open(quotes_file,'r') as csvfile:
            ccsvv= csv.reader(csvfile, delimiter='|')
            quotes=[{'author':line[0],'quote':line[1] } for line in ccsvv]
    except Exception as e:
        quotes=[{'author':'Eric Idle',
                 'quote':'Always look on the bright side of life'}]
    print(random.choice((quotes))) 
getQuote()'''

with open('quotes.csv','r') as csvfile:
    ccsvv= csv.reader(csvfile, delimiter='|')
    quotes=[{'author':line[0],'quote':line[1] } for line in ccsvv]