from time import sleep
# 导包
import pytest

# 实例化浏览器
from po_v6.index_page import IndexTask
from po_v6.login_page import TestLoginPage
from po_v6.utils import DriverUtil


class Test_TPShopLogin(object):

    def setup_class(self):
        # 1.实例化浏览器
        self.driver=DriverUtil.get_driver()
        self.index_task=IndexTask()    # 实例化首页
        self.login_task=TestLoginPage()    # 实例化登录页面操作层对象

    def setup_method(self):
        # 打开首页
        self.driver.get("http://127.0.0.1/")
        # 点击登录
        self.index_task.go_to_login()
        # self.index_task.go_to_login()
        sleep(2)

    def test_accout_not_exist(self):
        # # 2.输入一个不存在的用户名
        self.login_task.test_login("13800000001", "123456", "8888")

    def test_password_error(self):   # 版本3.明天再看一遍！！！
        # 2.输入一个错误密码
        self.login_task.test_login("13800000002", "12345", "8888")



    def teardown_class(self):
        DriverUtil.quit_driver()




