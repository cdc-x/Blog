import pytest
import os

if __name__ == '__main__':
    pytest.main()  # 执行项目中所有用例
    os.system("allure generate ./tmp -o ./report --clean")  # 生成allure测试报告
