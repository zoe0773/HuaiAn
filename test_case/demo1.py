# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from test_case.po.base import Base
from selenium.webdriver.common.by import By

dri = webdriver.Chrome()
base_ = Base(dri)
# 启动浏览器后获取cookies
#print(dri.get_cookies()
zbname = (By.CSS_SELECTOR, "span.radio-box.clearfix.fl.ml90 > span[name='node-type'] > i")

dri.get("http://157.0.0.59:50131/login")
dri.maximize_window()
time.sleep(3)
dri.find_element_by_id("username").send_keys("szss")
dri.find_element_by_id("password").send_keys("111111")
dri.find_element_by_id("captcha").send_keys("3597")
time.sleep(2)
dri.find_element_by_xpath("//div[@class='zjg-login-btn']/input").click()
# print(dri.get_cookies())
time.sleep(5)
dri.get("http://157.0.0.59:50251/reps-moral-http/html/standard-base/standard-setting.html")
time.sleep(20)


def xsdy(name):
    dri.find_element_by_xpath("//div[@class='moral-tree-list']/ul/li/ul/li[@class='active']/following-sibling::li/div[2]/span/label[text()='%s']"%name).click()
    #//div[@class='moral-tree-list']/ul/li/ul/li[@class='active']/following-sibling::li/div[@class='tree-node selected-style']/span/label[text()='%s'
xsdy("学生德育")
time.sleep(5)
dri.find_element_by_css_selector("div.tree-node.selected-style>div.node-ctl>span").click()
time.sleep(10)
#定位指标单选按钮
base_.click(zbname)

time.sleep(20)
dri.quit()

# jskp = (By.CSS_SELECTOR, "div.add-item checkType>div.input clearfix:nth-child(1)>span>i")  # 教师考评checkBox
# stuzp = (By.CSS_SELECTOR, "div.add-item checkType>div.input clearfix:nth-child(2)>span>i")  # 学生自评checkBox
# stuhp = (By.CSS_SELECTOR, "div.add-item checkType>div.input clearfix:nth-child(3)>span>i")  # 学生互评checkBox
# parentkp = (By.CSS_SELECTOR, "div.add-item checkType>div.input clearfix:nth-child(4)>span>i")  # 家长考评checkBox
# label_ded = (By.CSS_SELECTOR, "div.add-item scoreStrategy>div>span(2)>label")  # <label>减分</label>
# bjdy = (By.CSS_SELECTOR, "li.active:nth-child(1)>div.tree-node selected-style>span>label.node-name")  # 班级德育分类
# bjdy_ad = (By.CSS_SELECTOR, "li.active:nth-child(1)>div.tree-node selected-style hoverStyle>div.node-ctl>span[1]")  # 指标添加按钮
# xsdy = (By.CSS_SELECTOR, "li.active:nth-child(2)>div.tree-node selected-style>span>label.node-name")  # 学生德育分类
# xsdy_ad = (By.CSS_SELECTOR, "li.active:nth-child(2)>div.tree-node selected-style hoverStyle>div.node-ctl>span[1]")  # 指标添加按钮
# jsdy = (By.CSS_SELECTOR, "li.active:nth-child(3)>div.tree-node selected-style>span>label.node-name")  # 教师德育分类
# jsdy_ad = (By.CSS_SELECTOR, "li.active:nth-child(3)>div.tree-node selected-style hoverStyle>div.node-ctl>span[1]")  # 指标添加按钮
