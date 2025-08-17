
from time import sleep
# 导包
import pytest
from selenium import webdriver

# 实例化浏览器
from selenium.webdriver.common.by import By
'''
输入：账号、密码、验证码，点击登录
'''

class Login_object(object):
    '''对象层'''
    def __init__(self):
       self.driver=webdriver.Chrome()
       self.driver.get("http://127.0.0.1/")
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)  # 隐式等待
       self.driver.find_element(By.LINK_TEXT, "登录").click()

    def find_username(self):
        return self.driver.find_element(By.ID, "username")

    def find_element_password(self):
        return self.driver.find_element(By.ID, "password")

    def find_element_code(self):
        return self.driver.find_element(By.NAME, "verify_code")

    def find_element_login_button(self):
        return self.driver.find_element(By.NAME, "sbtbutton")

class Login_operation(object):
    '''操作层'''
    def __init__(self):
        self.login_object=Login_object()

    def input_username(self,username):
        self.login_object.find_username().send_keys(username)

    def input_password(self,password):
        self.login_object.find_element_password().send_keys(password)

    def input_code(self,code):
        self.login_object.find_element_code().send_keys(code)

    def click_login_button(self):
        self.login_object.find_element_login_button().click()


class Login_test(object):
    '''业务层'''
    def __init__(self):
        self.login_test=Login_operation()

    def login(self,username,password,code):
        self.login_test.input_username(username)
        self.login_test.input_password(password)
        self.login_test.input_code(code)
        self.login_test.click_login_button()
        sleep(2)