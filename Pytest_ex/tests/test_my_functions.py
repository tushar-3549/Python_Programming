import pytest
from source import my_functions

def test_add():
    # pass
    res = my_functions.add(1, 2)
    assert res == 3
def test_string_add():
    res = my_functions.add("I love ","you")
    assert res == "I love you"
def test_devide():
    res = my_functions.devide(10, 5)
    assert res == 2
def test_devide_by_zero():
    with pytest.raises(ValueError):
        my_functions.devide(10, 0)

@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    res = my_functions.add(2, 3)
    assert res == 5

@pytest.mark.xfail(reason="We can't devide by zero")
def test_devide():
    my_functions.devide(5, 0)