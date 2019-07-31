import pytest

def test_demo1_methodA(oneTimeSetUp,setUp):
    print("Running conftest demo1 method A")

def test_demo1_methodB(setUp,oneTimeSetUp):
    print("Running conftest demo1 method B")