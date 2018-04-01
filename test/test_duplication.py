import unittest
from unittest import TestCase
from src.duplication import Duplication
from src.news import News


class Test_duplication(TestCase):
    def test_str(self):
        expected = "duplicates title with 10 percentage"
        n = News("title", "desc", "url")
        d = Duplication(n, 10)
        self.assertEqual(str(d), expected)


if __name__ == '__main__':
    unittest.main()
