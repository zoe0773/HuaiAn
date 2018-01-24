# coding=utf-8

from test_case.po.base import Base
from selenium.webdriver.common.by import By


# url = "http://157.0.0.59:50131/login"

class DeyuPage(Base):
    # 定位器，定位页面元素
    zhfw_link = (By.LINK_TEXT, "综合服务")  # 综合服务
    jwjx_link = (By.LINK_TEXT, "教务教学")  # 教务教学
    bzsz_link = (By.LINK_TEXT, "标准设置")  # 标准设置
    label_fl = (By.CSS_SELECTOR, "div.add-item nodeType>div>span(1)>label")  # <label>分类</label>
    label_zb = (By.CSS_SELECTOR, "div.add-item nodeType>div>span(2)>label")  # <label>指标</label>
    label_add = (By.CSS_SELECTOR, "div.add-item scoreStrategy>div>span(1)>label")  # <label>加分</label>
    label_ded = (By.CSS_SELECTOR, "div.add-item scoreStrategy>div>span(2)>label")  # <label>减分</label>
    bjdy = (By.CSS_SELECTOR, "li.active:nth-child(1)>div.tree-node selected-style>span>label.node-name")  # 班级德育分类
    bjdy_ad = (
    By.CSS_SELECTOR, "li.active:nth-child(1)>div.tree-node selected-style hoverStyle>div.node-ctl>span[1]")  # 指标添加按钮
    xsdy = (By.CSS_SELECTOR, "li.active:nth-child(2)>div.tree-node selected-style>span>label.node-name")  # 学生德育分类
    xsdy_ad = (
    By.CSS_SELECTOR, "li.active:nth-child(2)>div.tree-node selected-style hoverStyle>div.node-ctl>span[1]")  # 指标添加按钮
    jsdy = (By.CSS_SELECTOR, "li.active:nth-child(3)>div.tree-node selected-style>span>label.node-name")  # 教师德育分类
    jsdy_ad = (
    By.CSS_SELECTOR, "li.active:nth-child(3)>div.tree-node selected-style hoverStyle>div.node-ctl>span[1]")  # 指标添加按钮
    zb_name = (By.CSS_SELECTOR, "div.add-item:nth-child(2)>div.input>input.name")  # 指标名称输入框
    total = (By.CSS_SELECTOR, "from>div.add-item>div.input>input.totalScore")  # 总分输入框
    fl = (By.CSS_SELECTOR, "div.input clearfix>span.radio-box clearfix fl>span.myRadio active>i")  # 分类单选按钮
    zb = (By.CSS_SELECTOR, "span.radio-box clearfix fl ml90>span.myRadio active>i")  # 指标单选按钮
    add__ = (By.CSS_SELECTOR, "form:nth-child(1)>div.input clearfix>span.radio-box clearfix fl>span>i")  # 加分单选
    deduction = (By.CSS_SELECTOR, "form:nth-child(1)>div.input clearfix>span.radio-box clearfix fl ml90>span>i")  # 减分单选
    jskp = (By.CSS_SELECTOR, "div.add-item checkType>div.input clearfix:nth-child(1)>span>i")  # 教师考评checkBox
    stuzp = (By.CSS_SELECTOR, "div.add-item checkType>div.input clearfix:nth-child(2)>span>i")  # 学生自评checkBox
    stuhp = (By.CSS_SELECTOR, "div.add-item checkType>div.input clearfix:nth-child(3)>span>i")  # 学生互评checkBox
    parentkp = (By.CSS_SELECTOR, "div.add-item checkType>div.input clearfix:nth-child(4)>span>i")  # 家长考评checkBox
    input1 = (By.CSS_SELECTOR, "from>div.add-item pointScope>div.input>input.fromPoint")  # 加分范围输入框from
    input2 = (By.CSS_SELECTOR, "from>div.add-item pointScope>div.input>input.toPoint")  # 加分范围输入框to
    text_area = (By.CSS_SELECTOR, "div.add-item:nth-child(3)>div.input>textarea.describe")  # 描述输入框
    save_bt = (By.CSS_SELECTOR, "div.moral-type-deal>div.ctlSpace>span.borderCheck save")  # 保存按钮

    def input_jwjx(self):

        # 登录后进入教务教学
        # 1.登录后定位综合服务
        # 2.点击教务教学
        # 3.定位标准设置
        self.move_to_element(self.zhfw_link)
        self.select_by_text(self.jwjx_link, text="教务教学").click()
        self.click(self.bzsz_link)

    def input_name(self, name):
        # 输入指标名称
        self.send_keys(self.zb_name, name)

    def select_jd(self, taget_text):  # 节点文本
        # 选择节点类型
        if self.is_text_in_element(self.label_fl, taget_text):
            self.click(self.fl)
        elif self.is_text_in_element(self.label_zb, taget_text):
            self.click(self.zb)
        else:
            print("请选择正确节点")

    def select_fz(self, type_text):
        # 选择加/减分制
        if self.is_text_in_element(self.label_add, type_text):
            self.click(self.add__)
        elif self.is_text_in_element(self.label_ded, type_text):
            self.click(self.deduction)
        else:
            print("请选择正确分制")

    def select_kp(self, category, *args):

        # 选择考评方式：教师考评、学生自评、学生互评、家长考评(category传入的文本)
        pass

    def input_total(self, total):

        # 输入总分
        pass

    def input_range(self, range1, range2):

        # 加分范围
        pass

    def input_text_area(self, textarea):

        # 描述
        pass

    def click_save(self):

        # 点击保存 传入的是save button的定位选择器
        self.click(self.save_bt)

    def addzb(self):

        # 1.登录后定位综合服务 hover
        # 2.点击教务教学

        # 3.定位标准设置菜单

        # 4.选择德育分类，点击此分类后的添加按钮

        # 5.判断用户要添加的节点类型是分类还是指标 （分类/指标， 加分/减分， 考评方式）

        # 如果传入的参数是分类：

        try:

        # 输入名称

        # 点击选择分类按钮

        # 输入描述信息

        # 保存   print(成功添加分类%s名称)

        except Exception as a:
            print(a)

            # 如果是指标：

        try:
        # 1.输入名称

        # 2.点击选择指标按钮

        # 3.点击选择加分or减分

        # 4.选择考评方式

        # 5.输入总分值

        # 6.输入分值范围

        # 7.描述

        # 8.保存

        # 9.print()


        except Exception as a:
            print(a)

    def login(self, username, psw, captcha):

        # 登录方法
        self.input_username(username)
        self.input_psw(psw)
        self.input_captcha(captcha)
        self.click_submit()
