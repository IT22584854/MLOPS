import pytest
from calculator import add,substract

@pytest.fixture
def calculator_setup():
    print("setting up the environment for calculator")
    return {}

def test_add(calculator_setup):
    assert add(3,4) == 7

def test_substract(calculator_setup):
    assert substract(3,4) == -1