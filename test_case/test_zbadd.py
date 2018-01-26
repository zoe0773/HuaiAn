#coding=utf-8

import unittest
from test_case.po import base
from test_case.po.base import browser
from test_case.po import login_page
from test_case.po.deyu_page import DeyuPage
from test_case.po.login_page import LoginPage, url
from time import sleep


class Testcase1(unittest.TestCase):

    #登陆后，进入教务教学的德育模块添加指标

    def setUp(self):
        #初始化浏览器
        self.dri = base.browser()
        self.ad_zb = DeyuPage(self.dri)
        self.log_in = LoginPage(self.dri)
        self.log_in.open(url)
        self.log_in.login("szss", "111111", "3597")


    def addzb_case(self, mname, taget_t, jname, scor_text, description,  tot_scor, from_scor, expect=True, *args):

        '''标准设置添加指标或分类'''
        self.ad_zb.addzb(mname, taget_t, jname, scor_text, description, tot_scor, from_scor,*args)

    def test_add1(self):

        kp=("教师考评")
        '''为学生德育添加指标 关键字：学生德育、指标、加分、教师考评、10、1-2'''
        self.addzb_case("学生德育","指标","完成作业","加分","按完成作业情况加分", 3, 1,True,*kp)
        print(kp)

    def tearDown(self):
        sleep(10)
        self.dri.quit()

if __name__ == '__main__':

        unittest.main()
