from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def get_alert_msg(self):
    '''获取浏览器弹窗信息'''
    sleep(2)
    msg = DriverUtil.get_driver().find_element(By.CLASS_NAME, "layui-layer-content").text
    return msg


class DriverUtil(object):
    # 说明:对象变量只需要在类定义内部使用，因此定义为私有变量
    __driver=None

    @classmethod
    def get_driver(cls):
        '''获取浏览器对象'''
        if cls.__driver is None:
            cls.__driver=webdriver.Chrome()
            cls.__driver.get("http://127.0.0.1/")
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        '''关闭浏览器对象'''
        # 说明:必须保证浏览器对象存在，才能执行退出操作
        if cls.__driver:
            sleep(3)
            cls.__driver.quit()
            cls.__driver=None   ## 保险手段:移除对象后，保留对象变量，以备下一次使用

if __name__ == '__main__':
    DriverUtil().get_driver()
    sleep(2)
    DriverUtil().quit_driver()

