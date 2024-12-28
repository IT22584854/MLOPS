import pytest
from main import add

def test_addition():  # In pytest, test functions are typically named with the prefix test_ 
    assert add(3,4) == 7  # test cases
    assert add(1,1) == 2
    assert add(-1,-2) == -4 