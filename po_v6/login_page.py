from po_v6.utils import DriverUtil
# 实例化浏览器
from selenium.webdriver.common.by import By

'''对象层'''
class LoginPage(object):
    def __init__(self):
        self.driver=DriverUtil.get_driver()
        self.name=(By.ID, "username")
        self.pwd=(By.ID, "password")
        self.verify_code=(By.ID, "verify_code")
        self.login_button=(By.NAME, "sbtbutton")

    def find_username(self):
        return self.driver.find_element(self.name[0], self.name[1])

    def find_password(self):
        return self.driver.find_element(self.pwd[0], self.pwd[1])

    def find_verify_code(self):
        return self.driver.find_element(self.verify_code[0], self.verify_code[1])

    # 5. 点击登录按钮
    def click_login_button(self):
        return self.driver.find_element(self.login_button[0], self.login_button[1])

'''操作层'''
class LoginPageAction(object):
    def __init__(self):
        self.login_page=LoginPage()   # 获取对象层对象

    def input_username(self, username):
        # 说明:在执行输入操作前，应该先执行清空操作
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    def input_verify_code(self, verify_code):
        self.login_page.find_verify_code().clear()
        self.login_page.find_verify_code().send_keys(verify_code)

    def click_login_button(self):
        self.login_page.click_login_button().click()

class TestLoginPage(object):
    '''测试用例层'''
    def __init__(self):
        self.login_page_action=LoginPageAction()   # 获取操作层对象
        
    def test_login(self, username, pwd, code):
        self.login_page_action.input_username(username)
        self.login_page_action.input_password(pwd)
        self.login_page_action.input_verify_code(code)
        self.login_page_action.click_login_button()