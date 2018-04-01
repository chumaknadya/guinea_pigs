import unittest

from src import file_processor


class TestFileProcessorMethods(unittest.TestCase):

    def test_readXMLFile_fileExists(self):
        self.assertTrue(file_processor.read_xml_file('resources/test.xml'))

    def test_readChannelsFromFile_fileDoesNotExist(self):
        self.assertRaises(FileNotFoundError, file_processor.read_channels_from_file, 'resources/file.xml')
        self.assertRaises(FileNotFoundError, file_processor.read_channels_from_file, '')

    def test_readChannelsFromFile(self):
        correct_title = 'Liga.net'
        correct_url = 'http://news.liga.net/all/rss.xml'

        self.assertTrue(file_processor.read_channels_from_file('resources/test.xml'))
        self.assertEqual(file_processor.read_channels_from_file('resources/test.xml')[0].title, correct_title)
        self.assertEqual(file_processor.read_channels_from_file('resources/test.xml')[0].url, correct_url)


if __name__ == '__main__':
    unittest.main()
