from lxml import etree
from .RSSChannel import RSSChannel
import xml.etree.ElementTree as ET


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


def write_results_to_file(duplicates_list):
    # create the file structure
    data = ET.Element('results')
    duplicates = ET.SubElement(data, 'duplicates')
    for d in duplicates_list:
        duplicate = ET.SubElement(duplicates, 'duplicate')
        link = ET.SubElement(duplicate, 'url')
        link.text = d.original.url
        percent = ET.SubElement(duplicate, 'duplication_percentage')
        percent.text = str(d.duplication_percentage)

    # create a new XML file with the results

    tree = ET.ElementTree(data)
    tree.write("results.xml",
               xml_declaration=True,
               encoding='utf-8',
               method="xml")
