import csv
import json
import random
from urllib import request

import requests
'''
Retrieve a random quote from a specified csv file
'''


def getQuote(quotes_file='quotes.csv'):
    try:
        with open(quotes_file, 'r') as csvfile:
            ccsvv = csv.reader(csvfile, delimiter='|')
            quotes = [{'author': line[0], 'quote': line[1]} for line in ccsvv]
    except Exception as e:
        quotes = [{'author': 'Eric Idle',
                   'quote': 'Always look on the bright side of life'}]
    return random.choice(quotes)


'''
quote=getQuote(quotes_file=None)
print(quote['quote']+' - '+quote['author'])'''

'''retrieve the current weather forecast from open weathermap'''


def getWeather(city):

    api_key = '9286889f30eaefe86c4428f2cf4cb317'
    url = f'https://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}&q={city}'
    data = requests.get(url).json()
    print(str(data))


def getTwitterTrend():
    pass


def getWikepidiaArticle():
    pass


if __name__ == '__main__':
    getWeather('Cape Town')
