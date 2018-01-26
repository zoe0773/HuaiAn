# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

def browser(brow='chrome'):
    '''获取浏览器驱动：Chrome\Firefox\IE\phantomjs,默认打开Chrome浏览器'''

    try:
        if brow == 'chrome':
            driver = webdriver.Chrome()
            return driver
        elif brow == 'firefox':
            driver = webdriver.Firefox()
            return driver
        elif brow == 'ie':
            driver = webdriver.Ie()
            return driver
        elif brow == 'phantomjs':
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found this browser,You can enter 'Firefox','Chrome','IE'...")
    except Exception as msg:
        print("%s" % msg)

class Base(object):
    '''基于原生框架的二次封装'''

    def __init__(self, driver):
        '''默认启动Chrome浏览器'''
        self.driver = driver

    def open(self, url, t='', timeout=10):

        # 使用get打开URL后，最大化窗口，判断title符合预期正确的title
        self.driver.get(url)
        #self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(t))
        except TimeoutException:
            print("open %s title error" % url)
        except Exception as msg:
            print("Error:%s" % msg)

    def find_element(self, locator, timeout=20):

        # 定位元素，参数locator是一组参数（"id","username"）
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):

        # 定位一组元素
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
        return elements

    def send_keys(self, locator, text):

        # 清空后再输入文本
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):

        # 点击操作
        element = self.find_element(locator)
        element.click()

    def is_title(self, title, timeout=10):

        # 判断title完全等于
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):

        # 判断title包含
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_located(self, locator, timout=10):

        # 判断元素是否被定位到（并不代表元素一定可见），定位到则返回element，没定位到返回False
        result = WebDriverWait(self.driver, timout, 1).until(EC.presence_of_element_located(locator))
        return result

    def is_text_in_element(self, locator, text, timeout=10):

        # 判断文本在元素里，没定位到返回False,定位到返回判断结果布尔值
        try:
            result =WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))

        except TimeoutException:

            print("元素没定位到：")
            return False
        else:
            return result


    def move_to_element(self, locator):

        # 鼠标悬停操作
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_by_text(self, locator, text):

        # 通过文本定位元素
        element = self.find_element(locator)
        Select(element).select_by_value(text)  #此处使用select模块的Select的根据value值定位元素

    def quit(self):

        # 退出浏览器
        self.driver.quit()