import unittest
from alpharange import AlphabetRange

class TestAlphabetRange(unittest.TestCase):
    def test_one_argument_default_start(self):
        letters = AlphabetRange('D')
        first = None
        expected = 'A'
        for ch in letters:
            first = ch
            break
        self.assertEqual(first, expected)

    def test_one_argument_stop(self):
        letters = AlphabetRange('D')
        last = None
        expected = 'C'
        for ch in letters:
            last = ch
        self.assertEqual(last, expected)

    def test_one_argument_default_step(self):
        letters = AlphabetRange('D')
        expected = ['A', 'B', 'C', ]
        for i, ch in enumerate(letters):
            self.assertEqual(ch, expected[i])

    def test_two_argument_start(self):
        letters = AlphabetRange('C', 'G')
        first = None
        expected = 'C'
        for ch in letters:
            first = ch
            break
        self.assertEqual(first, expected)

    def test_two_argument_stop(self):
        letters = AlphabetRange('C', 'G')
        last = None
        expected = 'F'
        for ch in letters:
            last = ch
        self.assertEqual(last, expected)

    def test_two_argument_default_step(self):
        letters = AlphabetRange('C', 'G')
        expected = ['C', 'D', 'E', 'F']
        for i, ch in enumerate(letters):
            self.assertEqual(ch, expected[i])

    def test_three_argument_start(self):
        letters = AlphabetRange('C', 'G', 2)
        first = None
        expected = 'C'
        for ch in letters:
            first = ch
            break
        self.assertEqual(first, expected)

    def test_three_argument_stop(self):
        letters = AlphabetRange('C', 'G', 2)
        last = None
        expected = 'E'
        for ch in letters:
            last = ch
        self.assertEqual(last, expected)

    def test_three_argument_step(self):
        letters = AlphabetRange('C', 'H', 2)
        expected = ['C', 'E', 'G']
        for i, ch in enumerate(letters):
            self.assertEqual(ch, expected[i])

    def test_equals_true(self):
        letters1 = AlphabetRange('D')
        letters2 = AlphabetRange('A', 'D')
        self.assertTrue(letters1 == letters2)

        letters2 = AlphabetRange('A', 'D')
        letters3 = AlphabetRange('A', 'D', 1)
        self.assertTrue(letters2 == letters3)

        letters1 = AlphabetRange('D')
        letters3 = AlphabetRange('A', 'D', 1)
        self.assertTrue(letters3 == letters1)

    def test_equals_false_end(self):
        letters1 = AlphabetRange('E')
        letters2 = AlphabetRange('F')
        self.assertTrue(letters1 != letters2)

    def test_equals_false_start(self):
        letters1 = AlphabetRange('E')
        letters2 = AlphabetRange('B', 'E')
        self.assertTrue(letters1 != letters2)

    def test_equals_false_end(self):
        letters1 = AlphabetRange('B', 'H', 1)
        letters2 = AlphabetRange('B', 'H', 2)
        self.assertTrue(letters1 != letters2)
    """

    def test_one_argument_start(self):
    def test_one_argument_stop(self):
    def test_one_argument_step(self):
    def test_one_argument_start(self):
    def test_one_argument_stop(self):
    def test_one_argument_step(self):
    6,8,2,5
    """
if __name__ == '__main__':
    unittest.main()
