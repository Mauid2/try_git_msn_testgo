
from time import sleep
# 导包
import pytest
from selenium import webdriver
class webLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def web_login(self):
        if self.driver==None:
            self.driver.get("http://127.0.0.1/")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)  # 隐式等待
        return self.driver

    def web_quit(self):
        sleep(2)
        self.driver.quit()
        if self.driver:
            self.driver=None

