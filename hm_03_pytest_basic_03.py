# 函数形式
import pytest


def test_func(): # 要求函数名以 test 开头
    """测试函数"""
    print('我是测试函数')
if __name__=='__main__':
    pytest.main(['-s','hm_03_pytest_basic_03.py'])