import unittest

class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print('Setup Method: will execute every test')

    def test_methodA(self):
        print('Method A Test case')
    def test_methodB(self):
        print('Method B Test case')
    def tearDown(self):
        print('Tear down method')

if __name__ == '__main__':
    unittest.main(verbosity=2)