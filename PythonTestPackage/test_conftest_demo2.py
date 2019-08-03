import pytest

def test_demo2_methodA(setUp,oneTimeSetUp):
    print("Running conftest demo2 method A")

def test_demo3_methodB(oneTimeSetUp,setUp,):
    print("Running conftest demo2 method B")