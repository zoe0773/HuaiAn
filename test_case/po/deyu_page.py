# coding=utf-8

from test_case.po.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


# url = "http://157.0.0.59:50131/login"

class DeyuPage(Base):
    # 定位器，定位页面元素
    zhfw_link = (By.LINK_TEXT, "综合服务")  # 综合服务
    jwjx_link = (By.LINK_TEXT, "教务教学")  # 教务教学
    # bzsz_link = (By.XPATH, "")  # 标准设置
    label_fl = (By.CSS_SELECTOR, "div.add-item.nodeType>div>span:nth-child(1)>label")  # <label>分类</label>
    label_zb = (By.CSS_SELECTOR, "div.add-item.nodeType>div>span(2)>label")  # <label>指标</label>
    label_add = (By.CSS_SELECTOR, "div.add-item.scoreStrategy > div > span:nth-child(1) > label")  # <label>加分</label>
    zb_name = (By.CSS_SELECTOR, "input.name")  # 指标名称输入框
    tot = (By.CSS_SELECTOR, "div:nth-child(3)>div>input")  # 总分输入框
    fl = (By.CSS_SELECTOR, "div.add-item.nodeType > div > span:nth-child(1) > span > i")  # 分类单选按钮
    zb = (By.CSS_SELECTOR, "span.radio-box.clearfix.fl.ml90>span[name=\"node-type\"] > i")  # 指标单选按钮
    add__ = (By.CSS_SELECTOR, "div.add-item.scoreStrategy>div>span:nth-child(1)>span>i")  # 加分单选
    deduction = (By.CSS_SELECTOR, "div.add-item.scoreStrategy > div > span.radio-box.clearfix.fl.ml90 > span > i")  # 减分单选
    input1 = (By.CSS_SELECTOR, "div.add-item.pointScope>div>input.fromPoint")  # 加分范围输入框from
    input2 = (By.CSS_SELECTOR, "div.add-item.pointScope>div>input.toPoint")  # 加分范围输入框to
    text_area = (By.CSS_SELECTOR, "div.standard-deal.moral-standard.none>div>div.item-box>div:nth-child(5)>div>textarea")  # 描述输入框

    save_bt = (By.CSS_SELECTOR, "div>div.ctlSpace>span.borderCheck.save")  # 保存按钮
    dyfl_add = (By.XPATH,
                "//div[@class='moral-tree-list']/ul/li/ul/li[@class='active']/following-sibling::li/div[2]/div[class='node-ctl']/span[1]")
    sz_url = "http://157.0.0.59:50251/reps-moral-http/html/standard-base/standard-setting.html"

    def input_jwjx(self):
        # 登录后进入教务教学
        # 1.登录后定位综合服务
        # 2.点击教务教学
        # 3.定位标准设置
        self.move_to_element(self.zhfw_link)
        WebDriverWait(self.driver, 10).until(lambda i: i.find_element_by_link_text("教务教学")).click()
        # self.driver.get("http://157.0.0.59:50251/reps-moral-http/html/standard-base/standard-setting.html")
        # self.open("http://157.0.0.59:50251/reps-moral-http/html/standard-base/standard-setting.html")
        # ele = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//div[@class='wrap']div[@class='wrapL fl']/ul/li[4]/ul[@class='two_level']/li/a[@class='icon-standard-set']"))
        # self.click(ele)
        # self.click(self.bzsz_link)

    def open_bzsz(self):
        # 打开标准设置页面
        self.open(self.sz_url)


    def dy_menu(self, menu_name):

        # 定位德育分类（班级、学生、教师）
        #打开标准设置页面
        self.open_bzsz()
        ha_all = self.driver.window_handles
        self.driver.switch_to.window(ha_all[0])
        time.sleep(4)
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//div[@class='moral-tree-list']/ul/li/ul/li[@class='active']/following-sibling::li/div[2]/span/label[text()='%s']"%menu_name)).click()
        # 点击添加按钮
        time.sleep(5)
        self.driver.find_element_by_css_selector("div.tree-node.selected-style > div.node-ctl > span").click()
        #WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//div[@class='moral-tree-list']/ul/li/ul/li[@class='active']/div[2]/div[class='node-ctl']/span[1]").click()
        time.sleep(10)

    def input_name(self, name):
        # 输入指标名称
        self.send_keys(self.zb_name, name)


    def check_box_byName(self, name):
        time.sleep(10)

        # 选择单个考评方式
        ele = self.driver.find_element_by_xpath("//div[2]/div/span[1]/label[text()='%s']/following-sibling::span/i"%name)
        ele.click()

    def check_box_byTuple(self, args):
        # 选择考评方式：教师考评、学生自评、学生互评、家长考评(*args作为元组传递参数)
        for i in args:      #直接遍历
            self.check_box_byName(i)
        '''
        for i in range(len(args)):    #tuple类型遍历
            print(args[i])
            self.check_box_byName(args[i])
        '''

    def input_score(self, total, sco_from):
        # 输入总分
        self.send_keys(self.tot, total)
        # 加分范围
        self.send_keys(self.input1, sco_from)  # from
        self.send_keys(self.input2, total)  # to


    def input_text_area(self, textarea):
        # 描述
        self.send_keys(self.text_area, textarea)


    def click_save(self):
        # 点击保存 传入的是save button的定位选择器
        self.click(self.save_bt)


    def select_jd(self, taget_text, name, scor_text, des, total, sco_from, args):  # 节点文本jdname;des描述,scor_text加减分

            # 选择节点类型

        fl_text = self.find_element(self.label_fl).text #获取标签的文本  分类
        if  fl_text == taget_text:
            self.click(self.fl)         # 选择分类单选按钮
            self.input_name(name)       # 输入分类名称
            self.input_text_area(des)   # 添加描述
        else:
            # 选择指标按钮
            self.click(self.zb)
            # 输入指标名称
            self.input_name(name)
            # 选择加/减分制
            fz_text = self.find_element(self.label_add).text  #获取标签文本 加分
            if fz_text == scor_text:
                self.click(self.add__)    #点击选择加分单选按钮
            else:
                self.click(self.deduction)  #点击选择减分单选按钮
            # 选择考评方式
            self.check_box_byTuple(args)
            self.input_score(total, sco_from)
            self.input_text_area(des)


    def addzb(self, menuname, taget_text, name, scor_text, description,  args,total_scor=2, from_scor=1):
        # 1.登录后定位综合服务 hover
        # 2.点击教务教学
        self.input_jwjx()
        # 3.跳转标准设置页面
        # self.click(self.bzsz_link)
        # 4.选择德育分类，点击此分类后的添加按钮
        self.dy_menu(menuname)
        # 5.判断用户要添加的节点类型是分类还是指标 （分类/指标， 加分/减分， 考评方式）
        self.select_jd(taget_text, name, scor_text, description, total_scor, from_scor, args)
        # 6.保存
        self.click_save()
'''
    def addfl(self, menuname, taget_text, name, description):
        self.input_jwjx()
        self.dy_menu(menuname)
        
'''