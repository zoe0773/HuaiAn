# coding=utf-8
from unittest import TestCase

from test_case.po import base
from test_case.po.base import browser
from test_case.po.login_page import LoginPage, url
import unittest
from selenium.webdriver.common.by import By
import time


class TestCase1(unittest.TestCase):
    # 登录页面的case
    @classmethod
    def setUpClass(cls):
        cls.driver = base.browser()
        cls.login = LoginPage(cls.driver)
        cls.login.open(url)
        cls.login.input_username("szss")
        cls.login.input_psw("111111")
        cls.login.input_captcha("3597")

        #cls.driver.implicitly_wait(120)


    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

    def login_case(self, username, psw, captcha, expect=True):  # expect 预期结果

        '''登录用例的方法'''
        # 1.输入用户名
        self.login.input_username(username)
        # 2.输入密码
        self.login.input_psw(psw)
        # 3.输入验证码
        self.login.input_captcha(captcha)
        # 4.点击登录
        self.login.click_submit()
        # 5.判断是否登录成功
        result = self.login.is_text_in_element(("link text", "szss"), "szss")
        # 6.期望结果
        ex_result = expect
        self.assertEqual(result, ex_result)

    def test_login01(self):
        '''输入正确的用户名密码验证码用户名：szss;密码：111111,验证码：3597'''
        self.login_case("szss", "111111", "3597", True)

    def test_login02(self):
        '''不输入用户名密码验证码'''
        self.login_case("", "", "", False)

    def test_login04(self):
        # 无效等价类
        '''输入正确的用户名、验证码，错误的密码'''
        self.login_case("szss", "123", "3597", False)

    def test_login03(self):
        # 无效等价类
        '''输入错误的用户名错误的密码，正确的验证码'''
        self.login_case("456", "123", "3597", False)


    def test_login05(self):
        # 无效等价类
        '''不输入用户名，输入正确的密码、验证码'''
        self.login_case("", "111111", "3597", False)


    def test_login06(self):
        '''只输入正确的验证码'''
        self.login_case("", "", "3597", False)


    def test_login07(self):
        # 无效等价类
        '''输入正确的用户名密码，错误的验证码'''
        self.login_case("szss", "111111", "111", False)

    def test_login08(self):
        # 无效等价类
        '''输入正确的用户名密码，不输入验证码'''
        self.login_case("szss", "111111", "", False)

    def test_login09(self):
        # 无效等价类
        '''输入正确的用户名，错误的密码、验证码'''
        self.login_case("szss", "0000", "00", False)

    def test_login10(self):
        # 无效等价类
        '''输入正确的用户名、验证码，错误的密码'''
        self.login_case("szss", "111", "3597", False)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
        unittest.main()
