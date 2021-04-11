import pytest


@pytest.fixture(name="init_product")
def product_init():
    print("\n产品测试前置操作....")
    yield
    print("\n产品测试后置操作....")


@pytest.fixture(name="init_user")
def user_init():
    print("\n用户测试前置操作....")
    yield
    print("\n用户测试后置操作....")
