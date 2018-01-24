#coding=utf-8

from selenium import webdriver
import time

dri = webdriver.Chrome()
#启动浏览器后获取cookies
print(dri.get_cookies())

dri.get("http://157.0.0.59:50131/login")
time.sleep(5)
dri.find_element_by_id("username").send_keys("szss")
dri.find_element_by_id("password").send_keys("111111")
dri.find_element_by_id("captcha").send_keys("3597")
time.sleep(2)
dri.find_element_by_xpath("//div[@class='zjg-login-btn']/input").click()
print(dri.get_cookies())
time.sleep(5)
dri.quit()

