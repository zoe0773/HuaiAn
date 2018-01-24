#coding=utf-8

import os
import unittest
import HTMLTestRunner_jpg  #导入测试报告模块

#用例路径
case_path = os.path.join(os.getcwd(), "test_case")   #返回当前路径并拼接test_case

#报告存放路径
report_path= os.path.join(os.getcwd(), "report")

def all_case():

    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    #print(discover)
    return discover

if __name__ == "__main__":

    #runner = unittest.TextTestRunner()
    #runner.run(all_case())

    report_abspath = os.path.join(report_path, "result.html") #生成HTML文件
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp, title="淮安登录页面测试报告,测试结果如下：", description="用例执行情况：")
    runner.run(all_case())
    fp.close()
