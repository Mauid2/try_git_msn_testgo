# 测试类形式
import pytest


class TestDemo:
    def setup_class(cls):
        """每个测试方法执行前调用"""
        print("开始咯")
    def teardown_class(cls):
        """每个测试方法执行后调用"""
        print("结束咯")
    def test_methode1(self): # 正常定义类，但是测试类名必须以 Test 开头
        """测试方法1"""
        print("测试方法1")
    def test_methode2(self): # 正常定义类，但是测试类名必须以 Test 开头
        """测试方法2"""
        print("测试方法2")
if __name__ == '__main__':
    pytest.main(['-s','hm_06_pytest_basic_06.py'])