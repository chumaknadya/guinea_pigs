import unittest

from src import file_processor
from src import Duplication
from src import News


class TestFileProcessorMethods(unittest.TestCase):

    def test_read_xml_ile_fileExists(self):
        self.assertTrue(file_processor.read_xml_file('resources/test.xml'))

    def test_read_channels_from_file_file_does_not_exist(self):
        self.assertRaises(FileNotFoundError, file_processor.read_channels_from_file, 'resources/teee.xml')
        self.assertRaises(FileNotFoundError, file_processor.read_channels_from_file, '')

    def test_read_channels_from_file(self):
        correct_title = 'Liga.net'
        correct_url = 'http://news.liga.net/all/rss.xml'

        self.assertTrue(file_processor.read_channels_from_file('resources/test.xml'))
        self.assertEqual(file_processor.read_channels_from_file('resources/test.xml')[0].title, correct_title)
        self.assertEqual(file_processor.read_channels_from_file('resources/test.xml')[0].url, correct_url)

    def test_get_xml_from_duplicates_list_empty_list(self):
        correct_string = "b'<results><duplicates /></results>'"
        duplications = []
        self.assertEqual(correct_string, str(file_processor.get_xml_form_duplicates_list(duplications)))

    def test_get_xml_from_duplicates_list(self):
        correct_string = "b'<results><duplicates><duplicate><url>url</url><duplication_percentage>15" + \
                         "</duplication_percentage></duplicate></duplicates></results>'"
        duplications = []
        duplications.append(Duplication(News("t", "d", "url"), 15))
        self.assertEqual(correct_string, str(file_processor.get_xml_form_duplicates_list(duplications)))


if __name__ == '__main__':
    unittest.main()
