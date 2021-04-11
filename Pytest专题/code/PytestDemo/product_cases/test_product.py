import pytest

num = 20


@pytest.mark.skip(reason="无意义的测试方法")
def test_product_case():
    print("模拟测试产品相关的操作")


@pytest.mark.skipif(num > 18, reason="超过限定条件")
def test_case_001():
    print("测试方法_001")


def test_case_002():
    print("测试方法_002")


def test_case_003():
    print("测试方法_003")


def test_case_004():
    print("测试方法_004")


def test_case_005():
    print("测试方法_005")
