import unittest

APP_VERSION = "1.0.0"
FLAG = False

class MyTest_1(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    @unittest.skip('The test is not ready yet')
    def test_case_2(self):
        self.assertEqual(2 * 5, 3)

    def test_case_3(self):
        self.assertEqual(2 * 10, 20)

    def test_case_4(self):
        self.skipTest('Not ready')

    def test_case_5(self):
        raise unittest.SkipTest('Not ready too')


@unittest.skip('Skip all')
class MyTest_2(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        self.assertEqual(2 * 5, 10)

    def test_case_3(self):
        self.assertEqual(2 * 10, 20)



class MyTest_3(unittest.TestCase):
    @unittest.skipIf(APP_VERSION == "1.0.0",'Test is missed: wrong condition')
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    @unittest.skipUnless(FLAG, "Тест пропущен: external_flag")
    def test_case_2(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
