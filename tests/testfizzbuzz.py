import unittest
from fizzbuzz.fizzbuzz import fizzbuzz


class FizzBuzzTester(unittest.TestCase):
    def setUp(self):
        self.generator = fizzbuzz(15)

    def test_fizzbuzz(self):
        for i in range(1, 16):
            val = next(self.generator)
            with self.subTest(i=i):
                if not i % 15:
                    self.assertEqual(val, 'FizzBuzz')
                elif not i % 3:
                    self.assertEqual(val, 'Fizz')
                elif not i % 5:
                    self.assertEqual(val, 'Buzz')
                else:
                    self.assertEqual(val, i)


if __name__ == '__main__':
    unittest.main()
