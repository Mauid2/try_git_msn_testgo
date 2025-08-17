from time import sleep

import pytest

from New_po.elementLogin import Test_Access
from New_po.indexLogin import IndexTask
from New_po.utils import GetDriver, get_windows


class TestLogin(object):
    def setup_class(self):
        self.driver=GetDriver.get_login()
        self.indexPlogin=IndexTask()
        self.login_task=Test_Access()

    def setup_method(self):  # 前置条件：打开网页，点击登录
        self.driver.get('http://127.0.0.1/')
        self.indexPlogin.go_to_login()
        sleep(2)

    def test_accout_not_exist(self):
        # # 2.输入一个不存在的用户名
        self.login_task.test_login("13800000001", "123456", "8888")

    def test_accout(self):
        # # 2.输入一个不存在的用户名
        self.login_task.test_login("13800000002", "123456", "8888")

    def teardown_method(self):
        msg=get_windows(self)
        print(msg)

    def teardown_class(self):
        GetDriver.quit_driver()


