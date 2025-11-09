import time

import pytest

# 解释一下 pytest 的 `autouse` Fixture 是什么以及如何使用。
# 如何使用 pytest-xdist 实现并行测试？
def test_fast_addition():
    """一个简单的、快速的测试，没有特定标记。"""
    assert 1 + 1 == 2


@pytest.mark.slow
def test_slow_database_query():
    print("slow-1")
    """模拟一个慢速测试，例如数据库查询。"""
    time.sleep(1)  # 模拟 1 秒的延迟
    assert True


@pytest.mark.api
def test_api_endpoint_user():
    """模拟一个需要调用 API 的测试。"""
    # 想象这里有调用 API 的代码
    assert True


@pytest.mark.slow
def test_another_slow_operation():
    print("slow-2")
    """另一个模拟的慢速测试。"""
    time.sleep(1.5)  # 模拟 1.5 秒的延迟
    assert True
