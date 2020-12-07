import random
import time
import unittest

import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from zol_desk.common.warning import message
# from zol_desk.common.log import Logger
from zol_desk.common.cappic import Cappic
from zol_desk.pages.basepage import BasePage
import os
from selenium import webdriver
from zol_desk.common.tools import PageTool
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
path = os.path.abspath('..') + '\\downloads\\'
pre_fs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
options.add_experimental_option('prefs', pre_fs)
cwb = webdriver.Chrome(chrome_options=options)
net_183 = BasePage(cwb)
# my_logger = Logger(logger='2').getlog()
my_tools = PageTool()


class WywNet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        net_183.start_browser()

    @classmethod
    def tearDownClass(cls):
        # net_183.quit_browser()
        pass

    def test_01(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="headerWrap"]/div/div[1]/a', now_whd, False, True, False, "", "", '', False,
                            '', False, '')

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.move_in(cwb, '//*[@id="top_more_nav"]/span')
        time.sleep(2)
        my_tools.ele_clicks(cwb, '//*[@id="top_more_nav"]/div/dl[1]/dd/a', now_whd, False, False, False, '', '', '',
                            False, '', False, '//*[@id="top_more_nav"]/span')
        my_tools.ele_clicks(cwb, '//*[@id="top_more_nav"]/div/dl[2]/dd/a', now_whd, False, False, False, '', '', '',
                            False, '', False, '//*[@id="top_more_nav"]/span')
        my_tools.ele_clicks(cwb, '//*[@id="top_more_nav"]/div/dl[3]/dd/a', now_whd, False, False, False, '', '', '',
                            False, '', False, '//*[@id="top_more_nav"]/span')
        my_tools.ele_clicks(cwb, '//*[@id="top_more_nav"]/div/dl[4]/dd/a', now_whd, False, False, False, '', '', '',
                            False, '', False, '//*[@id="top_more_nav"]/span')
        my_tools.ele_clicks(cwb, '//*[@id="top_more_nav"]/div/p/a', now_whd, False, False, False, '', '', '', False, '',
                            False, '')

    def test_03(self):
        now_whd = cwb.current_window_handle
        my_tools.move_in(cwb, '//*[@id="headerWrap"]/div/div[3]/span')
        my_tools.ele_clicks(cwb, '//*[@id="headerWrap"]/div/div[3]/div/ul/li[1]/a', now_whd, False, False, False, '', ''
                            , '', False, '', True, '//*[@id="headerWrap"]/div/div[3]/span')
        my_tools.ele_clicks(cwb, '//*[@id="headerWrap"]/div/div[3]/div/ul/li[2]/a', now_whd, False, False, False, '', ''
                            , '', False, '', True, '//*[@id="headerWrap"]/div/div[3]/span')

    def test_04(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/a', now_whd, False, True, False, "", '', '', False, '',
                            False, '')

    def test_05(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[1]/div/ul/li/a', now_whd, False, False, False, '', '', '', True,
                            'target', False, '')

    def test_06(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[2]/div/div[2]/div/a', now_whd, False, False, False, '', '', '',
                            True, 'href', False, '')

    def test_07(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[2]/div/div[2]/ul/li/a', now_whd, False, False, False, '', '', ''
                            , False, '', False, '')

    def test_08(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="main"]/dl[1]/dd/a', now_whd, False, True, False, '', '', '', False, '', False
                            , '')

    def test_09(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="main"]/dl[2]/dd/a[1<position() and 6>position()]', now_whd, False, True,
                            False, '', '', '', False, '', True, '')
        my_tools.ele_clicks(cwb, '//*[@id="main"]/dl[2]/dd/a[6<position() and 12>position()]', now_whd, False, True,
                            False, '', '', '', False, '', True, '')
        my_tools.ele_clicks(cwb, '//*[@id="main"]/dl[3]/dd/a', now_whd, False, True, False, '', '', '', False, '', False
                            , '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div/div[2]/a[position()<25]', now_whd, False, True, False, ''
                            , '', '', False, '', False, '')

    def test_10(self):
        my_tools.wintowh(cwb, 0, 800)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="newPicList"]/li/a', now_whd, False, True, False, '', '', '', True, 'title',
                            False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[1]/ul/li/a', now_whd, False, True, False, '', '', '',
                            False, '', False, '')

    def test_11(self):
        my_tools.wintowh(cwb, 0, 1200)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul[2]/li/a', now_whd, False, True, False, '', '', '', True,
                            'title', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[2]/ul/li/a', now_whd, False, True, False, '', '', '',
                            True, 'title', False, '')

    def test_12(self):
        my_tools.wintowh(cwb, 0, 1600)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul[3]/li/a', now_whd, False, True, False, '', '', '', True,
                            'title', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[3]/ul/li/a', now_whd, False, True, False, '', '', '',
                            True, 'title', False, '')

    def test_13(self):
        my_tools.wintowh(cwb, 0, 2000)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul[4]/li/a', now_whd, False, True, False, '', '', '', True,
                            'title', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[4]/ul/li/a', now_whd, False, True, False, '', '', '',
                            True, 'title', False, '')

    def test_14(self):
        my_tools.wintowh(cwb, 0, 2400)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul[5]/li/a', now_whd, False, True, False, '', '', '', True,
                            'title', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[5]/ul/li/a', now_whd, False, True, False, '', '', '',
                            True, 'title', False, '')

    def test_15(self):
        my_tools.wintowh(cwb, 0, 2800)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul[6]/li/a', now_whd, False, True, False, '', '', '', True,
                            'title', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[6]/ul/li/a', now_whd, False, True, False, '', '', '',
                            True, 'title', False, '')

    def test_16(self):
        my_tools.wintowh(cwb, 0, 3200)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul[7]/li/a', now_whd, False, True, False, '', '', '', True,
                            'title', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[7]/ul/li/a', now_whd, False, True, False, '', '', '',
                            True, 'title', False, '')

    def test_17(self):
        my_tools.wintowh(cwb, 0, 3700)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div/em/a', now_whd, False, False, False, '', '', '', False, '', True
                            , '')

    def test_18(self):
        my_tools.wintowh(cwb, 0, 3700)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[9]/p/a', now_whd, False, True, False, '', '', '', False, '', False, '')

    def test_19(self):
        my_tools.wintowh(cwb, 0, 3700)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="zolGlobalFooter"]/div/div/span/a', now_whd, False, True, False, '', '', '',
                            False, '', True, '')

    def test_20(self):
        my_tools.wintowh(cwb, 0, 3700)
        try:
            cwb.find_element_by_xpath('//*[@id="backTop"]').click()
            my_tools.my_logger.info('回到顶部div点击正常')
        except:
            my_tools.my_logger.error('回到顶部div点击异常')

    def test_21(self):
        now_whd = cwb.current_window_handle
        str_list = ['美女', '风景', '可爱', '哈哈', '情侣']
        str1 = str_list[random.randint(1, 5)]
        try:
            cwb.find_element_by_xpath('//*[@id="softSearch"]').send_keys(str1+'\n')
            my_tools.swich_handle(cwb, now_whd)
            if str1 in cwb.title:
                my_tools.my_logger.info('搜索框功能正常')
            else:
                my_tools.my_logger.error('搜索框不能正常跳转')
        except:
            my_tools.my_logger.error('搜索框异常')
            message('搜索框异常')

    def test_22(self):
        # 电脑壁纸
        now_whd = cwb.current_window_handle
        txt = cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[2]/a').text
        cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[2]/a').click()
        my_tools.swich_handle(cwb, now_whd)
        tt = cwb.title
        res1 = my_tools.judgestr(txt, tt)
        if res1:
            my_tools.my_logger.info('{}模块点击成功'.format(txt))
        else:
            my_tools.my_logger.error('{}模块未跳转'.format(txt))
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div[1]/dl[1]/dd/a[position()>1]', now_whd, False, True, False
                            , '', '', '', False, '', True, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div[1]/dl[2]/dd/a[position()>1]', now_whd, False, True, False
                            , '', '', '', False, '', True, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div[1]/dl[3]/dd/a[position()>1]', now_whd, False, True, False
                            , '', '', '', False, '', True, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[1]/div[2]/div/a', now_whd, False, True, False, '', '', ''
                            , False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[1]/div[2]/ul/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul[1]/li/a/img', now_whd, False, True, False, '', '', '',
                            True, 'title', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[3]/ul/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '//*[@id="zdownrank"]/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[5]/div[2]/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul[2]/li/a/img', now_whd, False, True, False, '', '', '',
                            True, 'title', False, '')
        my_tools.ele_clicks_bt(cwb, '/html/body/div[6]/div[2]/div[6]/ul/li/a', now_whd, False, True, False, '', '', '',
                            False, '', False, '')

    def test_23(self):
        # 笔记本壁纸
        now_whd = cwb.current_window_handle
        txt = cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[3]').text
        cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[3]').click()
        my_tools.swich_handle(cwb, now_whd)
        tt = cwb.title
        res1 = my_tools.judgestr(txt, tt)
        if res1:
            my_tools.my_logger.info('{}模块点击成功'.format(txt))
        else:
            my_tools.my_logger.error('{}模块未跳转'.format(txt))
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul/li/a/img', now_whd, False, True, False, '', '', '',
                            True, 'title', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[1]/div[2]/ul/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[3]/ul/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '//*[@id="zdownrank"]/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[5]/div[2]/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[6]/ul/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')

    def test_24(self):
        # iapd壁纸
        now_whd = cwb.current_window_handle
        txt = cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[4]').text
        cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[4]').click()
        my_tools.swich_handle(cwb, now_whd)
        tt = cwb.title
        res1 = my_tools.judgestr(txt, tt)
        if res1:
            my_tools.my_logger.info('{}模块点击成功'.format(txt))
        else:
            my_tools.my_logger.error('{}模块未跳转'.format(txt))
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div/ul/li/a/img', now_whd, False, True, False, '', '', '', True,
                            'title', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[1]/div[2]/ul/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[3]/ul/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '//*[@id="zdownrank"]/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[5]/div[2]/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[6]/ul/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')

    def test_25(self):
        # 手机壁纸
        now_whd = cwb.current_window_handle
        txt = cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[5]').text
        cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[5]').click()
        my_tools.swich_handle(cwb, now_whd)
        tt = cwb.title
        res1 = my_tools.judgestr(txt, tt)
        if res1:
            my_tools.my_logger.info('{}模块点击成功'.format(txt))
        else:
            my_tools.my_logger.error('{}模块未跳转'.format(txt))
        now_whd = cwb.current_window_handle
        my_tools.move_in(cwb, '/html/body/div[4]/ul/li[1]/span')
        my_tools.ele_clicks(cwb, '//*[@id="bigSlideUl"]/li[position()>0 and position()<5]/a/img', now_whd, False, True,
                            False, '', '', '', True, 'alt', False, '/html/body/div[4]/ul/li[1]/span')
        my_tools.move_in(cwb, '/html/body/div[4]/ul/li[2]/span')
        my_tools.ele_clicks(cwb, '//*[@id="bigSlideUl"]/li[position()>4 and position()<9]/a/img', now_whd, False, True,
                            False, '', '', '', True, 'alt', False, '/html/body/div[4]/ul/li[2]/span')
        my_tools.move_in(cwb, '/html/body/div[4]/ul/li[3]/span')
        my_tools.ele_clicks(cwb, '//*[@id="bigSlideUl"]/li[position()>8 and position()<13]/a/img', now_whd, False, True,
                            False, '', '', '', True, 'alt', False, '/html/body/div[4]/ul/li[3]/span')
        my_tools.move_in(cwb, '/html/body/div[4]/ul/li[4]/span')
        my_tools.ele_clicks(cwb, '//*[@id="bigSlideUl"]/li[position()>12 and position()<17]/a/img', now_whd, False, True
                            , False, '', '', '', True, 'alt', False, '/html/body/div[4]/ul/li[4]/span')
        my_tools.move_in(cwb, '/html/body/div[4]/ul/li[5]/span')
        my_tools.ele_clicks(cwb, '//*[@id="bigSlideUl"]/li[position()>16 and position()<21]/a/img', now_whd, False, True
                            , False, '', '', '', True, 'alt', False, '/html/body/div[4]/ul/li[4]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div/ul/li/a', now_whd, False, True, False, '', '', '', True, 'title'
                            , False, '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div/div[2]/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '//*[@id="zdownrank"]/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '//*[@id="fjdownrank"]/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')
        my_tools.ele_clicks(cwb, '//*[@id="dmdownrank"]/li/a', now_whd, False, True, False, '', '',
                            '', False, '', False, '')

    def test_26(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="J_MainNav"]/li[position()>5]/a', now_whd, False, True, False, '', '', '',
                            False, '', False, '')


if __name__ == "__main__":
    unittest.main()