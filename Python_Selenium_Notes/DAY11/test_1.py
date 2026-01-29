import pytest

#simple assert

def test_addition():
    print("addition done")
    assert 2+3==5
    assert 2+5==7

#assert with message

# def test_subtraction():
#     print("subtraction done")
#     assert 5-3==1,"subtraction result is incorrect"

#exception handling in pytest


def divide(a,b):
    print("\n division done")
    return a/b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)


#markers

#! smoke mark
@pytest.mark.smoke
def test_login():
    assert  True

#! skip mark


@pytest.mark.skip(reason="feature not implemented")
def test_payment():
    assert True

#! conditional skip

import sys

@pytest.mark.skipif(sys.platform=="win32",reason="not supported in windows")
def test_linux_only():
    assert True


#! expected failure


@pytest.mark.xfail(reason="known bug")
def test_know_issue():
    assert 4+4==10


#calculator.py

def multiply(a,b):
    return a*b

def test_multiply():
    assert multiply(3,4)==12

