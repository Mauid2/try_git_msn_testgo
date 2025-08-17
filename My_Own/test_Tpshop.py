from time import sleep

import pandas
import pytest
import os
import allure

from My_Own.Find_Element import VerifyElement
from My_Own.Go_to_Login import IndexTask
from My_Own.utils import GetDriver, get_alert_msg

@allure.epic("TPshop")
@allure.feature("登录模块")

class TestShop(object):

    def setup_class(self):
        self.driver=GetDriver.set_driver()
        self.IndexPage=IndexTask()
        self.login_task=VerifyElement()

    def setup_method(self):
        self.driver.get('http://127.0.0.1/')
        self.IndexPage.go_to_login()
        sleep(2)

    @allure.title("测试账号不存在")
    def test_accout_not_exist(self):
        # # 2.输入一个不存在的用户名
        self.login_task.test_element("13800000001", "123456", "8888")

    @allure.title("测试成功")
    def test_accout(self):
        # # 2.输入一个不存在的用户名
        self.login_task.test_element("13800000002", "123456", "8888")

    def teardown_method(self):
        # 6.获取错误提示信息
        msg = get_alert_msg(self)
        print(msg)

    def teardown_class(self):
        sleep(2)
        GetDriver.quit_driver()

# if __name__ == '__main__':
#     pytest.main(['-s', 'test_Tpshop.py'])
#     os.system("allure generate ./temps -o ./report --clean")
