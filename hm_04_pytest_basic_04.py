# 测试类形式
import pytest


class TestDemo:
    def test_methode1(self): # 正常定义类，但是测试类名必须以 Test 开头
        """测试方法1"""
        print("测试方法1")
    def test_methode2(self): #正常定义方法，但是测试方法名必须以 test开头
        """测试方法2"""
        print("测试方法2")
if __name__ == '__main__':
    pytest.main(['-s','hm_04_pytest_basic_04.py'])