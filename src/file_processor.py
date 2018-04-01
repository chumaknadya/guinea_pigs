from lxml import etree
from .RSSChannel import RSSChannel
import xml.etree.ElementTree as ET
from xml.dom import minidom



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


def get_xml_form_duplicates_list(duplicates_list):
    data = ET.Element('results')
    duplicates = ET.SubElement(data, 'duplicates')
    for d in duplicates_list:
        duplicate = ET.SubElement(duplicates, 'duplicate')
        link = ET.SubElement(duplicate, 'url')
        link.text = d.original.url
        percent = ET.SubElement(duplicate, 'duplication_percentage')
        percent.text = str(d.duplication_percentage)
    result = ET.tostring(data)
    return result


def write_results_to_file(duplicates_list):
    result = get_xml_form_duplicates_list(duplicates_list)
    #result = minidom.parseString(result).toprettyxml(indent="   ")
    file = open("results.xml", "w")
    file.write(str(result))
