import hashlib
import os
import random
import re
import time

import pyautogui

from fixdown_net.common.cappic import Cappic
from fixdown_net.common.warning import message
from fixdown_net.pages.basepage import BasePage
from fixdown_net.common.log import Logger
from selenium.webdriver import ActionChains
import clr
from certificateDll import *




class PageTool(object):
    my_logger = Logger(logger="2").getlog()
    def jump_link(self, driver, start, end, xpath, attr, is_judge_link, now_hd, pc_or_mobile, is_attr, is_bt, is_mix):
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
                        self.my_logger.info('fixdown首页"{}"跳转正常'.format(zx_txt))
                    else:
                        self.my_logger.error('fixdown首页"{}"跳转异常'.format(zx_txt))
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
                        driver.find_element_by_xpath('//div[@class="bt_abtn"]/a')
                        self.my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
                    except:
                        try:
                            driver.find_element_by_xpath('//ul[@class="clearfix"]/li/a')
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
                            driver.find_element_by_xpath('//div[@class="bt_abtn"]/a')
                            self.my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
                        except:
                            self.my_logger.error('页面"{}"按钮异常'.format(pg_tt))
                            # message('页面"{}"按钮异常'.format(pg_tt))
                            Cappic(driver)
                    else:
                        try:
                            driver.find_element_by_xpath('//ul[@class="clearfix"]/li/a')
                            self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(pg_tt))
                        except:
                            self.my_logger.error('页面"{}"手机下载按钮异常'.format(pg_tt))
                            # message('页面"{}"手机下载按钮异常'.format(pg_tt))
                            Cappic(driver)
            else:
                if is_judge_link:
                    judge = self.judgestr(zx_txt, pg_tt)
                    if judge:
                        self.my_logger.info('fixdown首页"{}"跳转正常'.format(zx_txt))
                    else:
                        self.my_logger.error('fixdown首页"{}"跳转异常'.format(zx_txt))
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

    def move_link(self, driver, m_start, m_end, link_start, link_end, move_xpath, jump_xpath, pc_or_mobile, is_mix, now_hd, is_btn):
        for i in range(m_start, m_end):
            ele = driver.find_element_by_xpath(move_xpath.format(i))
            ActionChains(driver).move_to_element(ele).perform()
            for x in range(link_start, link_end):
                driver.find_element_by_xpath(jump_xpath.format(x)).click()
                BasePage(driver).wait(10)
                self.swich_handle(driver, now_hd)
                pg_tt = driver.title
                if is_btn:
                    if pg_tt:
                        self.my_logger.info('页面"{}"跳转正常'.format(pg_tt))
                    else:
                        self.my_logger.error('页面"{}"跳转异常'.format(pg_tt))
                        # message('页面"{}"跳转异常'.format(pg_tt))
                        Cappic(driver)
                    if is_mix:
                        try:
                            driver.find_element_by_xpath('//div[@class="bt_abtn"]/a')
                            self.my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
                        except:
                            try:
                                driver.find_element_by_xpath('//ul[@class="clearfix"]/li/a')
                                self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(pg_tt))
                            except:
                                self.my_logger.error('页面"{}"下载按钮异常'.format(pg_tt))
                                # message('页面"{}"下载按钮异常'.format(pg_tt))
                                Cappic(driver)
                    else:
                        if pc_or_mobile == "pc":
                            try:
                                driver.find_element_by_xpath('//div[@class="bt_abtn"]/a')
                                self.my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
                            except:
                                self.my_logger.error('页面"{}"按钮异常'.format(pg_tt))
                                # message('页面"{}"按钮异常'.format(pg_tt))
                                Cappic(driver)
                        else:
                            try:
                                driver.find_element_by_xpath('//ul[@class="clearfix"]/li/a')
                                self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(pg_tt))
                            except:
                                self.my_logger.error('页面"{}"手机下载按钮异常'.format(pg_tt))
                                # message('页面"{}"手机下载按钮异常'.format(pg_tt))
                                Cappic(driver)
                else:
                    if pg_tt:
                        self.my_logger.info("页面{}正常".format(pg_tt))
                    else:
                        self.my_logger.error('页面"{}"异常'.format(pg_tt))
                        # message('页面"{}"异常'.format(pg_tt))
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

    def jump_pg(self, driver, xpath, now_whd, is_mix, is_tt, home_link, pc_or_mobile):
        driver.find_element_by_xpath(xpath).click()
        BasePage(driver).wait(10)
        self.swich_handle(driver, now_whd)
        p_tt = driver.title
        if is_tt:
            res = self.judgestr(home_link, p_tt)
            if res:
                self.my_logger.info('fixdown首页"{}"跳转正常'.format(p_tt))
            else:
                self.my_logger.error('fixdown首页"{}"跳转异常'.format(p_tt))
                # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                Cappic(driver)
            if is_mix:
                try:
                    driver.find_element_by_xpath('//div[@class="bt_abtn"]/a')
                    self.my_logger.info('页面"{}"按钮正常存在'.format(p_tt))
                except:
                    try:
                        driver.find_element_by_xpath('//ul[@class="clearfix"]/li/a')
                        self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"下载按钮异常'.format(p_tt))
                        # message('页面"{}"下载按钮异常'.format(pg_tt))
                        Cappic(driver)
            else:
                if pc_or_mobile == "pc":
                    try:
                        driver.find_element_by_xpath('//div[@class="bt_abtn"]/a')
                        self.my_logger.info('页面"{}"按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"按钮异常'.format(p_tt))
                        # message('页面"{}"按钮异常'.format(pg_tt))
                        Cappic(driver)
                else:
                    try:
                        driver.find_element_by_xpath('//ul[@class="clearfix"]/li/a')
                        self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"手机下载按钮异常'.format(p_tt))
                        # message('页面"{}"手机下载按钮异常'.format(pg_tt))
                        Cappic(driver)
        else:
            if p_tt:
                self.my_logger.info('fixdown首页"{}"跳转正常'.format(p_tt))
            else:
                self.my_logger.error('fixdown首页"{}"跳转异常'.format(p_tt))
                # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                Cappic(driver)
            if is_mix:
                try:
                    driver.find_element_by_xpath('//div[@class="bt_abtn"]/a')
                    self.my_logger.info('页面"{}"按钮正常存在'.format(p_tt))
                except:
                    try:
                        driver.find_element_by_xpath('//ul[@class="clearfix"]/li/a')
                        self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"下载按钮异常'.format(p_tt))
                        # message('页面"{}"下载按钮异常'.format(pg_tt))
                        Cappic(driver)
            else:
                if pc_or_mobile == "pc":
                    try:
                        driver.find_element_by_xpath('//div[@class="bt_abtn"]/a')
                        self.my_logger.info('页面"{}"按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"按钮异常'.format(p_tt))
                        # message('页面"{}"按钮异常'.format(pg_tt))
                        Cappic(driver)
                else:
                    try:
                        driver.find_element_by_xpath('//ul[@class="clearfix"]/li/a')
                        self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"手机下载按钮异常'.format(p_tt))
                        # message('页面"{}"手机下载按钮异常'.format(pg_tt))
                        Cappic(driver)
        self.close_hd_back(driver, now_whd)
        time.sleep(2)

    def jump_without_hd(self, driver, start, end, xpath, now_hd):
        for i in range(start, end):
            driver.find_element_by_xpath(xpath.format(i)).click()
            self.swich_handle(driver, now_hd)
            pg_tit = driver.title
            if pg_tit:
                self.my_logger.info('fixdown"{}"页跳转正常'.format(pg_tit))
            else:
                self.my_logger.error('fixdown"{}"页跳转异常'.format(pg_tit))
                # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                Cappic(driver)
            time.sleep(5)
            BasePage(driver).back()

    def jump_link_pg(self, driver, start, end, xpath, now_hd, xpaths, xpaths1):
        r_n = random.randint(start, end-1)
        print(r_n)
        for i in range(start, end):
            driver.find_element_by_xpath(xpath.format(i)).click()
            self.swich_handle(driver, now_hd)
            BasePage(driver).wait(10)
            pg_tt = driver.title
            if pg_tt:
                self.my_logger.info('页面{}跳转正常'.format(pg_tt))
            else:
                self.my_logger.error('页面{}跳转异常'.format(pg_tt))
                self.close_hd_back(driver, now_hd)
                Cappic(driver)
                break
                # message('页面"{}"跳转异常'.format(pg_tt))
            # self.wintowh(driver, 0, 3200)
            # all_links = int(driver.find_element_by_xpath(
            #     '// *[ @ id = "main1k"] / div[2] / div[1] / div[3] / div / a[1] / b').text)
            # pg_num, which = self.pages_links(all_links, 25)
            res = driver.find_elements_by_xpath(xpaths)
            random_pg = random.randint(2, len(res)-2)
            res[random_pg].click()
            res1 = driver.find_elements_by_xpath(xpaths1)
            random_link = random.randint(2, len(res1)-1)
            res1[random_link].click()
            self.swich_handle(driver, now_hd)
            tt_downloader = driver.title
            if tt_downloader:
                self.my_logger.info('fixdown下载页"{}"跳转正常'.format(tt_downloader))
            else:
                self.my_logger.error('fixdown下载页"{}"页跳转异常'.format(tt_downloader))
                # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                Cappic(driver)
            try:
                driver.find_element_by_xpath('//*[@id="main1k"]/div[3]/div[2]/div[2]/div[2]/div[2]/a')
                self.my_logger.info('页面"{}"按钮正常存在'.format(tt_downloader))
                if i == r_n:
                    driver.find_element_by_xpath('//*[@id="main1k"]/div[3]/div[2]/div[2]/div[2]/div[2]/a').click()
                    # driver.find_element_by_xpath('//*[@id="xzqdzbox"]/div[2]/div[2]/div/div/div/dl[1]/dd/div[1]/img[1]').click()
                    time.sleep(10)
                    self.mouse_do(1900, 1000)
                    filename = ""
                    for root, dirs, files in os.walk(os.path.abspath('..') + '\\downloads\\'):
                        # print(root)  # 当前目录路径
                        # print(dirs)  # 当前路径下所有子目录
                        # print(files[-1])  # 当前路径下所有非目录子文件
                        filename = files[-1]
                    filename1 = os.path.abspath('..') + '\\downloads\\' + filename
                    md5_msg, num_name, time_msg = self.downloader_msg(filename1)
                    self.my_logger.info(
                        '下载页面{}按钮的信息:\nmd5:{}\n数字签名:{}\n时间戳:{}'.format(tt_downloader, md5_msg, num_name, time_msg))
                    time.sleep(2)
                self.close_hd_back(driver, now_hd)
                time.sleep(3)
            except:
                try:
                    driver.find_element_by_xpath('//*[@id="zcgs"]/div[2]/ul/li[1]/a')
                    self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(tt_downloader))
                    if r_n == i:
                        driver.find_element_by_xpath('//*[@id="zcgs"]/div[2]/ul/li[1]/a').click()
                        time.sleep(10)
                        self.mouse_do(1900, 1000)
                        filename = ""
                        for root, dirs, files in os.walk(os.path.abspath('..') + '\\downloads\\'):
                            # print(root)  # 当前目录路径
                            # print(dirs)  # 当前路径下所有子目录
                            # print(files[-1])  # 当前路径下所有非目录子文件
                            filename = files[-1]
                        filename1 = os.path.abspath('..') + '\\downloads\\' + filename
                        md5_msg, num_name, time_msg = self.downloader_msg(filename1)
                        self.my_logger.info(
                            '下载页面{}按钮的信息:\nmd5:{}\n数字签名:{}\n时间戳:{}'.format(tt_downloader, md5_msg, num_name, time_msg))
                        time.sleep(2)
                    self.close_hd_back(driver, now_hd)
                    time.sleep(3)
                except:
                    self.my_logger.error('页面"{}"下载按钮异常'.format(tt_downloader))
                    # message('页面"{}"下载按钮异常'.format(pg_tt))
                    Cappic(driver)
                    self.close_hd_back(driver, now_hd)

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
        pyautogui.moveTo(x / 1920 * wi, y / 1080 * hei, duration=0.9)
        pyautogui.click(button='left')
        
    def ele_clicks(self, driver, xpaths, now_whd, is_bt, is_judge_link, is_mix, pc_bt_xpath, mo_bt_xpath, pc_or_mobile, attr,
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

    def judge_jump(self, is_bt, is_judge_link, zx_txt, pg_tt, driver, is_mix, pc_bt_xpath, mo_bt_xpath, now_hd, pc_or_mobile
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
                    # self.self.self.my_logger.error('页面"{}"按钮异常'.format(pg_tt))
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