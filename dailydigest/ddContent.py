from ast import main
import csv
import json
import random
from unicodedata import name
from urllib import request
import configparser
import tweepy
import wikipedia
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


def getWeather(lon=18.4231, lat=33.9221):

    api_key = '9286889f30eaefe86c4428f2cf4cb317'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    data = requests.get(url).json()

    dataDict = {
        # 'city': data['city']['name'],
        'temp': data['main']['temp'],
        'feels': data['main']['feels_like'],
        'min': data['main']['temp_min'],
        'max': data['main']['temp_max'],
        'weather': data['weather'][0]['description']
    }
    # location

    return dataDict


def getTwitterTrend():
    api_key = 'P4YLqpuWhZ3KuFcjBTBvoztNc'
    api_key_secret = '856HjSfHZlE0R5cZuzw2cDLlwBN9QBieW1fs8edRXi0yjQs1ni'
    access_token = '1761760210069184512-hXs8byCQm6XIr6RLcXnIhYMbYfQZti'
    access_token_secret = 'NoneAjRpztdHSwVXXRfDp7gc2JYNHMi19iVtBGO7K4VxRNZxn'
    # authenticate twitter

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    woeid = '55881535'

    trending = api.get_place_trends(woeid)
    print(trending.text())


def getWikepidiaArticle():
    j = wikipedia.random()
    data = {'title': j,
            'extract': wikipedia.summary(j)}
    return data


if __name__ == '__main__':

    getWeather()
    getWikepidiaArticle