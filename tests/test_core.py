from mypackage.core import add,divide,compute
import pytest


def test_add():
    assert add(2, 3) == 5

def test_divide_success():
    assert divide(10, 2) == 5

# 测试除零错误
# 本函数旨在验证当除数为零时，是否能正确抛出ZeroDivisionError异常
def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

# 测试整数相加
def test_compute_integers():
    assert compute(2, 3) == 5
    assert compute(-1, 1) == 0


# 测试浮点数相加
def test_compute_floats():
    assert round(compute(2.5, 3.1), 1) == 5.6


# 测试字符串拼接
def test_compute_strings():
    assert compute("hello", " world") == "hello world"


# 测试列表拼接
def test_compute_lists():
    assert compute([1, 2], [3, 4]) == [1, 2, 3, 4]


# 测试元组拼接
def test_compute_tuples():
    assert compute((1, 2), (3, 4)) == (1, 2, 3, 4)


# 测试混合类型：整数 + 浮点数
def test_compute_mixed_types():
    assert compute(2, 3.5) == 5.5


# 测试非法类型组合，期望抛出 TypeError
def test_compute_invalid_types():
    with pytest.raises(TypeError):
        compute(5, None)
