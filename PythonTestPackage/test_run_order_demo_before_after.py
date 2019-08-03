"""
http://pytest-ordering.readthedocs.io/en/develop/
"""

import pytest

@pytest.mark.run(after='test_second')
def test_third():
    assert True
    print("third")

def test_second():
    assert True
    print("second")

@pytest.mark.run(before='test_second')
def test_first():
    assert True
    print("First")