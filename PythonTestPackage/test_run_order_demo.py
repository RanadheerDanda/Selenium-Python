"""
http://pytest-ordering.readthedocs.io/en/develop/
"""

import pytest

#B,C,D,E,F,A

def test_run_order_methodB(oneTimeSetUp, setUp):
    print("Running method B")


def test_run_order_methodC(oneTimeSetUp, setUp):
    print("Running method C")


def test_run_order_methodD(oneTimeSetUp, setUp):
    print("Running method D")


def test_run_order_methodE(oneTimeSetUp, setUp):
    print("Running method E")


def test_run_order_methodF(oneTimeSetUp, setUp):
    print("Running method F")

def test_run_order_methodA(oneTimeSetUp, setUp):
    print("Running method A")