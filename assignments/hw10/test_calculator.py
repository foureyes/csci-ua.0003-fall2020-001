import unittest
from calculator import RPNCalculator


class TestRPNCalculator(unittest.TestCase):
    def test_evaluate(self):
        c = RPNCalculator('2 3 +')
        self.assertEqual(c.evaluate(), 5)
        c = RPNCalculator('2 3 3 +')
        self.assertEqual(c.evaluate(), None)
        c = RPNCalculator('2 3 * 4 +')
        self.assertEqual(c.evaluate(), 10)

    def test_expression_saved(self):
        c = RPNCalculator('2 3 * 4 +')
        self.assertEqual(c.expression, '2 3 * 4 +')

    def test_skip_unsupported_operator(self):
        c = RPNCalculator('2 3 ? +')
        self.assertEqual(c.evaluate(), 5)

    def test_return_none(self):
        c = RPNCalculator('2 3 * 4 ')
        self.assertEqual(c.evaluate(), None)

if __name__ == '__main__':
    unittest.main()
