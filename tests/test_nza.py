import pytest
import math
from nza import NZA

def test_init():
    n = NZA(5)
    assert n.local == 5.0
    assert math.isinf(n.universe)

def test_add():
    a = NZA(2)
    b = NZA(3)
    assert (a + b).local == 5.0

def test_sub():
    a = NZA(5)
    b = NZA(3)
    assert (a - b).local == 2.0
    assert (b - a).local == -1.0

def test_mul():
    a = NZA(2)
    b = NZA(3)
    assert (a * b).local == 6.0

def test_div():
    a = NZA(6)
    b = NZA(2)
    assert (a / b).local == 3.0

def test_div_zero():
    one = NZA(1)
    zero = NZA(0)
    result = one / zero
    assert math.isinf(result.local)

def test_repr():
    zero = NZA(0)
    assert \"0.0_local + ∞_universe\" in str(zero)
    inf_div = NZA(1) / NZA(0)
    assert \"∞_universe\" == str(inf_div)

def test_neg():
    pos = NZA(5)
    neg = -pos
    assert neg.local == -5.0

def test_comparisons():
    a = NZA(1)
    b = NZA(2)
    assert a < b
    assert a == NZA(1)
    assert a != 2

def test_radd_rsub_etc():
    assert NZA(1) + 2 == NZA(3)
    assert 5 - NZA(2) == NZA(3)
