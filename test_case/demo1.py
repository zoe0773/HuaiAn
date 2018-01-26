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