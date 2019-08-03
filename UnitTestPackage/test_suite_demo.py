import unittest
from UnitTestPackage.test_class1 import TestClass1
from UnitTestPackage.test_class2 import TestClass2
from UnitTestPackage.test_case_demo import TestCaseDemo
from UnitTestPackage.test_case_demo2 import TestCaseDemo2


# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)
# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=2).run(smokeTest)