from lxml import etree
from .RSSChannel import RSSChannel


def read_xml_file(filename):
    file = open(filename)
    soup = etree.parse(file)
    file.close()
    return soup


def read_channels_from_file(filename):
    try:
        xml = read_xml_file(filename)
        channels = xml.xpath('//channel')
    except FileNotFoundError:
        print("No such file: {0}".format(filename))
        raise
    except IOError as e:
        print(e)
        raise
    return [RSSChannel(channel) for channel in channels]
