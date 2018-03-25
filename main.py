import os
import sys
import xml.etree.cElementTree as ET
from bs4 import BeautifulSoup
from lxml import etree
import requests

import src
#
# HEADERS = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
#     }
#
#
#
def readXMLFile(filename):
    with open(filename) as xml:
        soup = etree.parse(xml)
    return soup

def getChanelsFromFile(filename):
    channels = []
    xml = None
    try:
        xml = readXMLFile(filename)
    except IOError:
        print(e)
    finally:
        if not xml:
            channels = []
        else:
            channels = xml.xpath('//channel')

    return [src.RSSChannel(channel) for channel in channels]

channels = getChanelsFromFile(sys.argv[1])
print(channels)
for c in channels:
    c.loadNews()

#
# def getNews(url):
#     text = requests.get(url, headers=HEADERS)
#     root = ET.fromstring(text)
#     news = []
#     for item in root.findall('item'):
#         print('+++')
#         print(item)
#         news.append(item.get('title').text, item.get('description').text)
#
#     print(news)
#
#
#     # xml = ET.fromstring(text)
#     # tree = ET.parse(xml)
#     # # xml = BeautifulSoup(text, "lxml-xml")
#     # items = tree.findall("item")
#     # print(tree)
#     # news = []
#     # for item in items:
#     #     news.append(src.News(item))
#
#


