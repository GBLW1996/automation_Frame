# coding=utf-8
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from jiegeng_net.common.cappic import Cappic
from jiegeng_net.common.log import Logger
from jiegeng_net.common.warning import message

mylogger = Logger(logger='basepage').getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    def __init__(self, driver):
        self.driver = driver

    def start_browser(self):
        mylogger.info("桔梗导航自动化测试开始")
        url = "https://www.jiegeng.com/"
        # 隐形等待10秒时间
        self.wait(10)
        # 跳转网页
        self.driver.get(url)
        # wait = WebDriverWait(self.driver, 20, 0.5)
        # # 使用匿名函数
        # wait.until(lambda diver: self.driver.find_element_by_class_name('phb'))
        mylogger.info("跳转至%s" % url)
        # 窗口最大化
        self.driver.maximize_window()
        mylogger.info("窗口已经最大化")
        # 调用截屏方法
        Cappic(self.driver)
        self.sleep(1)

    # quit browser and end testing
    def quit_browser(self):
        mylogger.info("桔梗导航自动化测试结束")
        # mylogger.info("当前浏览器版本:" + self.driver.capabilities['version'])
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        mylogger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        mylogger.info("Click back on current page.")

    # 浏览器刷新操作
    def refresh(self):
        self.driver.refresh()
        mylogger.info("Click refresh on current page.")

    # 模拟鼠标左键点击
    def click_by_xpath(self, xpath):
        txt = self.driver.find_element_by_xpath(xpath).text
        self.driver.find_element_by_xpath(xpath).click()
        mylogger.info("%s点击成功" % txt)

    def inputkeys_by_xpath(self, xpath, content):
        self.driver.find_element_by_xpath(xpath).send_keys(content)
        mylogger.info("%s搜索成功" % content)



    def wait(self, seconds):
        # 隐式等待
        self.driver.implicitly_wait(seconds)
        mylogger.info("隐性等待 %d 秒" % seconds)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        # mylogger.info("强制等待 %d 秒" % seconds)

    def title_judge(self, titname): # 定义标题判断方法
        title = self.driver.title
        if title == titname:
            mylogger.info(titname+"页面打开成功")
        else:
            mylogger.info(titname+"页面打开失败", exc_info=1)

    def titpd(self, titname):
        # 定义判断title的方法
        if titname in self.driver.title :
            mylogger.info("%s跳转成功" % titname)
        else:
            mylogger.error("%s跳转失败" % titname, exc_info=1)
            Cappic(self.driver)
            message("%s跳转失败" % titname)
            # 调用钉钉发送方法
            message("\n 服务挂了，速度来嗨"* 3)

    def radio_click(self,xpath):
        # 定义点击单选框页面跳转
        pages = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].click();", pages)
        # 获取原句柄
        window_1 = self.driver.current_window_handle
        # 获取所有句柄
        windows = self.driver.window_handles
        # self.sleep(2)
        for current_window in windows:
            if current_window != window_1:
                # 跳转至当前窗口的句柄
                self.driver.switch_to.window(current_window)
                tit = self.driver.title
                mylogger.info(tit + "打开成功")
                # self.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(window_1)

    def radio_enterkey(self, xpath):
        checkboxs = self.driver.find_elements_by_xpath(xpath)
        for k in checkboxs:
            k.send_keys(Keys.ENTER)
            window_1 = self.driver.current_window_handle
            windows = self.driver.window_handles
            # self.sleep(1)
            for current_window in windows:
                if current_window != window_1:
                    self.driver.switch_to.window(current_window)
                    tit = self.driver.title
                    mylogger.info(tit + "打开成功")
                    self.driver.close()
                    self.driver.switch_to.window(window_1)
                    # self.sleep(1)

    def check_click(self, xpath):
        checkboxs = self.driver.find_elements_by_xpath(xpath)
        for k in checkboxs:
            k.click()
            window_1 = self.driver.current_window_handle
            windows = self.driver.window_handles
            # self.sleep(1)
            for current_window in windows:
                if current_window != window_1:
                    self.driver.switch_to.window(current_window)
                    tit = self.driver.title
                    mylogger.info(tit + "打开成功")
                    self.driver.close()
                    self.driver.switch_to.window(window_1)
            # self.sleep(1)

    def radio_linktext_click(self, xpath):
         pages = self.driver.find_element_by_xpath(xpath)
         self.driver.execute_script("arguments[0].click();", pages)
         window_1 = self.driver.current_window_handle
         windows = self.driver.window_handles
         # self.sleep(1)
         for current_window in windows:
             if current_window != window_1:
                 self.driver.switch_to.window(current_window)
                 self.driver.close()
                 self.driver.switch_to.window(window_1)
                 # self.sleep(1)

    def radio_click_pd(self, xpath, titname):
        # 定义点击单选框页面跳转及title判断的方法
        pages = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].click();", pages)

    def check_click_pd(self, xpath, titname):
        checkboxs = self.driver.find_elements_by_xpath(xpath)
        for k in checkboxs:
            k.click()
            window_1 = self.driver.current_window_handle
            windows = self.driver.window_handles
            # self.sleep(1)
            for current_window in windows:
                if current_window != window_1:
                    self.driver.switch_to.window(current_window)
                    self.titpd(titname)
                    self.driver.close()
                    self.driver.switch_to.window(window_1)
                    # self.sleep(1)

    def check_list_pd(self, xpath, tit_list):
        checkboxs = self.driver.find_elements_by_xpath(xpath)
        for k in checkboxs:
            k.click()
            window_1 = self.driver.current_window_handle
            windows = self.driver.window_handles
            for current_window in windows:
                if current_window != window_1:
                    self.driver.switch_to.window(current_window)
                    # self.sleep(2)
                    tit = self.driver.title
                    if tit in tit_list:
                        mylogger.info("%s 页面打开成功" % tit)
                        # self.sleep(2)
                    else:
                        mylogger.info("%s 页面打开出错" % tit)
                        message("%s 页面打开出错" % tit)
                        Cappic(self.driver)
                    self.driver.close()
                    self.driver.switch_to.window(window_1)

    def switchframe(self, xpath):
        self.driver.switch_to.frame('myFrame')
        pages = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].click();", pages)
        window_1 = self.driver.current_window_handle
        windows = self.driver.window_handles
        # self.sleep(1)
        for current_window in windows:
            if current_window != window_1:
                self.driver.switch_to.window(current_window)
                tit = self.driver.title
                mylogger.info(tit + "打开成功")
                self.driver.close()
                self.driver.switch_to.window(window_1)
        self.driver.switch_to.default_content()