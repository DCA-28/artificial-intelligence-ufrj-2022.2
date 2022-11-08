import pytest
from queens_moves import *

def test_horizontal_attack():
    assert horizontal_attack([1, 2], [1, 3]) is True
    assert horizontal_attack([4, 2], [4, 3]) is True
    assert horizontal_attack([7, 2], [9, 3]) is False

def test_diagonal_attack():
    assert diagonal_attack([5, 0], [2, 3]) is True
    assert diagonal_attack([2, 6], [1, 7]) is True
    assert diagonal_attack([7, 0], [0, 7]) is True
    assert diagonal_attack([7, 0], [1, 7]) is False
    assert diagonal_attack([7, 2], [2, 3]) is False