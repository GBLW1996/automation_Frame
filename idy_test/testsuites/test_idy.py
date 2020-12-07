import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from idy_test.common.warning import message
# from idy_test.common.log import Logger
from idy_test.common.cappic import Cappic
from idy_test.pages.basepage import BasePage
import os
from selenium import webdriver
from idy_test.common.tools import PageTool
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
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div[1]/div[2]/div/div/ul/li/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', 'href', 1,
                            '/html/body/div[2]/div[1]/div[2]/div/input', '')
        my_tools.my_logger.info('首页搜索框检查完成')

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/div/div/dl/dd/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')

    def test_03(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="index-tab-content"]/div[2]/div[1]/div[1]/div[1]/ul/li/div[2]/a', now_whd, 1,
                            1, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

        my_tools.move_in(cwb, '//*[@id="index-tab-content"]/div[1]/a[2]')
        my_tools.ele_clicks(cwb, '//*[@id="index-tab-content"]/div[2]/div[2]/div[1]/div[1]/ul/li/div[2]/a', now_whd, 1,
                            1, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '//*[@id="index-tab-content"]/div[1]/a[2]', '')

        my_tools.move_in(cwb, '//*[@id="index-tab-content"]/div[1]/a[3]')
        my_tools.ele_clicks(cwb, '//*[@id="index-tab-content"]/div[2]/div[3]/div[1]/div[1]/ul/li/div[2]/a', now_whd, 1,
                            1, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '//*[@id="index-tab-content"]/div[1]/a[3]', '')

        my_tools.move_in(cwb, '//*[@id="index-tab-content"]/div[1]/a[4]')
        my_tools.ele_clicks(cwb, '//*[@id="index-tab-content"]/div[2]/div[4]/div[1]/div[1]/ul/li/div[2]/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '//*[@id="index-tab-content"]/div[1]/a[4]', '')

        my_tools.move_in(cwb, '//*[@id="index-tab-content"]/div[1]/a[5]')
        my_tools.ele_clicks(cwb, '//*[@id="index-tab-content"]/div[2]/div[5]/div[1]/div/div/div/div[2]/ul/li/a', now_whd
                            , 0, 0, 0, '', '', '', 'href', 1, '', '')

        my_tools.move_in(cwb, '//*[@id="index-tab-content"]/div[1]/a[5]')
        my_tools.ele_clicks(cwb, '//*[@id="index-tab-content"]/div[2]/div[5]/div[@class="side banner"]/div/ul/li/a',
                            now_whd, 0, 0, 0, '', '', '', 'href', 1, '', '')

    def test_04(self):
        # 热门电影
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 750)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[1]/ul[1]/li/div[1]/a/img', now_whd, 1, 1,
                            0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', 'alt', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[1]/ul[2]/li/div/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_05(self):
        # 热门电视剧
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1150)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[1]/ul[1]/li/div[1]/a/img', now_whd, 1, 1,
                            0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', 'alt', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[1]/ul[2]/li/div/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_06(self):
        # 热门综艺
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1600)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[1]/ul/li/div[1]/a/img', now_whd, 1, 1,
                            0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', 'alt', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_07(self):
        # 热门动漫
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2100)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[1]/ul/li/div[1]/a/img', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', 'alt', 1, ''
                            , '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_08(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2500)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[6]/div/div[2]/div/a[position()<5]', now_whd, 0, 0, 0, '', '', ''
                            , '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[6]/div/div[2]/div/a[position()>4]', now_whd, 0, 0, 0, '', '',
                            '', '', 0, '', '')

    def test_09(self):
        # 电影
        js = "window.scrollTo(0,0)"
        cwb.execute_script(js)
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        BasePage(cwb).wait(10)
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/div/dl/dd/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')

    def test_10(self):
        # 热映电影
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[2]/div/ul[1]/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_11(self):
        # 热门电影
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 550)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[1]/ul[1]/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[1]/ul[2]/li/div/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_12(self):
        # 热搜电影
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1050)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_13(self):
        # 欧美
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1550)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_14(self):
        # 华语
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2050)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_15(self):
        # 电视剧
        js = "window.scrollTo(0,0)"
        cwb.execute_script(js)
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[3]/a')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        BasePage(cwb).wait(10)
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/div/dl/dd/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')

    def test_16(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[2]/div/div[1]/ul[1]/li/div[1]/a/img', now_whd, 1, 1,
                            0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', 'alt', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[2]/div/div[1]/ul[2]/li/div/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_17(self):
        # 热搜电视剧
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 750)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_18(self):
        # 美剧
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1150)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_19(self):
        # 国产
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1700)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_20(self):
        # 韩剧
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2200)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1, 0, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')

    def test_21(self):
        # 综艺
        js = "window.scrollTo(0,0)"
        cwb.execute_script(js)
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[4]/a')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        BasePage(cwb).wait(10)
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/div/dl/dd/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')

    def test_22(self):
        # 热搜电综艺
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_23(self):
        # 选秀
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 750)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_24(self):
        # 情感
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1150)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_25(self):
        # 访谈
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1550)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_26(self):
        # 国外
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2000)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_27(self):
        # 动漫
        js = "window.scrollTo(0,0)"
        cwb.execute_script(js)
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[5]/a')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        BasePage(cwb).wait(10)
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/div/dl/dd/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')

    def test_28(self):
        # 热搜动漫
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_29(self):
        # 热门动漫
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 750)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[1]/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[1]/ul[1]/li/div[2]/a', now_whd, 1, 1, 0,
                            '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[1]/ul[2]/li/div/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_30(self):
        # 日本
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1150)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_31(self):
        # 国产
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1550)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[4]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_32(self):
        # 搞笑
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2100)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[5]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_33(self):
        # 冒险
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2700)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[6]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[6]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_34(self):
        # 益智
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3200)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[7]/div/div[2]/div/div[1]/ul/li/div[2]/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[7]/div/div[2]/div/div[2]/div/ul/li/p/a', now_whd, 1,
                            0, 0, '//*[@id="introduce-content"]/div[1]/div[1]/div/div[1]/div[2]/a/img', '', 'pc', '', 1,
                            '', '')

    def test_35(self):
        # 好片推荐
        js = "window.scrollTo(0,0)"
        cwb.execute_script(js)
        try:
            ele = cwb.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[6]/a')
            my_tools.static_click(cwb, ele)
            my_tools.my_logger.info('idy好片推荐点击正常')
        except:
            my_tools.my_logger.error('idy好片推荐点击异常')
            message('idy好片推荐点击异常')
        time.sleep(2)
        BasePage(cwb).wait(10)


if __name__ == "__main__":
    unittest.main()