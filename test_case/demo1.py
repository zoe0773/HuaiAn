# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from test_case.po.base import Base
from selenium.webdriver.common.by import By
from test_case.po.deyu_page import DeyuPage

dri = webdriver.Chrome()
base_ = Base(dri)
deyu = DeyuPage(dri)
# 启动浏览器后获取cookies
# print(dri.get_cookies()
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
time.sleep(10)


#def xsdy(name):
dri.find_element_by_xpath("//div/div[2]/div[1]/ul/li/ul/li[2]/div[2]/span/label").click()
    #dri.find_element_by_xpath("//div[@class='moral-tree-list']/ul/li/ul/li[@class='active']/following-sibling::li/div[2]/span/label[text()='%s']").click()

#xsdy("学生德育")
time.sleep(5)

# 点击学生德育后的新增按钮
dri.find_element_by_css_selector("div.tree-node.selected-style>div.node-ctl>span").click()
time.sleep(10)

# 定位指标单选按钮
base_.click(zbname)
time.sleep(10)

# 获取分类label标签文本
# ttt = base_.find_element(deyu.label_fl).text
# print(ttt)

# 选择加分label标签
t = base_.find_element(deyu.label_add).text
print(t)

# 点击加分按钮
base_.click(deyu.add__)
print("已定位加分按钮")


def kp(*kp_name):
    '''
    ele = dri.find_element_by_xpath("//div[2]/div/span/label[text()='%s']/following-sibling::span/i" % name)
    ele.click()
    '''
    deyu.check_box_byTuple(*kp_name)

kpfs = ('教师考评', '学生自评')

kp(*kpfs)




# 点击教师考评复选框
# dri.find_element_by_xpath("//div[2]/div/span[1]/label[text()='教师考评']/following-sibling::span/i").click()
#print("考评方式定位成功")

'''
#tuple 遍历
args = ("abc")
for i in range(len(args)):
    print(args[i])
输出结果：
a
b
c

args = ("abc" , )  #tuple类型
for i in range(len(args)):
    print(args[i])
输出结果：
abc   
'''

time.sleep(20)
dri.quit()
