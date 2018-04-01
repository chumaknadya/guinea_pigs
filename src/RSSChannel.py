import requests
from lxml import etree

from src import News

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }


class RSSChannel:

    def __init__(self, xml):
        self.title = xml.xpath('title')[0].text
        self.url = xml.xpath('url')[0].text
        self.item = xml.xpath('//items/path')[0].text
        self.item_title = xml.xpath('//items/pathToTitle')[0].text
        self.item_description = xml.xpath('//items/pathToDescription')[0].text
        self.item_url = xml.xpath('//items/pathToUrl')[0].text
        self.news = []

    def load_news(self):
            text = requests.get(self.url, headers=HEADERS)
            xml = etree.fromstring(text.text.encode('utf8'))
            items = xml.xpath(self.item)
            print(len(items))
            for item in items:
                self.news.append(News(item.xpath(self.item_title)[0],
                                      item.xpath(self.item_description)[0],
                                      item.xpath(self.item_url)[0]))
            print(self.news)


    def __str__(self):
        return "RSS {title} from url: {url}".format(title = self.title, url = self.url)

    __repr__ = __str__