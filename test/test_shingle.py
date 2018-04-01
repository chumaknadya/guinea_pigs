import unittest
from unittest import TestCase
from shingle import canonize, genshingle, compaire


class Test_shingle(TestCase):
    def test_canonize(self):
        filename = '../resources/stopWords'
        self.assertEqual(['мной', 'беда'], canonize('со мной беда', filename))
        self.assertEqual([], canonize('', filename))
        self.assertEqual([], canonize('со', filename))
        self.assertEqual([], canonize('также там такой', filename))
        self.assertEqual(['знать', 'сидит', 'фазан'], canonize('знать, где сидит фазан', filename))
        self.assertEqual(['оля'], canonize('Оля, ты?', filename))
        self.assertEqual([], canonize('?,', filename))

    def test_compaire(self):
        filename = '../resources/stopWords'
        s = 'Жаль без тебя до небес бежать,Без тебя не могу дышать,Под ногами лишь небо вижу.' \
            'Стой, я тебя не коснусь рукой,Ты не слышишь, ты далеко,И наверно не будешь ближе.'
        cmp1 = genshingle(canonize(s, filename))
        cmp2 = genshingle(canonize(s, filename))
        self.assertEqual(compaire(cmp1, cmp2), 100);
        self.assertIsNone(compaire(genshingle(canonize(' ', filename)), genshingle(canonize(' ', filename))))


if __name__ == '__main__':
    unittest.main()

