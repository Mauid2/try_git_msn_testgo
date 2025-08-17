from selenium.webdriver.common.by import By

from My_Own.utils import GetDriver


class FindElement(object):
    def __init__(self):
        self.driver=GetDriver.set_driver()
        self.name = (By.ID, "username")
        self.pwd = (By.ID, "password")
        self.verify_code = (By.ID, "verify_code")
        self.login_button = (By.NAME, "sbtbutton")

    def Find_Username(self):
        return self.driver.find_element(self.name[0], self.name[1])

    def Find_Password(self):
        return self.driver.find_element(self.pwd[0], self.pwd[1])

    def Find_verify_code(self):
        return self.driver.find_element(self.verify_code[0], self.verify_code[1])

    def Find_button(self):
        return self.driver.find_element(self.login_button[0], self.login_button[1])

class ActionElement(object):
    def __init__(self):
        self.action=FindElement()

    def Input_Username(self, username):
        self.action.Find_Username().send_keys(username)

    def Input_Password(self, password):
        self.action.Find_Password().send_keys(password)

    def Input_verify_code(self, verify_code):
        self.action.Find_verify_code().send_keys(verify_code)

    def Click_button(self):
        self.action.Find_button().click()


class VerifyElement(object):
    def __init__(self):
        self.verify=ActionElement()

    def test_element(self, username, password, verify_code):
        self.verify.Input_Username(username)
        self.verify.Input_Password(password)
        self.verify.Input_verify_code(verify_code)
        self.verify.Click_button()