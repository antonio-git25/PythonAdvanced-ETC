import unittest


class MyTestCase1(unittest.TestCase):

    def test_c(self):
        print('test 3')

    def test_a(self):
        print('test 1')

    def test_b(self):
        print('test 2')


class MyTestCase2(unittest.TestCase):

    def test_c(self):
        print('test 6')

    def test_b(self):
        print('test 5')

    def non_test_a(self):
        print('test 4')


class MyTestCase3(unittest.TestCase):

    def test_a(self):
        print('test 1a')

    def test_a(self):
        print('test 2a')

    def test_a(self):
        print('test 3a')

if __name__ == '__main__':
    unittest.main()