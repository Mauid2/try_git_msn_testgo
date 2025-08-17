from time import sleep
# 导包
import pytest
from selenium import webdriver

# 实例化浏览器
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class Test_TPShopLogin:

    def setup_method(self):
        driver.get("http://127.0.0.1/")
        driver.maximize_window()
        driver.implicitly_wait(10)  # 隐式等待
        driver.find_element(By.LINK_TEXT, "登录").click()


    def test_accout_not_exist(self):
        # 2.输入一个不存在的用户名
        driver.find_element(By.ID, "username").send_keys("13800000001")
        # 3.输入密码
        driver.find_element(By.ID, "password").send_keys("123456")
        # 4.输入验证码
        driver.find_element(By.NAME, "verify_code").send_keys("8888")
        # 5. 点击登录按钮
        driver.find_element(By.NAME, "sbtbutton").click()

    def test_password_error(self):   # 版本3.明天再看一遍！！！
        # 2.输入一个不存在的用户名
        driver.find_element(By.ID, "username").send_keys("13800000002")
        # 3.输入密码
        driver.find_element(By.ID, "password").send_keys("12345")
        # 4.输入验证码
        driver.find_element(By.NAME, "verify_code").send_keys("8888")
        # 5. 点击登录按钮
        driver.find_element(By.NAME, "sbtbutton").click()

    def teardown_method(self):
        # 6.获取错误提示信息
        msg = driver.find_element(By.CLASS_NAME, "layui-layer-content").text
        print("错误提示信息：", msg)

    def teardown_class(self):
        # 查看页面
        sleep(3)
        # 退出
        driver.quit()

if __name__ == '__main__':
    pytest.main(["-s", "tpshop_login_1.py"])