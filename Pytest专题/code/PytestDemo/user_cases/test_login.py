import pytest


def test_other_case():
    print("模拟测试其他情况")
    assert 1 == 2


class TestLogin:
    @pytest.mark.user_manage
    def test_case_001(self):
        print("模拟测试用户登录操作")
