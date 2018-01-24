#coding=utf-8

from test_case.po.base import Base
from selenium.webdriver.common.by import By

url = "http://157.0.0.59:50131/login"

class LoginPage(Base):

    # 定位器，定位页面元素
    uname = (By.ID, "username")
    psw = (By.ID, "password")
    seccode = (By.ID, "captcha")
    submit = (By.CLASS_NAME, "zjg-login-btn")

    def input_username(self, username):

        #输入用户名
        self.send_keys(self.uname, username)

    def input_psw(self, password):

        #输入密码
        self.send_keys(self.psw, password)

    def input_captcha(self, captcha):

        #输入验证码
        self.send_keys(self.seccode, captcha)

    def click_submit(self):

        # 登录按钮
        self.click(self.submit)

    def login(self, username, psw, captcha):

        #登录方法
        self.input_username(username)
        self.input_psw(psw)
        self.input_captcha(captcha)
        self.click_submit()



