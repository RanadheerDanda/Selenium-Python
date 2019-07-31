import pytest


class TestCaseDemo1():

    @pytest.fixture()
    def setUp(self):
        print("Running demo1 setUp")

    def test_demo1_methodA(self,setUp):
        print("Running demo1 method A")

    def test_demo1_methodB(self,setUp):
        print("Running demo1 method B")



