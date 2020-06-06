import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def test_peek(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 2)

    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertFalse(s.empty())
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())

    def test_str(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(str(s), '|2|\n|1|\n ‾')

    def test_empty(self):
        s = Stack()
        self.assertTrue(s.empty())

    def test_all(self):
        s = Stack()
        s.push(1)
        self.assertEqual(str(s), '|1|\n ‾')
        s.push(2)
        self.assertEqual(str(s), '|2|\n|1|\n ‾')
        s.push(3)
        self.assertEqual(str(s), '|3|\n|2|\n|1|\n ‾')
        self.assertEqual(3, s.peek())
        s.pop()
        self.assertEqual(str(s), '|2|\n|1|\n ‾')
        s.pop()
        self.assertEqual(str(s), '|1|\n ‾')
        self.assertEqual(1, s.peek())

if __name__ == '__main__':
    unittest.main()
