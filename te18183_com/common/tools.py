import hashlib
import os
import random
import re
import time

import pyautogui

from te18183_com.common.cappic import Cappic
from te18183_com.common.warning import message
from te18183_com.pages.basepage import BasePage
from te18183_com.common.log import Logger
from selenium.webdriver import ActionChains
import clr
from certificateDll import *

# my_logger = Logger(logger="2").getlog()


class PageTool(object):
    my_logger = Logger(logger="2").getlog()
    def jump_link(self, driver, start, end, xpath, attr, is_judge_link, now_hd, pc_or_mobile, is_attr, is_bt, is_mix, pc_bt_xpath, mo_bt_xpath):
        # driver 循环开始 循环结束 xpath 页面文字属性 是否对比文字和title 当前窗口句柄（最好填首页句柄） pc或者app 按属性还是text 是否有按钮 是否有pc也有app
        for i in range(start, end):
            zx_txt = ""
            if is_attr:
                zx_txt = driver.find_element_by_xpath(xpath.format(i)).get_attribute(attr)
            else:
                zx_txt = driver.find_element_by_xpath(xpath.format(i)).text
            driver.find_element_by_xpath(xpath.format(i)).click()
            self.swich_handle(driver, now_hd)
            BasePage(driver).wait(10)

            pg_tt = driver.title

            if is_bt:
                if is_judge_link:
                    judge = self.judgestr(zx_txt, pg_tt)
                    if judge:
                        self.my_logger.info('18183.com首页"{}"跳转正常'.format(zx_txt))
                    else:
                        self.my_logger.error('18183.com首页"{}"跳转异常'.format(zx_txt))
                        # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                        Cappic(driver)
                else:
                    if pg_tt:
                        self.my_logger.info('页面"{}"跳转正常'.format(pg_tt))
                    else:
                        self.my_logger.error('页面"{}"跳转异常'.format(pg_tt))
                        # message('页面"{}"跳转异常'.format(pg_tt))
                        Cappic(driver)
                if is_mix:
                    try:
                        driver.find_element_by_xpath(pc_bt_xpath)
                        self.my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
                    except:
                        try:
                            driver.find_element_by_xpath(mo_bt_xpath)
                            self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(pg_tt))
                        except:
                            self.my_logger.error('页面"{}"下载按钮异常'.format(pg_tt))
                            # message('页面"{}"下载按钮异常'.format(pg_tt))
                            Cappic(driver)
                        # self.my_logger.error('页面"{}"按钮异常'.format(pg_tt))
                        # message('页面"{}"按钮异常'.format(pg_tt))
                        # Cappic(driver)
                else:
                    if pc_or_mobile == "pc":
                        try:
                            driver.find_element_by_xpath(pc_bt_xpath)
                            self.my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
                        except:
                            self.my_logger.error('页面"{}"按钮异常'.format(pg_tt))
                            # message('页面"{}"按钮异常'.format(pg_tt))
                            Cappic(driver)
                    else:
                        try:
                            driver.find_element_by_xpath(mo_bt_xpath)
                            self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(pg_tt))
                        except:
                            self.my_logger.error('页面"{}"手机下载按钮异常'.format(pg_tt))
                            # message('页面"{}"手机下载按钮异常'.format(pg_tt))
                            Cappic(driver)
            else:
                if is_judge_link:
                    judge = self.judgestr(zx_txt, pg_tt)
                    if judge:
                        self.my_logger.info('18183.com首页"{}"跳转正常'.format(zx_txt))
                    else:
                        self.my_logger.error('18183.com首页"{}"跳转异常'.format(zx_txt))
                        # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                        Cappic(driver)
                else:
                    if pg_tt:
                        self.my_logger.info('页面"{}"跳转正常'.format(pg_tt))
                    else:
                        self.my_logger.error('页面"{}"跳转异常'.format(pg_tt))
                        # message('页面"{}"跳转异常'.format(pg_tt))
                        Cappic(driver)
            self.close_hd_back(driver, now_hd)
            time.sleep(2)

    def wintobt(self, driver):
        # 滚动条到最底下
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        time.sleep(2)

    def wintowh(self, driver, x, y):
        # 滚动条横竖向任意滚动
        js = "window.scrollTo({},{})".format(x, y)
        driver.execute_script(js)
        time.sleep(2)

    def close_hd_back(self, driver, now_wd):
        # 关闭所有标签页并切换句柄回到主页
        dr_hds = driver.window_handles
        for i in dr_hds:
            if i != now_wd:
                driver.switch_to.window(i)
                driver.close()
        driver.switch_to.window(now_wd)

    def swich_handle(self, driver, now_hd):
        # 切换窗口句柄
        win_hds = driver.window_handles
        driver.switch_to.window(win_hds[-1])

    def judgestr(self, lin_txt, tt):
        # 首页链接文字,第二页title
        res = []
        for x in lin_txt:
            if x in tt:
                res.append(x)
        if len(res) / len(lin_txt) >= 0.3:
            return res
        else:
            return False

    def random_two_num(self, num1, num2):
        re_num1 = random.randint(1, num1)
        re_num2 = random.randint(1, num2)
        return re_num1, re_num2

    def pages_links(self, all_links, every_page):
        num1 = random.randint(1, all_links)
        num2 = num1 % every_page
        pages = num1 // every_page
        num3 = 0
        if num2 != 0:
            pages += 1
            num3 = num2
        else:
            num3 = every_page
        return pages, num3

    def downloader_msg(self, filename):
        with open(filename, "rb") as f:
            data = f.read()
            m = hashlib.md5()
            m.update(data)
            md5_msg = m.hexdigest()
        clr.AddReference('certificateDll')
        certificate_information = certificate.getCert(filename)
        certificate_information = str(certificate_information)
        digital_signature = re.findall(r'CN=.+C=CN', certificate_information)
        digital_moment = digital_signature[0]
        digital_signature_data = str(digital_moment[3:-6])
        # digital_signature_data数字签名
        timestamp = re.findall(r'signDate.+', certificate_information)
        timestamp_moment = timestamp[0]
        timestamp_data = str(timestamp_moment[11:-2])
        return md5_msg, digital_signature_data, timestamp_data

    def mouse_do(self, x, y):
        wi, hei = pyautogui.size()
        pyautogui.moveTo(x / 1920 * wi, y / 1080 * hei, duration=1.5)
        pyautogui.click(button='left')

    def ele_clicks(self, driver, xpaths, now_whd, is_bt, is_judge_link, is_mix, pc_bt_xpath, mo_bt_xpath, pc_or_mobile,
                   attr,
                   is_back, mv_xp, click_xp):
        res = []
        try:
            res = driver.find_elements_by_xpath(xpaths)
        except:
            self.my_logger.error('xpath有误,站点结构改了？')
            message('xpath有误,站点结构改了？')
            return
        lenth = len(res)
        w = 0
        for i in res:
            w += 1
            res1 = driver.find_elements_by_xpath(xpaths)
            res2 = res1[w - 1]
            zx_txt = ''
            if attr != '':
                zx_txt = res2.get_attribute(attr)
            else:
                zx_txt = res2.text
            driver.execute_script("arguments[0].click();", res2)
            time.sleep(2)
            self.swich_handle(driver, now_whd)
            pg_tt = driver.title
            self.judge_jump(is_bt, is_judge_link, zx_txt, pg_tt, driver, is_mix, pc_bt_xpath, mo_bt_xpath, now_whd,
                            pc_or_mobile, is_back, mv_xp, lenth, w, click_xp)

    def judge_jump(self, is_bt, is_judge_link, zx_txt, pg_tt, driver, is_mix, pc_bt_xpath, mo_bt_xpath, now_hd,
                   pc_or_mobile
                   , is_back, mv_xp, lenth, w, click_xp):
        # 判断页面跳转以及按钮
        if is_bt:
            if is_judge_link:
                judge = self.judgestr(zx_txt, pg_tt)
                if judge:
                    self.my_logger.info('页面"{}"跳转正常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                else:
                    self.my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                    # message('desk.zol页面"{}"跳转异常'.format(zx_txt))
                    Cappic(driver)
            else:
                if pg_tt:
                    code_sta = self.page_tt_code(pg_tt)
                    if code_sta:
                        self.my_logger.info('页面"{}"跳转正常,该类元素共{}个，当前第{}个'.format(pg_tt, lenth, w))
                    else:
                        self.my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(pg_tt, lenth, w))
                        # message('页面"{}"跳转异常'.format(pg_tt))
                        Cappic(driver)
                else:
                    self.my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                    # message('页面"{}"跳转异常'.format(pg_tt))
                    Cappic(driver)
            if is_mix:
                try:
                    driver.find_element_by_xpath(pc_bt_xpath)
                    self.my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
                except:
                    try:
                        driver.find_element_by_xpath(mo_bt_xpath)
                        self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(pg_tt))
                    except:
                        self.my_logger.error('页面"{}"下载按钮异常'.format(pg_tt))
                        # message('页面"{}"下载按钮异常'.format(pg_tt))
                        Cappic(driver)
                    # self.self.my_logger.error('页面"{}"按钮异常'.format(pg_tt))
                    # message('页面"{}"按钮异常'.format(pg_tt))
                    # Cappic(driver)
            else:
                if pc_or_mobile == "pc":
                    try:
                        driver.find_element_by_xpath(pc_bt_xpath)
                        self.my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
                    except:
                        self.my_logger.error('页面"{}"按钮异常'.format(pg_tt))
                        # message('页面"{}"按钮异常'.format(pg_tt))
                        Cappic(driver)
                else:
                    try:
                        driver.find_element_by_xpath(mo_bt_xpath)
                        self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(pg_tt))
                    except:
                        self.my_logger.error('页面"{}"手机下载按钮异常'.format(pg_tt))
                        # message('页面"{}"手机下载按钮异常'.format(pg_tt))
                        Cappic(driver)
        else:
            if is_judge_link:
                judge = self.judgestr(zx_txt, pg_tt)
                if judge:
                    self.my_logger.info('页面"{}"跳转正常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                else:
                    self.my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                    # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                    Cappic(driver)
            else:
                if pg_tt:
                    code_sta = self.page_tt_code(pg_tt)
                    if code_sta:
                        self.my_logger.info('页面"{}"跳转正常,该类元素共{}个，当前第{}个'.format(pg_tt, lenth, w))
                    else:
                        self.my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(pg_tt, lenth, w))
                        # message('页面"{}"跳转异常'.format(pg_tt))
                        Cappic(driver)
                else:
                    self.my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                    # message('页面"{}"跳转异常'.format(pg_tt))
                    Cappic(driver)
        if is_back:
            BasePage(driver).back()
            time.sleep(2)
        else:
            self.close_hd_back(driver, now_hd)
            time.sleep(2)
        if mv_xp != '':
            self.move_in(driver, mv_xp)
            time.sleep(1)
        if click_xp != '':
            home_ele = driver.find_element_by_xpath(click_xp)
            driver.execute_script("arguments[0].click();", home_ele)

    def move_in(self, driver, xpath):
        ele = driver.find_element_by_xpath(xpath)
        ActionChains(driver).move_to_element(ele).perform()
        time.sleep(2)

    def page_tt_code(self, pg_tt):
        list_worn = ['401', '402', '403', '404', '405', '406', '407', '408', '409', '501', '502', '503', '504',
                     '505', '506', '507', '508', '509']
        for u in list_worn:
            if u in pg_tt:
                return False
        return True

    def static_click(self, driver, res):
        driver.execute_script("arguments[0].click();", res)


if __name__ == "__main__":
    md5_msg, num_name, time_msg = PageTool().downloader_msg(r"C:\Users\Administrator\Downloads\QQScLauncher.exe")
    print(md5_msg, "\n", num_name, "\n", time_msg, "\n")