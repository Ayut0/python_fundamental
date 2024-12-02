from CS50.function.calculator import square

def test_positive():
    assert square(1) != 4
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    assert square(10) == 100

def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-10) == 100

def test_zero():
    assert square(0) == 0
    assert square(0) != 1
    assert square(0) != 4
    assert square(0) != 9
    assert square(0) != 100