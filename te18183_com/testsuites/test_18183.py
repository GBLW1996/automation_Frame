import random
import time
import unittest

import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from te18183_com.common.warning import message
# from te18183_com.common.log import Logger
from te18183_com.common.cappic import Cappic
from te18183_com.pages.basepage import BasePage
import os
from selenium import webdriver
from te18183_com.common.tools import PageTool
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
        my_tools.ele_clicks(cwb, '/html/body/div[1]/div/div/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_02(self):
        now_whd = cwb.current_window_handle
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[1]/div/div/div[3]/div/dl'))+1):
            my_tools.move_in(cwb, '/html/body/div[1]/div/div/div[3]/a/span')
            my_tools.ele_clicks(cwb, '/html/body/div[1]/div/div/div[3]/div/dl[{}]/dd/a'.format(i), now_whd, 0, 0, 0, '',
                                '', '', '', 0, '/html/body/div[1]/div/div/div[3]/a/span', '')

    def test_03(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_04(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div/ul/li/a', now_whd, 0, 0, 0, '', '', '', 'title', 0, '',
                            '')

    def test_05(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="topindex20160"]/a/img', now_whd, 0, 0, 0, '', '', '', 'src', 0, '', '')

    def test_06(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[1]/div[3]/div[1]/ul/li/a', now_whd, 1, 0, 1,
                            '/html/body//span[text()="电脑版下载"]', '/html/body//span[text()="安卓版下载"]', '', 'title',
                            0, '', '')


    def test_07(self):
        now_whd = cwb.current_window_handle
        my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div[1]/div[2]/ul/li[2]/a')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[1]/div[3]/div[2]/div[1]/p/a', now_whd, 0, 0, 0, '', '',
                            '', '', 0, '/html/body/div[5]/div[3]/div[1]/div[2]/ul/li[2]/a', '')
        my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div[1]/div[2]/ul/li[2]/a')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[1]/div[3]/div[2]/div[2]/a', now_whd, 0, 0, 0, '', '',
                            '', '', 0, '/html/body/div[5]/div[3]/div[1]/div[2]/ul/li[2]/a', '')
        my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div[1]/div[2]/ul/li[3]/a')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[1]/div[3]/div[3]/div[2]/div[1]/div/p/a', now_whd, 0, 0, 0
                            , '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[1]/div[3]/div[3]/div[2]/div/div/a', now_whd, 0, 0, 0, '',
                            '', '', '', 0, '', '')

    def test_08(self):
        # 轮播图
        my_tools.wintowh(cwb, 0, 600)
        now_whd = cwb.current_window_handle
        time.sleep(2)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="point_news"]/div[1]/div[1]/div/span'))+1):
            cwb.find_element_by_xpath('//*[@id="point_news"]/div[1]/div[1]/div/span[{}]'.format(i)).click()
            time.sleep(0.5)
            my_tools.mouse_do(480, 540)
            my_tools.close_hd_back(cwb, now_whd)

    def test_09(self):
        my_tools.wintowh(cwb, 0, 650)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="point_news"]/div[1]/div[2]/div/div/a', now_whd, 0, 0, 0, '', '', '', 'title',
                            0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="point_news"]/div[1]/div[2]/ul/li/a/p/strong', now_whd, 0, 0, 0, '', '', '',
                            '', 0, '', '')

    def test_10(self):
        my_tools.wintowh(cwb, 0, 650)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="point_news"]/div[2]/div/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_11(self):
        my_tools.wintowh(cwb, 0, 650)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="indextxtrd0"]/a', now_whd, 0, 0, 0, '', '', '', 'href', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="point_news"]/div[3]/div[2]/div[1]/a/img', now_whd, 0, 0, 0, '', '', '', 'alt'
                            , 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="point_news"]/div[3]/div[2]/div[2]/a/dl/dd[1]/h5', now_whd, 0, 0, 0, '', '',
                            '', 'alt', 0, '', '')

    def test_12(self):
        my_tools.wintowh(cwb, 0, 1300)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[5]/div[1]/div[1]/ul/li/a', now_whd, 0, 0, 0, '', '', '',
                            'title', 0, '', '')

    def test_13(self):
        # 点击轮播图 //*[@id="point_newgame"]/div[1]/div[2]/div/ul/li/a/div/p
        my_tools.wintowh(cwb, 0, 1300)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="point_newgame"]/div[1]/div[2]/div/ul/li/a/div/p', now_whd, 0, 0, 0, '', '',
                            '', '', 0, '', '')

    def test_14(self):
        my_tools.wintowh(cwb, 0, 1300)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[5]/div[2]/div/ul/li/a', now_whd, 0, 0, 0, '', '', '',
                            'title', 0, '', '')

    def test_15(self):
        my_tools.wintowh(cwb, 0, 1900)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[6]/div[3]/div[1]/ul/li/a', now_whd, 0, 0, 0, '', '', '',
                            'title', 0, '', '')

    def test_16(self):
        my_tools.wintowh(cwb, 0, 2250)
        time.sleep(5)
        now_whd = cwb.current_window_handle
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="point_gif"]/div[1]/div/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '//*[@id="point_gif"]/div[1]/div/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="point_gif"]/div[1]/div/div[2]/div[{}]/table/tbody/tr/td[3]/a'.format(i),
                                now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_17(self):
        my_tools.wintowh(cwb, 0, 2250)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="point_gif"]/div[2]/div/div[1]/ul/li/a/img', now_whd, 0, 0, 0, '', '', '',
                            'alt', 0, '', '')

    def test_18(self):
        my_tools.wintowh(cwb, 0, 2250)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="point_gif"]/div[2]/div/div[2]/ul/li/a', now_whd, 0, 0, 0, '', '', '', 'title'
                            , 0, '', '')

    def test_19(self):
        my_tools.wintowh(cwb, 0, 2700)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[3]/div[9]/div[1]/div/div/div[1]/ul/li/a'))+1):
            if i == 1:
                my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div[9]/div[1]/div/div/div[1]/ul/li[{}]/a'.format(i))
                my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[9]/div[1]/div/div/div[2]/div[{}]/ul/li/a/img'.format(i)
                                    , now_whd, 0, 0, 0, '', '', '', 'alt', 0, '', '')
            else:
                my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div[9]/div[1]/div/div/div[1]/ul/li[{}]/a'.format(i))
                my_tools.ele_clicks(cwb,
                                    '/html/body/div[5]/div[3]/div[9]/div[1]/div/div/div[2]/div[{}]/div[4]/ul/li/a'.format(i)
                                    , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_20(self):
        my_tools.wintowh(cwb, 0, 2700)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        for i in range(1, len(
                cwb.find_elements_by_xpath('/html/body/div[5]/div[3]/div[9]/div[2]/div/div/div[1]/ul/li/a')) + 1):
            if i == 1:
                my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div[9]/div[2]/div/div/div[1]/ul/li[{}]/a'.format(i))
                my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[9]/div[2]/div/div/div[2]/div[1]/ul/li/a', now_whd
                                    , 0, 0, 0, '', '', '', '', 0, '', '')
                my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[9]/div[2]/div/div/div[2]/div[1]/div[3]/a',
                                    now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
            elif i == 2:
                my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div[9]/div[2]/div/div/div[1]/ul/li[{}]/a'.format(i))
                my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[9]/div[2]/div/div/div[2]/div[2]/div[2]/ul/li/a',
                                    now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
            else:
                my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div[9]/div[1]/div/div/div[1]/ul/li[{}]/a'.format(i))
                my_tools.ele_clicks(cwb,
                                    '/html/body/div[5]/div[3]/div[9]/div[2]/div/div/div[2]/div[{}]/div[3]/ul/li/a'.format(
                                        i)
                                    , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_21(self):
        my_tools.wintowh(cwb, 0, 3150)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        for i in range(1, 5):
            cwb.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div/ul/li[{}]/a'.format(i)).click()
            time.sleep(2)
            if i != 2:
                my_tools.jump_link(cwb, 1, 3, '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[2]/div[{}]/a' % (i + 1),
                                   'title', True, now_whd, 'app', True, False, False, '', '')
                my_tools.jump_link(cwb, 1, 10, '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[3]/a[{}]' % (i+1), '',
                                   True, now_whd, 'app', False, False, False, '', '')
                my_tools.jump_link(cwb, 1, 10, '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[1]/ul/li[{}]/a' % (i+1),
                                   'title', True, now_whd, 'app', True, False, False, '', '')
            else:
                cwb.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div/div[3]/div[2]/div[1]/a").click()
                time.sleep(3)
                BasePage(cwb).back()
                time.sleep(3)
                cwb.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div/ul/li[2]/a').click()
                time.sleep(3)
                my_tools.jump_link(cwb, 2, 3, '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[2]/div[{}]/a' % (i + 1),
                                   'title', True, now_whd, 'app', True, False, False, '', '')
                my_tools.jump_link(cwb, 1, 10, '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[3]/a[{}]' % (i + 1), '',
                                   True, now_whd, 'app', False, False, False, '', '')
                my_tools.jump_link(cwb, 1, 10,
                                   '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[1]/ul/li[{}]/a' % (i + 1),
                                   'title', True, now_whd, 'app', True, False, False, '', '')
        cwb.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/a[2]").click()
        time.sleep(3)
        for x in range(5, 9):
            cwb.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div/ul/li[{}]/a'.format(x)).click()
            time.sleep(2)
            if x != 8:
                my_tools.jump_link(cwb, 1, 3, '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[2]/div[{}]/a' % (x + 1),
                                   'title', True, now_whd, 'app', True, False, False, '', '')
            else:
                my_tools.jump_link(cwb, 1, 3, '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[2]/div[{}]/a' % (x + 1),
                                   'target', False, now_whd, 'app', True, False, False, '', '')
            my_tools.jump_link(cwb, 1, 10, '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[3]/a[{}]' % (x + 1), '',
                               True, now_whd, 'app', False, False, False, '', '')
            my_tools.jump_link(cwb, 1, 10,
                               '/html/body/div[6]/div[1]/div[2]/div/div[%d]/div[1]/ul/li[{}]/a' % (x + 1),
                               'title', True, now_whd, 'app', True, False, False, '', '')

    def test_22(self):
        my_tools.wintowh(cwb, 0, 3500)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 2, '/html/body/div[6]/div[4]/div[{}]/div[2]/div/a', 'target', False, now_whd, 'app',
                           True, False, False, '', '')

    def test_23(self):
        my_tools.wintowh(cwb, 0, 3500)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 6, '/html/body/div[6]/div[5]/div[1]/div[1]/div[1]/ul[1]/li[{}]/a', 'title', True,
                           now_whd, 'app', True, False, False, '', '')
        cwb.find_element_by_xpath("/html/body/div[6]/div[5]/div[1]/div[1]/div[2]/a").click()
        my_tools.jump_link(cwb, 1, 6, '/html/body/div[6]/div[5]/div[1]/div[1]/div[1]/ul[2]/li[{}]/a', 'title', True,
                           now_whd, 'app', True, False, False, '', '')

    def test_24(self):
        my_tools.wintowh(cwb, 0, 3500)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 10, '//*[@id="point_game"]/div[1]/div[2]/a[{}]', '', False, now_whd, 'app', False,
                           False, False, '', '')

    def test_25(self):
        my_tools.wintowh(cwb, 0, 3500)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 9, '//*[@id="point_game"]/div[2]/ul/ul/li[{}]/a', 'title', True, now_whd, 'app', True
                           , False, False, '', '')

    def test_26(self):
        my_tools.wintowh(cwb, 0, 3500)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        for i in range(1, 6):
            ele = cwb.find_element_by_xpath('//*[@id="point_game"]/div[3]/div/div/div[1]/ul/li[{}]/a'.format(i))
            ActionChains(cwb).move_to_element(ele).perform()
            if i == 1:
                my_tools.jump_link(cwb, 1, 6, '/html/body/div[6]/div[5]/div[3]/div/div/div[2]/div[1]/ul/li[{}]/a',
                                   'title', True, now_whd, 'app', True, False, False, '', '')
                my_tools.jump_link(cwb, 1, 2, '//*[@id="point_game"]/div[3]/div/div/div[2]/div[{}]/div[2]/a', '', False,
                                   now_whd, 'app', False, False, False, '', '')
            else:
                for v in range(1, 6):
                    my_tools.jump_link(cwb, 1, 3,
                                       '//*[@id="point_game"]/div[3]/div/div/div[2]/div[%d]/div[3]/ul[{}]/li[%d]/a' % (i, v),
                                       'title', True, now_whd, 'app', True, False, False, '', '')
                my_tools.jump_link(cwb, 4, 5, '//*[@id="point_game"]/div[3]/div/div/div[2]/div[%d]/div[{}]/a' % (i), '',
                                   False,
                                   now_whd, 'app', False, False, False, '', '')

    def test_27(self):
        my_tools.wintowh(cwb, 0, 4000)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 6, '//*[@id="point_union"]/div[6]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[{}]/a',
                           'title', True, now_whd, 'app', True, False, False, '', '')
        cwb.find_element_by_xpath('//*[@id="point_union"]/div[6]/div[1]/div[1]/div[1]/div[2]/a').click()
        time.sleep(3)
        my_tools.jump_link(cwb, 1, 6, '//*[@id="point_union"]/div[6]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[{}]/a',
                           'title', True, now_whd, 'app', True, False, False, '', '')

    def test_28(self):
        my_tools.wintowh(cwb, 0, 3500)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 10, '///*[@id="point_union"]/div[6]/div[1]/div[1]/div[2]/a[{}]', '', False, now_whd, 'app', False,
                           False, False, '', '')

    def test_29(self):
        my_tools.wintowh(cwb, 0, 3900)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 5, '//*[@id="point_union"]/div[6]/div[2]/div/div[2]/div/ul[1]/li[{}]/a', 'title',
                           True, now_whd, 'app', True, False, False, '', '')
        my_tools.jump_link(cwb, 1, 6, '//*[@id="point_union"]/div[6]/div[2]/div/div[2]/div/ul[2]/li[{}]/a/span[4]', 'target',
                           False, now_whd, 'app', True, False, False, '', '')

    def test_30(self):
        my_tools.wintowh(cwb, 0, 4200)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 4, '//*[@id="point_pic"]/div[1]/a[{}]', 'title', False, now_whd, 'app', True, False,
                           False, '', '')
        my_tools.jump_link(cwb, 2, 3, '//*[@id="point_pic"]/div[{}]/a', 'title', False, now_whd, 'app', True, False,
                           False, '', '')
        my_tools.jump_link(cwb, 1, 3, '//*[@id="point_pic"]/div[3]/a[{}]', 'title', False, now_whd, 'app', True, False,
                           False, '', '')

    def test_31(self):
        my_tools.wintowh(cwb, 0, 4600)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        for i in range(1, 9):
            ele = cwb.find_element_by_xpath('//*[@id="point_union"]/div[8]/div[1]/div[2]/ul/li/div/div[1]/ul/li[{}]'.
                                            format(i))
            ActionChains(cwb).move_to_element(ele).perform()
            if i == 1:
                my_tools.jump_link(cwb, 1, 9,
                                   '//*[@id="point_union"]/div[8]/div[1]/div[2]/ul/li/div/div[2]/ul/li[1]/div/ul/li[{}]/div[2]/a', '', False, now_whd, 'app', False, False, False, '', '')
            else:
                my_tools.jump_link(cwb, 1, 21, '//*[@id="point_union"]/div[8]/div[1]/div[2]/ul/li/div/div[2]/ul/li[%d]/div/ul/li[{}]/a' % (i), 'title', True, now_whd, 'app', True, False, False, '', '')

    def test_32(self):
        my_tools.wintowh(cwb, 0, 5000)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        for i in range(1, 5):
            my_tools.jump_link(cwb, 1, 11, '//*[@id="point_rank"]/div[%d]/div/dl[{}]/dd/h5/a' % (i), '', True, now_whd,
                               'app', False, False, False, '', '')

    def test_33(self):
        my_tools.wintowh(cwb, 0, 5500)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        for i in range(1, 9):
            cwb.find_element_by_xpath('//*[@id="point_union"]/div[9]/div/div[2]/div[2]').click()
            time.sleep(3)
            if i != 8:
                my_tools.jump_link(cwb, 16+(i-1)*5, 16+i*5, '//*[@id="links_box"]/a[{}]', '', False, now_whd, 'app',
                                   False, False, False, '', '')
            else:
                my_tools.jump_link(cwb, 51, 52, '//*[@id="links_box"]/a[{}]', '', False, now_whd, "app", False, False,
                                   False, '', '')

    def test_34(self):
        my_tools.wintowh(cwb, 0, 5500)
        time.sleep(3)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 8, '/html/body/div[8]/div/p[1]/a[{}]', '', False, now_whd, '', False, False, False,
                           '', '')
        my_tools.jump_link(cwb, 1, 4, '/html/body/div[8]/div/p[2]/a[{}]', '', False, now_whd, 'app', False, False, False
                           , '', '')
        my_tools.jump_link(cwb, 1, 7, '/html/body/div[8]/div/div[1]/a[{}]', '', False, now_whd, 'app', False, False,
                           False, '', '')

    def test_35(self):
        my_tools.wintowh(cwb, 0, 5500)
        time.sleep(3)
        for i in range(1, 9):
            try:
                cwb.find_element_by_xpath('/html/body/div[7]/ul/li[{}]/a'.format(i)).click()
                print('页面右侧快捷栏{}正常导航'.format(i))
                time.sleep(2)
            except:
                print('页面右侧快捷栏{}不能正常导航'.format(i))

    def test_36(self):
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 10, 11, '/html/body/div[{}]/div/a', 'target', False, now_whd, '', True, False, False, ''
                           , '')
        my_tools.jump_link(cwb, 1, 3, '/html/body/div[10]/div/p[{}]/a', 'target', False, now_whd, '', True, False, False
                           , '', '')

    def test_37(self):
        # 登录
        cwb.find_element_by_xpath('//*[@id="pprt_login"]').click()
        time.sleep(3)
        my_tools.mouse_do(960, 440)
        pyautogui.typewrite("18365049450", interval=0.3)
        pyautogui.press('tab', interval=0.5)
        pyautogui.typewrite("wxwx1996918", interval=0.3)
        pyautogui.press('enter', interval=0.5)
        time.sleep(3)
        if "18183玩家" in cwb.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/a').text:
            print("登录成功")


if __name__ == "__main__":
    unittest.main()