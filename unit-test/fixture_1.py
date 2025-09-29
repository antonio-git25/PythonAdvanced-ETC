import unittest


def setUpModule():
    print('Running setUpModule')


def tearDownModule():
    print('Running tearDownModule')


class TestMyModule1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Running setUpClass in first TestModule')

    @classmethod
    def tearDownClass(cls):
        print('Running first tearDownClass')

    def setUp(self):
        print('')
        print('Running setUp first module')

    def tearDown(self):
        print('Running tearDown first module')

    def test_case_1(self):
        self.assertEqual(5 + 5, 10)

    def test_case_2(self):
        self.assertEqual(1 + 1, 2)


class TestMyModule2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Running setUpClass in second TestModule')

    @classmethod
    def tearDownClass(cls):
        print('Running second tearDownClass')

    def setUp(self):
        print('')
        print('Running setUp second module')

    def tearDown(self):
        print('Running tearDown second module')

    def test_case_3(self):
        self.assertEqual(7 - 2, 5)

    def test_case_4(self):
        self.assertEqual(2 * 3, 6)


if __name__ == '__main__':
    unittest.main()
