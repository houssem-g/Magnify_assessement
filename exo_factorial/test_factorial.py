from factorial import ToyMath
import unittest


class TestFactorial(unittest.TestCase):

    def test_(self):
        self.assertEqual(ToyMath.factorial_at_Speed("hello"), 'please enter a number!')
        self.assertEqual(ToyMath.factorial_at_Speed(5), 120)
        self.assertEqual(ToyMath.factorial_at_Speed(-1), 'please use postive number')
        self.assertEqual(ToyMath.factorial_at_Speed(0), 1)



if __name__ == '__main__':
    unittest.main()