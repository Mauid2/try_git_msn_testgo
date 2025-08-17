from selenium.webdriver.common.by import By

# 获取对象层
from My_Own.utils import GetDriver


class indexPage(object):

    def __init__(self):
        self.driver=GetDriver.set_driver()

    def loginPage(self):
        return self.driver.find_element(By.LINK_TEXT, "登录")
# 操作层：动作层，但没有具体的实现
class indexAction(object):
    def __init__(self):
        self.action=indexPage()

    def loginAction(self):
        self.action.loginPage().click()

# 业务层
class IndexTask(object):
    def __init__(self):
        self.access=indexAction()

    def go_to_login(self):
        self.access.loginAction()

