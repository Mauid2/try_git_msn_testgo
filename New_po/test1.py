from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('http://127.0.0.1/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"登录").click()
driver.find_element("id","username").send_keys("13800000001")
driver.find_element("id","password").send_keys("123456")
driver.find_element("id","verify_code").send_keys("8888")
driver.find_element("name","sbtbutton").click()

# 显示错误信息
msg=driver.find_element(By.CLASS_NAME,"layui-layer-content").text
print(msg)

sleep(5)
driver.quit()

