import calk
import unittest

class CalkTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calk.add(100, 3), 103)

    def test_sub(self):
        self.assertEqual(calk.sub(100, 3), 97)

    def test_mul(self):
        self.assertEqual(calk.mul(100, 3), 300)

    def test_div(self):
        self.assertEqual(calk.div(90, 3), 30)

if __name__ == '__main__':
    unittest.main()
