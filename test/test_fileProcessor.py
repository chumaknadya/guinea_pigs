import unittest

from src import fileProcessor


class TestFileProcessorMethods(unittest.TestCase):

    def test_readXMLFile_fileExists(self):
        self.assertTrue(fileProcessor.read_xml_file('test.xml'))

    def test_readChannelsFromFile_fileDoesNotExist(self):
        self.assertRaises(FileNotFoundError, fileProcessor.read_channels_from_file, 'file.xml')
        self.assertRaises(FileNotFoundError, fileProcessor.read_channels_from_file, '')

    def test_readChannelsFromFile(self):
        correct_title = 'Liga.net'
        correct_url = 'http://news.liga.net/all/rss.xml'

        self.assertTrue(fileProcessor.read_channels_from_file('test.xml'))
        self.assertEqual(fileProcessor.read_channels_from_file('test.xml')[0].title, correct_title)
        self.assertEqual(fileProcessor.read_channels_from_file('test.xml')[0].url, correct_url)


if __name__ == '__main__':
    unittest.main()
