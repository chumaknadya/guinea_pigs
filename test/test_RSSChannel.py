import unittest

from src import RSSChannel
from src import news
from src import file_processor

class TestRSSChannelMethods(unittest.TestCase):

    def setUp(self):
        self.channels = file_processor.read_channels_from_file('resources/test.xml')

    def test_loadNews(self):
        self.channels[0].load_news()
        self.assertTrue(self.channels[0].news)

if __name__ == '__main__':
    unittest.main()
