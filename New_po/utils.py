from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_windows(self):
    sleep(5)
    msg = GetDriver.set_driver().find_element(By.CLASS_NAME, "layui-layer-content").text
    return msg

class GetDriver(object):
    __driver=None

    @classmethod
    def get_login(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.get('http://127.0.0.1/')
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver = None
