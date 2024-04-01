import ddContent
import datetime
import csv


class DailyDigestEmail:
    def __init__(self) -> None:
        self.content = {'quote': {'include': True, 'content': ddContent.getQuote},
                        'weather': {'include': True, 'content': ddContent.getWeather},
                        'twitter': {'include': True, 'content': ddContent.getTwitterTrend},
                        'wikipedia': {'include': True, 'content': ddContent.getWikepidiaArticle()}
                        }

    def send_email(self):
        k = self.content["quote"]["content"]

        print(k()['quote'])

    '''generate email body as plain text and html'''

    def format_message(self):

        text = f'*_*_*_`~*Daily Digest ~ {datetime.date.today().strftime("%d,%b,%Y")}*_*_*_*_-*\n\n'
        if self.content['quote']['include'] and self.content['quote']['content']:
            k = self.content["quote"]["content"]
            text = text + '********Quote of the day *********\n\n'
            text += f'"{k()["quote"]}" - {k()["author"] }\n\n'

        if self.content['wikipedia']['include'] and self.content['wikipedia']['content']:
            k = self.content["wikipedia"]["content"]
            text = text + '******** Daily Random learning *********\n\n'
            text += f'"{k["title"]}" - {k["extract"] }\n\n'

        if self.content['weather']['include'] and self.content['weather']['content']:
            k = self.content["weather"]["content"]
            text = text + '******** Daily weather and forecast *********\n\n'
            text += f'the current temperature is {k()["temp"]} degrees celcius\nfeels like {k()["feels"]} degrees celcius\n the minimum temperature will be {k()["min"] } degrees celcius\nthe maximum temperature will be {k()["max"] } degrees celcius\nthe weather conditions will be {k()["weather"] }\n\n'

        print(text)
        f = open('dd.txt', 'w')
        f.write(text)
        f.close()


daily = DailyDigestEmail()
daily.format_message()
