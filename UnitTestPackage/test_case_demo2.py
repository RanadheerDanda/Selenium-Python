import unittest

class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('*#'*30)
        print('Class level setup method: execute one time before test')
        print('*#' * 30)

    def setUp(self):
        print('\nSetup Method: will execute every test')

    def test_methodA(self):
        print('Method A Test case')
    def test_methodB(self):
        print('Method B Test case')
    def tearDown(self):
        print('Tear down method')

    @classmethod
    def tearDownClass(cls):
        print('*#' * 30)
        print('Class level setup method: execute one time after test')
        print('*#' * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)