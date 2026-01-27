import pytest

def test_add():
    assert add(2,3)==5

def test_sub():
    assert sub(5,3)==2

def test_mul():
    assert mul(4,3)==12

def test_div():
    assert div(10,2)==5

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(10,0) 


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b 

def div(a,b):
    if b==0:
        raise ValueError("Divison by zero is not allowed.")
    return a/b 