from selenium.webdriver.common.by import By

from New_po.utils import GetDriver


class elementPage(object):
    def __init__(self):
        self.driver = GetDriver.get_login()
        self.name = (By.ID, "username")
        self.pwd = (By.ID, "password")
        self.verify_code = (By.ID, "verify_code")
        self.login_button = (By.NAME, "sbtbutton")

    def find_username(self):
        return self.driver.find_element(self.name[0], self.name[1])

    def find_password(self):
        return self.driver.find_element(self.pwd[0], self.pwd[1])

    def find_verify_code(self):
        return self.driver.find_element(self.verify_code[0], self.verify_code[1])

    # 点击登录按钮
    def find_login_btn(self):
        return self.driver.find_element(self.login_button[0], self.login_button[1])


class elementAction(object):
    def __init__(self):
        self.action=elementPage()

    def input_username(self,username):
        self.action.find_username().clear()
        self.action.find_username().send_keys(username)

    def input_password(self,password):
        self.action.find_password().clear()
        self.action.find_password().send_keys(password)

    def input_verify_code(self,verify_code):
        self.action.find_verify_code().clear()
        self.action.find_verify_code().send_keys(verify_code)

    def click_login_btn(self):
        self.action.find_login_btn().click()

class Test_Access(object):
    def __init__(self):
        self.access=elementAction()

    def test_login(self,username,password,verify_code):
        self.access.input_username(username)
        self.access.input_password(password)
        self.access.input_verify_code(verify_code)
        self.access.click_login_btn()