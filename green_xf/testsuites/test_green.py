import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from green_xf.common.warning import message
# from green_xf.common.log import Logger
from green_xf.common.cappic import Cappic
from green_xf.pages.basepage import BasePage
import os
from selenium import webdriver
from green_xf.common.tools import PageTool
from selenium.webdriver import ActionChains
import requests
options = webdriver.ChromeOptions()
path = os.path.abspath('..') + '\\downloads\\'
pre_fs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
options.add_experimental_option('prefs', pre_fs)
options.add_argument('--headless')
cwb = webdriver.Chrome(chrome_options=options)
# my_logger = Logger(logger='2').getlog()
my_tools = PageTool()


class WywNet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        BasePage(cwb).start_browser()

    @classmethod
    def tearDownClass(cls):
        BasePage(cwb).quit_browser()

    def test_01(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/header/div[1]/div/div[2]/a', now_whd, 0, 0, 0, '', '', '', '', 1, '', '')
        my_tools.test_input(cwb, ['QQ', '超级玛丽', '微信', '英雄联盟'], '//*[@id="q"]', now_whd)

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/section[1]/div/ul/li/a/div/img', now_whd, 1, 1, 1,
                            '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/section[1]/ul/li[1]/a', now_whd, 1, 1, 1, '//*[@id="local-download"]/div',
                            '//*[@id="androidPopup"]/p', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/section[1]/ul/li[2]/a', now_whd, 1, 1, 1, '//*[@id="local-download"]/div',
                            '//*[@id="androidPopup"]/p', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/section[1]/ul/li[3]/a', now_whd, 1, 1, 1, '//*[@id="local-download"]/div',
                            '//*[@id="androidPopup"]/p', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/section[2]/ul/li/a/div/div/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0, ''
                            , '')

    def test_03(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 750)
        my_tools.move_in(cwb, '//*[@id="home-slide"]/div[4]/i[1]')
        my_tools.ele_clicks(cwb, '//*[@id="home-slide"]/div[1]/a[1]/img', now_whd, 1, 1, 1,
                            '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'alt', 1, '', '')
        my_tools.move_in(cwb, '//*[@id="home-slide"]/div[4]/i[2]')
        my_tools.ele_clicks(cwb, '//*[@id="home-slide"]/div[1]/a[2]/img', now_whd, 1, 1, 1,
                            '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'alt', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/section[3]/div[1]/div[2]/ul/li/a', now_whd, 1, 1, 1,
                            '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'title', 0, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/section[3]/div[2]/ul/li/i'))+1):
            my_tools.move_in(cwb, '/html/body/section[3]/div[2]/ul/li[{}]/i'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/section[3]/div[2]/div/div[{}]/ul/li/span[2]/a'.format(i), now_whd, 0, 1
                                , 0, '', '', '', '', 1, '/html/body/section[3]/div[2]/ul/li[{}]/i'.format(i), '')
            my_tools.ele_clicks(cwb, '/html/body/section[3]/div[2]/div/div[{}]/ul/li/a'.format(i), now_whd, 0, 1, 0, '',
                                '', '', '', 1, '/html/body/section[3]/div[2]/ul/li[{}]/i'.format(i), '')
        my_tools.ele_clicks(cwb, '/html/body/section[3]/div[3]/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', ''
                            , 'title', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/section[3]/div[3]/div[2]/ul/li/a/p', now_whd, 0, 1, 0, '', '', '', '', 1,
                            '', '')

    def test_04(self):
        # 电脑软件
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1525)
        my_tools.ele_clicks(cwb, '/html/body/section[4]/div[2]/div/ul/li/a', now_whd, 1, 1, 1,
                            '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'title', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/section[4]/div[3]/div[2]/ul[1]/li/a', now_whd, 1, 1, 1,
                            '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/section[4]/div[3]/div[1]/ul/li[2]')
        my_tools.ele_clicks(cwb, '/html/body/section[4]/div[3]/div[2]/ul[2]/li/a', now_whd, 1, 1, 1,
                            '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'title', 0, '', '')

    def test_05(self):
        # 安卓应用
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2250)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/section[5]/div[2]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/section[5]/div[2]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/section[5]/div[2]/div/ul[{}]/li/a'.format(i), now_whd, 0, 1, 0, '', '',
                                '', '', 1, '/html/body/section[5]/div[2]/ul/li[{}]'.format(i), '')
        for y in range(1, len(cwb.find_elements_by_xpath('/html/body/section[5]/div[3]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/section[5]/div[3]/div[1]/ul/li[{}]'.format(y))
            my_tools.ele_clicks(cwb, '/html/body/section[5]/div[3]/div[2]/ul[{}]/li/a'.format(y), now_whd, 0, 1, 0, '',
                                '', '', 'title', 0, '', '')

    def test_06(self):
        # MAC应用
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2850)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/section[6]/div[2]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/section[6]/div[2]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/section[6]/div[2]/div/ul[{}]/li/a'.format(i), now_whd, 0, 1, 0, '', '',
                                '', '', 1, '/html/body/section[6]/div[2]/ul/li[{}]'.format(i), '')
        for y in range(1, len(cwb.find_elements_by_xpath('/html/body/section[6]/div[3]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/section[6]/div[3]/div[1]/ul/li[{}]'.format(y))
            my_tools.ele_clicks(cwb, '/html/body/section[6]/div[3]/div[2]/ul[{}]/li/a'.format(y), now_whd, 0, 1, 0, '',
                                '', '', 'title', 0, '', '')

    def test_07(self):
        # 分类更新
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3450)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/section[7]/div[2]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/section[7]/div[2]/ul/li[{}]'.format(i))
            for y in range(1, len(cwb.find_elements_by_xpath('/html/body/section[7]/div[2]/div/div[1]/ul/li'))+1):
                my_tools.move_in(cwb, '/html/body/section[7]/div[2]/div/div[1]/ul/li[{}]'.format(y))
                my_tools.ele_clicks(cwb, '/html/body/section[7]/div[2]/div/div[{}]/div/ul[{}]/li/a'.format(i, y),
                                    now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        for x in range(1, len(cwb.find_elements_by_xpath('/html/body/section[7]/div[3]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/section[7]/div[3]/div[1]/ul/li[{}]'.format(x))
            my_tools.ele_clicks(cwb, '/html/body/section[7]/div[3]/div[2]/ul[{}]/li/a'.format(x), now_whd, 0, 1, 0, '',
                                '', '', 'title', 0, '', '')

    def test_08(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3950)
        my_tools.ele_clicks(cwb, '/html/body/section[8]/div[2]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_09(self):
        # 电脑软件
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 0)
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/header/div[3]/nav/ul/li[2]/a'))
            my_tools.my_logger.info('进入”电脑软件“模块')
            time.sleep(1)
        except:
            my_tools.my_logger.error('进入”电脑软件“模块异常')
            # message('进入”电脑软件“模块异常')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/section/div[1]/a'))+1):
            my_tools.ele_clicks(cwb, '/html/body/section[{}]/div[2]/ul[1]/li/a'.format(i), now_whd, 0, 1, 0, '', '', '', '', 1, '',
                                '')
            my_tools.ele_clicks(cwb, '/html/body/section[{}]/div[2]/ul[2]/li/a/div/img'.format(i), now_whd, 1, 1, 1,
                                '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'alt', 1, '', '')

    def test_10(self):
        # 安卓下载
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/header/div[3]/nav/ul/li[3]/a'))
            my_tools.my_logger.info('进入”安卓下载“模块')
            time.sleep(1)
        except:
            my_tools.my_logger.error('进入”安卓下载“模块异常')
            # message('进入”电脑软件“模块异常')
        BasePage(cwb).back()

    def test_11(self):
        # MAC下载
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/header/div[3]/nav/ul/li[4]/a'))
            my_tools.my_logger.info('进入”MAC下载“模块')
            time.sleep(1)
        except:
            my_tools.my_logger.error('进入”MAC下载“模块异常')
            # message('进入”电脑软件“模块异常')
        BasePage(cwb).back()

    def test_12(self):
        # 文章教程
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/header/div[3]/nav/ul/li[5]/a'))
            my_tools.my_logger.info('进入”文章教程“模块')
            time.sleep(1)
        except:
            my_tools.my_logger.error('进入”文章教程“模块异常')
            # message('进入”电脑软件“模块异常')
        my_tools.ele_clicks(cwb, '/html/body/section/div[2]/div[3]/div/div[2]/ul[1]/li/a', now_whd, 1, 1, 1,
                            '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/section/div[2]/div[3]/div/div[1]/ul/li[2]')
        my_tools.ele_clicks(cwb, '/html/body/section/div[2]/div[3]/div/div[2]/ul[2]/li/a', now_whd, 1, 1, 1,
                            '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'title', 0, '', '')

    def test_13(self):
        # 专题合集
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/header/div[3]/nav/ul/li[6]/a'))
            my_tools.my_logger.info('进入”专题合集“模块')
            time.sleep(1)
        except:
            my_tools.my_logger.error('进入”专题合集“模块异常')
            # message('进入”电脑软件“模块异常')
        my_tools.ele_clicks(cwb, '/html/body/section/div/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')

    def test_14(self):
        # 排行榜
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/header/div[3]/nav/ul/li[7]/a'))
            my_tools.my_logger.info('进入”排行榜“模块')
            time.sleep(1)
        except:
            my_tools.my_logger.error('进入”排行榜“模块异常')
            # message('进入”电脑软件“模块异常')
        my_tools.ele_clicks(cwb, '/html/body/section[1]/nav/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/section[2]/div/div'))+1):
            for x in range(1, len(cwb.find_elements_by_xpath('/html/body/section[2]/div/div[{}]/div[1]/ul/li'.format(i)))+1):
                my_tools.move_in(cwb, '/html/body/section[2]/div/div[{}]/div[1]/ul/li[{}]'.format(i, x))
                my_tools.ele_clicks(cwb, '/html/body/section[2]/div/div[{}]/div[2]/ul[{}]/li/a'.format(i, x), now_whd, 1
                                    , 1, 1, '//*[@id="local-download"]/div', '//*[@id="androidPopup"]/p', '', 'title', 0
                                    , '', '')


if __name__ == "__main__":
    unittest.main()