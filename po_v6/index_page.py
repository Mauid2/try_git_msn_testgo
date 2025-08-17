from po_v6.utils import DriverUtil
# 实例化浏览器
from selenium.webdriver.common.by import By


class IndexPage(object):
    '''首页对象层'''
    def __init__(self):
        self.driver=DriverUtil.get_driver()

    def find_login(self):
        return self.driver.find_element(By.LINK_TEXT,"登录")

class IndexHandle(object):
    '''首页操作层'''
    def __init__(self):
        self.index_page=IndexPage()  # 获取对象层对象

    def click_login(self):
        '''点击登录按钮'''
        self.index_page.find_login().click()

class IndexTask(object):
    '''首页任务层'''
    def __init__(self):
        self.index_handle=IndexHandle()  # 获取操作层对象

    def go_to_login(self):
        self.index_handle.click_login()  # 点击登录按钮