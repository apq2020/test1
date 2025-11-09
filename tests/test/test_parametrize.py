import pytest


def add(a, b):
    """一个简单的加法函数，用于演示。"""
    return a + b


# 定义多组测试数据
# 每个元组的格式是 (输入a, 输入b, 期望的输出)
add_test_data = [
    # 使用 pytest.param 为每个测试用例设置一个可读的 ID
    pytest.param(1, 2, 3, id="positive-integers"),
    pytest.param(-1, 1, 0, id="positive-and-negative"),
    pytest.param(-5, -5, -10, id="negative-integers"),
    pytest.param(0, 0, 0, id="zeros"),
    pytest.param(2.5, 2.5, 5.0, id="floats"),
]


@pytest.mark.parametrize("a, b, expected", add_test_data)
def test_add_with_various_inputs(a, b, expected):
    """使用多组数据测试 add 函数。"""
    assert add(a, b) == expected
