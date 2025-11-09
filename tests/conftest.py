import pytest


@pytest.fixture(scope="session")
def sample_order_data():
    """
    这是一个在 conftest.py 中定义的共享 Fixture，作用域为整个测试会话 (session)。
    它只会在整个测试运行开始时执行一次。
    """
    print("\n(SETUP - session scope from conftest.py) 正在准备订单数据...")
    order = {
        "order_id": "ORD-12345",
        "customer_id": "CUST-007",
        "items": [
            {"product_id": "PROD-A", "quantity": 2, "price": 10.0},
            {"product_id": "PROD-B", "quantity": 1, "price": 25.5},
        ],
        "is_paid": False,
    }
    yield order
    # 'yield' 之后的所有代码都是清理部分
    print("\n(TEARDOWN - session scope from conftest.py) 正在清理订单数据...")
