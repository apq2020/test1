import pytest


@pytest.fixture
def order_total(sample_order_data):
    """
    这是一个依赖于 sample_order_data 的 Fixture。
    它计算订单的总价。
    """
    print("\n(SETUP) 正在计算订单总价...")
    total = sum(item["quantity"] * item["price"] for item in sample_order_data["items"])
    return total


def test_order_has_items(sample_order_data):
    """测试订单中是否包含商品。它通过参数名 'sample_order_data' 来使用 Fixture。"""
    # 修正：测试应该验证项目数量大于0，而不是等于0
    assert len(sample_order_data["items"]) > 0


def test_order_is_not_paid(sample_order_data):
    """测试订单的初始状态是否为“未支付”。这个测试也重用了同一个 Fixture。"""
    assert sample_order_data["is_paid"] is False


def test_order_total_calculation(order_total):
    """测试订单总价是否计算正确。它使用了依赖其他 Fixture 的 Fixture。"""
    # 2 * 10.0 + 1 * 25.5 = 20.0 + 25.5 = 45.5
    assert order_total == 45.5
