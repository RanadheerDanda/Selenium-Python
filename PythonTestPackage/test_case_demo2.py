import pytest

class TestCaseDemo2():

    @pytest.yield_fixture()
    def setUp(self):
        print("Running demo2 setUp")
        yield
        print("Running demo2 tearDown")

    def test_demo2_methodA(self,setUp):
        print("Running demo2 method A")

    def test_demo2_methodB(self,setUp):
        print("Running demo2 method B")
