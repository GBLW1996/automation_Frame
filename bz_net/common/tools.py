import hashlib
import os
import random
import re
import time

import pyautogui

from bz_net.common.cappic import Cappic
from te18183_com.common.warning import message
from bz_net.pages.basepage import BasePage
from bz_net.common.log import Logger
from selenium.webdriver import ActionChains
import clr
from certificateDll import *




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
            self.judge_jump(is_bt, is_judge_link, zx_txt, pg_tt, driver, is_mix, pc_bt_xpath, mo_bt_xpath, now_hd, pc_or_mobile)
            # time.sleep(2)

    def move_link(self, driver, m_start, m_end, link_start, link_end, move_xpath, jump_xpath, pc_or_mobile, is_mix, now_hd, is_btn, pc_bt_xpath, mo_bt_xpath):
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

    def jump_pg(self, driver, xpath, now_whd, is_mix, is_tt, home_link, pc_or_mobile, pc_bt_xpath, mo_bt_xpath):
        driver.find_element_by_xpath(xpath).click()
        BasePage(driver).wait(10)
        self.swich_handle(driver, now_whd)
        p_tt = driver.title
        if is_tt:
            res = self.judgestr(home_link, p_tt)
            if res:
                self.my_logger.info('官网"{}"跳转正常'.format(p_tt))
            else:
                self.my_logger.error('官网"{}"跳转异常'.format(p_tt))
                # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                Cappic(driver)
            if is_mix:
                try:
                    driver.find_element_by_xpath(pc_bt_xpath)
                    self.my_logger.info('页面"{}"按钮正常存在'.format(p_tt))
                except:
                    try:
                        driver.find_element_by_xpath(mo_bt_xpath)
                        self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"下载按钮异常'.format(p_tt))
                        # message('页面"{}"下载按钮异常'.format(pg_tt))
                        Cappic(driver)
            else:
                if pc_or_mobile == "pc":
                    try:
                        driver.find_element_by_xpath(pc_bt_xpath)
                        self.my_logger.info('页面"{}"按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"按钮异常'.format(p_tt))
                        # message('页面"{}"按钮异常'.format(pg_tt))
                        Cappic(driver)
                else:
                    try:
                        driver.find_element_by_xpath(mo_bt_xpath)
                        self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"手机下载按钮异常'.format(p_tt))
                        # message('页面"{}"手机下载按钮异常'.format(pg_tt))
                        Cappic(driver)
        else:
            if p_tt:
                self.my_logger.info('官网"{}"跳转正常'.format(p_tt))
            else:
                self.my_logger.error('官网"{}"跳转异常'.format(p_tt))
                # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                Cappic(driver)
            if is_mix:
                try:
                    driver.find_element_by_xpath(pc_bt_xpath)
                    self.my_logger.info('页面"{}"按钮正常存在'.format(p_tt))
                except:
                    try:
                        driver.find_element_by_xpath(mo_bt_xpath)
                        self.my_logger.info('页面"{}"手机下载按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"下载按钮异常'.format(p_tt))
                        # message('页面"{}"下载按钮异常'.format(pg_tt))
                        Cappic(driver)
            else:
                if pc_or_mobile == "pc":
                    try:
                        driver.find_element_by_xpath(pc_bt_xpath)
                        self.my_logger.info('页面"{}"按钮正常存在'.format(p_tt))
                    except:
                        self.my_logger.error('页面"{}"按钮异常'.format(p_tt))
                        # message('页面"{}"按钮异常'.format(pg_tt))
                        Cappic(driver)
                else:
                    try:
                        driver.find_element_by_xpath(mo_bt_xpath)
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
                self.my_logger.info('官网"{}"页跳转正常'.format(pg_tit))
            else:
                self.my_logger.error('官网"{}"页跳转异常'.format(pg_tit))
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
                self.my_logger.info('18183.com下载页"{}"跳转正常'.format(tt_downloader))
            else:
                self.my_logger.error('18183.com下载页"{}"页跳转异常'.format(tt_downloader))
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
        pyautogui.moveTo(x / 1920 * wi, y / 1080 * hei, duration=1.5)
        pyautogui.click(button='left')

    def move_link1(self, driver, link_start, link_end, move_xpath, jump_xpath, pc_or_mobile, is_mix, now_hd, is_btn, pc_bt_xpath, mo_bt_xpath):
        for x in range(link_start, link_end):
            ele = driver.find_element_by_xpath(move_xpath)
            ActionChains(driver).move_to_element(ele).perform()
            time.sleep(2)
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
                if pg_tt:
                    self.my_logger.info("页面{}正常".format(pg_tt))
                else:
                    self.my_logger.error('页面"{}"异常'.format(pg_tt))
                    # message('页面"{}"异常'.format(pg_tt))
                    Cappic(driver)
            self.close_hd_back(driver, now_hd)
            time.sleep(2)

    def ele_clicks(self, driver, xpaths, now_whd, is_bt, is_judge_link, is_mix, pc_bt_xpath, mo_bt_xpath, pc_or_mobile, is_attr, attr):
        res = driver.find_elements_by_xpath(xpaths)
        zx_txt = ''
        for i in res:
            if is_attr:
                zx_txt = i.get_attribute(attr)
            else:
                zx_txt = i.text
            driver.execute_script("arguments[0].click();", i)
            self.swich_handle(driver, now_whd)
            pg_tt = driver.title
            self.judge_jump(is_bt, is_judge_link, zx_txt, pg_tt, driver, is_mix, pc_bt_xpath, mo_bt_xpath, now_whd, pc_or_mobile)

    def judge_jump(self, is_bt, is_judge_link, zx_txt, pg_tt, driver, is_mix, pc_bt_xpath, mo_bt_xpath, now_hd, pc_or_mobile):
        # 判断页面跳转以及按钮
        if is_bt:
            if is_judge_link:
                judge = self.judgestr(zx_txt, pg_tt)
                if judge:
                    self.my_logger.info('官网"{}"跳转正常'.format(zx_txt))
                else:
                    self.my_logger.error('官网"{}"跳转异常'.format(zx_txt))
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
                    # my_logger.error('页面"{}"按钮异常'.format(pg_tt))
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
                    self.my_logger.info('官网"{}"跳转正常'.format(zx_txt))
                else:
                    self.my_logger.error('官网"{}"跳转异常'.format(zx_txt))
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

    def find_eles(self, driver, xpaths, is_attr, attr, which, which1, is_move_in, is_many, xpath, is_use_name, is_click,
                  now_whd, is_bt, is_judge_link):
        if is_many:
            try:
                xp_list = driver.find_elements_by_xpath(xpaths)
                lenth = len(xp_list)
                name = ''
                for i in xp_list:
                    if is_move_in:
                        ActionChains(driver).move_to_element(i).perform()
                        time.sleep(2)
                    if is_attr:
                        name = i.get_attribute(attr)
                    else:
                        name = i.text
                    if is_use_name:
                        if which1 != "":
                            self.my_logger.info("{}下{}：{}正常存在,共{}个,目前第{}个".format(which, which1, name, lenth, xp_list.index(i)+1))
                        else:
                            self.my_logger.info("{}:{}正常存在,共{}个,目前第{}个".format(which, name, lenth, xp_list.index(i)+1))
                    else:
                        if which1 != "":
                            self.my_logger.info("{}:{}正常存在,共{}个,目前第{}个".format(which, which1, lenth, xp_list.index(i)+1))
                        else:
                            self.my_logger.info("{}:正常存在,共{}个,目前第{}个".format(which, lenth, xp_list.index(i)+1))
                    if is_click:
                        # i.click()
                        driver.execute_script("arguments[0].click();", i)
                        self.swich_handle(driver, now_whd)
                        pg_tt = driver.title
                        self.judge_jump(is_bt, is_judge_link, name, pg_tt, driver, False, '', '', now_whd, '')
            except Exception as e:
                print(e)
                if which1 != "":
                    self.my_logger.error("{}：{}异常".format(which, which1))
                    # message("{}下{}异常".format(which, which1))
                else:
                    self.my_logger.error("{}异常".format(which))
                    # message("{}异常".format(which))
        else:
            try:
                ele_xp = driver.find_element_by_xpath(xpath)
                name = ''
                if is_move_in:
                    ActionChains(driver).move_to_element(ele_xp).perform()
                    time.sleep(1)
                if is_attr:
                    name = ele_xp.get_attribute(attr)
                else:
                    name = ele_xp.text
                if is_use_name:
                    if which1 != "":
                        self.my_logger.info("{}下{}：{}正常存在".format(which, which1, name))
                    else:
                        self.my_logger.info("{}下{}正常存在".format(which, name))
                else:
                    if which1 != "":
                        self.my_logger.info("{}下{}正常存在".format(which, which1))
                    else:
                        self.my_logger.info("{}下正常存在".format(which))
                if is_click:
                    ele_xp.click()
                    self.swich_handle(driver, now_whd)
                    pg_tt = driver.title
                    self.judge_jump(is_bt, is_judge_link, name, pg_tt, driver, False, '', '', now_whd, '')
            except:
                if which1 != "":
                    self.my_logger.error("{}下{}异常".format(which, which1))
                else:
                    self.my_logger.error("{}异常".format(which))

    def jump_in_current(self, begin, end, driver, xpath, is_ju_tt, is_attr, attr):
        for i in range(begin, end):
            link_txt = ''
            if is_attr:
                link_txt = driver.find_element_by_xpath(xpath.format(i)).get_attribute(attr)
            else:
                link_txt = driver.find_element_by_xpath(xpath.format(i)).text
            driver.find_element_by_xpath(xpath.format(i)).click()
            BasePage(driver).wait(10)
            p_tt = driver.title
            if is_ju_tt:
                res = self.judgestr(link_txt, p_tt)
                if res:
                    self.my_logger.info('官网"{}"跳转正常'.format(link_txt))
                else:
                    self.my_logger.error('官网"{}"跳转异常'.format(link_txt))
                    # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                    Cappic(driver)
            else:
                if p_tt:
                    self.my_logger.info('官网"{}"跳转正常'.format(p_tt))
                else:
                    self.my_logger.error('官网"{}"跳转异常'.format(p_tt))
                    # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                    Cappic(driver)
            time.sleep(2)
            BasePage(driver).back()
            time.sleep(2)

    def jump_eles_in_current(self, driver, xpaths, is_ju_tt, is_attr, attr):
        res = driver.find_elements_by_xpath(xpaths)
        print(res)
        print(driver.current_window_handle)
        for i in res:
            link_txt = ''
            if is_attr:
                link_txt = i.get_attribute(attr)
            else:
                link_txt = i.text
            i.click()
            BasePage(driver).wait(10)
            p_tt = driver.title
            if is_ju_tt:
                res = self.judgestr(link_txt, p_tt)
                if res:
                    self.my_logger.info('官网"{}"跳转正常'.format(link_txt))
                else:
                    self.my_logger.error('官网"{}"跳转异常'.format(link_txt))
                    # message('官网"{}"跳转异常'.format(zx_txt))
                    Cappic(driver)
            else:
                if p_tt:
                    self.my_logger.info('官网"{}"跳转正常'.format(p_tt))
                else:
                    self.my_logger.error('官网"{}"跳转异常'.format(p_tt))
                    # message('官网"{}"跳转异常'.format(zx_txt))
                    Cappic(driver)
            time.sleep(2)
            BasePage(driver).back()
            time.sleep(5)
            # BasePage(driver).refresh()
            # time.sleep(5)

    def click_a(self, driver, xpaths, is_attr, attr, which):
        res = driver.find_elements_by_xpath(xpaths)
        for i in res:
            txt = ''
            if is_attr:
                txt = i.get_attribute(attr)
            else:
                txt = i.text
            try:
                # i.click()
                driver.execute_script("arguments[0].click();", i)
                time.sleep(3)
                self.my_logger.info('官网"{}"模块"{}"点击正常,该元素共{}，目前是第{}个'.format(which, txt, len(res), res.index(i)+1))
            except:
                self.my_logger.error('官网"{}"模块"{}"点击异常,该元素共{}，目前是第{}个'.format(which, txt, len(res), res.index(i)+1))
                time.sleep(3)
                # message('官网{}模块{}点击异常'.format(which, txt))

    def find_eles1(self, driver, xpaths, is_attr, attr, which, which1, is_move_in, is_many, xpath, is_use_name, is_click,
                  now_whd, is_bt, is_judge_link):
        if is_many:
            xp_list = []
            try:
                xp_list = driver.find_elements_by_xpath(xpaths)
            except:
                if which1 != "":
                    self.my_logger.error('官网{}模块{}xpath获取不到元素列表'.format(which, which1))
                else:
                    self.my_logger.error('官网{}模块xpath获取不到元素列表'.format(which))
                    # message('官网{}模块xpath获取不到元素列表'.format(which))
                    return
            lenth = len(xp_list)
            name = ''
            for i in xp_list:
                if is_move_in:
                    try:
                        ActionChains(driver).move_to_element(i).perform()
                        time.sleep(2)
                    except:
                        if which1 != "":
                            self.my_logger.error('官网{}模块{}第{}个元素不能移动到，共{}个'.format(which, which1, xp_list.index(i)+1, len(xp_list)))
                            # message('官网{}模块{}第{}个元素不能移动，共{}个'.format(which, which1, xp_list.index(i)+1, len(xp_list)))
                        else:
                            self.my_logger.error('官网{}模块第{}个元素不能移动到，共{}个'.format(which, xp_list.index(i)+1, len(xp_list)))
                            # message('官网{}模块第{}个元素不能移动，共{}个'.format(which, xp_list.index(i)+1, len(xp_list)))
                if is_attr:
                    name = i.get_attribute(attr)
                else:
                    name = i.text
                if is_use_name:
                    if which1 != "":
                        self.my_logger.info("{}下{}：{}正常存在,共{}个,目前第{}个".format(which, which1, name, lenth, xp_list.index(i)+1))
                    else:
                        self.my_logger.info("{}:{}正常存在,共{}个,目前第{}个".format(which, name, lenth, xp_list.index(i)+1))
                else:
                    if which1 != "":
                        self.my_logger.info("{}:{}正常存在,共{}个,目前第{}个".format(which, which1, lenth, xp_list.index(i)+1))
                    else:
                        self.my_logger.info("{}:正常存在,共{}个,目前第{}个".format(which, lenth, xp_list.index(i)+1))
                if is_click:
                    i.click()
                    self.swich_handle(driver, now_whd)
                    pg_tt = driver.title
                    self.judge_jump(is_bt, is_judge_link, name, pg_tt, driver, False, '', '', now_whd, '')
        else:
            ele_xp = None
            try:
                ele_xp = driver.find_element_by_xpath(xpath)
            except:
                if which1 != "":
                    self.my_logger.error('官网{}模块{}xpath获取不到元素'.format(which, which1))
                    # message('官网{}模块xpath获取不到元素列表'.format(which))
                else:
                    self.my_logger.error('官网{}模块xpath获取不到元素'.format(which))
                    # message('官网{}模块xpath获取不到元素列表'.format(which))
                    return
            name = ''
            if is_move_in:
                try:
                    ActionChains(driver).move_to_element(ele_xp).perform()
                    time.sleep(1)
                except:
                    if which1 != "":
                        self.my_logger.error(
                            '官网{}模块{}元素不能移动到'.format(which, which1))
                        # message('官网{}模块{}第{}个元素不能移动，共{}个'.format(which, which1, xp_list.index(i)+1, len(xp_list)))
                    else:
                        self.my_logger.error('官网{}模块元素不能移动到'.format(which))
                        # message('官网{}模块第{}个元素不能移动，共{}个'.format(which, xp_list.index(i)+1, len(xp_list)))
            if is_attr:
                name = ele_xp.get_attribute(attr)
            else:
                name = ele_xp.text
            if is_use_name:
                if which1 != "":
                    self.my_logger.info("{}下{}：{}正常存在".format(which, which1, name))
                else:
                    self.my_logger.info("{}下{}正常存在".format(which, name))
            else:
                if which1 != "":
                    self.my_logger.info("{}下{}正常存在".format(which, which1))
                else:
                    self.my_logger.info("{}下正常存在".format(which))
            if is_click:
                ele_xp.click()
                self.swich_handle(driver, now_whd)
                pg_tt = driver.title
                self.judge_jump(is_bt, is_judge_link, name, pg_tt, driver, False, '', '', now_whd, '')


if __name__ == "__main__":
    md5_msg, num_name, time_msg = PageTool().downloader_msg(r"C:\Users\Administrator\Downloads\QQScLauncher.exe")
    print(md5_msg, "\n", num_name, "\n", time_msg, "\n")