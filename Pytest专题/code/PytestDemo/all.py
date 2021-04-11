import pytest

if __name__ == '__main__':
    # 开两个线程去执行用户操作目录下所有的用例
    pytest.main(["-vs", "./user_cases", "-k=Test"])
