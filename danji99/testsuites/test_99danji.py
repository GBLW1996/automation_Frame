import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from danji99.common.warning import message
# from danji99.common.log import Logger
from danji99.common.cappic import Cappic
from danji99.pages.basepage import BasePage
import os
from selenium import webdriver
from danji99.common.tools import PageTool
from selenium.webdriver import ActionChains
import requests
options = webdriver.ChromeOptions()
path = os.path.abspath('..') + '\\downloads\\'
pre_fs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
options.add_experimental_option('prefs', pre_fs)
cwb = webdriver.Chrome(chrome_options=options)
# my_logger = Logger(logger='2').getlog()
my_tools = PageTool()


class WywNet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        BasePage(cwb).start_browser()

    @classmethod
    def tearDownClass(cls):
        # BasePage(cwb).quit_browser()
        pass

    def test_01(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[1]/div/ul/li/strong/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[1]/div/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.test_input(cwb, ['超级玛丽', 'cf', '冒险岛'], '//*[@id="q"]', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="tab-one"]/div[2]/div[1]/div[1]/ul/li/a/img', now_whd, 1, 1, 0,
                            '/html/body//a[text()="立即下载"]', '', 'pc', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="tab-one"]/div[2]/div[1]/div[2]/dl/dd/ul/li/a', now_whd, 1, 1, 0,
                            '/html/body/section[2]/article/section[1]/div/article/p/a[1]', '', 'pc', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="pos19_1"]/li/a/span', now_whd, 1, 1, 0, '/html/body//span[text()="下载到电脑"]',
                            '', 'pc', '', 0, '', '')
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="tab-one"]/div[1]/ul/li[2]'))
        time.sleep(1)
        my_tools.ele_clicks(cwb, '//*[@id="tab-one"]/div[2]/div[2]/div[1]/ul/li/a/img', now_whd, 1, 1, 0, '',
                            '/html/body//a[text()="安卓版下载"]', 'app', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="tab-one"]/div[2]/div[2]/div[2]/dl/dd/ul/li/a', now_whd, 1, 1, 0, '',
                            '/html/body//span[text()="下载到电脑"]', 'app', '', 0, '', '')

    def test_03(self):
        my_tools.wintowh(cwb, 0, 650)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="banner"]/div[1]/ul/li/a', now_whd, 1, 0, 0,
                            '/html/body//span[text()="下载到电脑"]', '', 'pc', 'href', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/div[1]/div[2]/ul/li/a/span', now_whd, 0, 1, 0, '', '', '', ''
                            , 0, '', '')
        len_list = cwb.find_elements_by_xpath('//*[@id="tab-two"]/div[1]/ul/li')
        for i in range(1, len(len_list)+1):
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="tab-two"]/div[1]/ul/li[{}]'.format(i)))
            time.sleep(1)
            my_tools.ele_clicks(cwb, '//*[@id="tab-two"]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 1, 0, '', '', ''
                                , '', 0, '', '')

    def test_04(self):
        my_tools.wintowh(cwb, 0, 1250)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[7]/div[1]/span/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="tab-three"]/div[2]/div[1]/ul/li/a/span', now_whd, 1, 1, 0,
                            '/html/body//span[text()="下载到电脑"]', '', 'pc', '', 0, '', '')
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="tab-three"]/div[1]/ul/li[2]'))
        time.sleep(1)
        my_tools.ele_clicks(cwb, '//*[@id="tab-three"]/div[2]/div[2]/ul/li/a/span', now_whd, 1, 1, 0,
                            '/html/body//span[text()="下载到电脑"]', '', 'pc', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="tab-four"]/div[2]/div[1]/ul/li/a', now_whd, 1, 0, 0,
                            '/html/body//span[text()="下载到电脑"]', '', 'pc', '', 0, '', '')
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="tab-four"]/div[1]/ul/li[2]'))
        time.sleep(1)
        my_tools.ele_clicks(cwb, '//*[@id="tab-four"]/div[2]/div[2]/ul/li/a', now_whd, 1, 0, 0,
                            '/html/body//span[text()="下载到电脑"]', '', 'pc', '', 0, '', '')

    def test_05(self):
        my_tools.wintowh(cwb, 0, 1750)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="tab-five"]/div[2]/div[1]/ul/li/a/span', now_whd, 1, 1, 0,
                            '/html/body//span[text()="下载到电脑"]', '', 'pc', '', 0, '', '')
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="tab-five"]/div[1]/ul/li[2]'))
        time.sleep(1)
        my_tools.ele_clicks(cwb, '//*[@id="tab-five"]/div[2]/div[2]/ul/li/a/span', now_whd, 1, 1, 0,
                            '/html/body//span[text()="下载到电脑"]', '', 'pc', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="tab-six"]/div[2]/div[1]/ul/li/a', now_whd, 1, 0, 0,
                            '/html/body//span[text()="下载到电脑"]', '', 'pc', '', 0, '', '')
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="tab-six"]/div[1]/ul/li[2]'))
        time.sleep(1)
        my_tools.ele_clicks(cwb, '//*[@id="tab-six"]/div[2]/div[2]/ul/li/a', now_whd, 1, 0, 0,
                            '/html/body//span[text()="下载到电脑"]', '', 'pc', '', 0, '', '')

    def test_06(self):
        my_tools.wintowh(cwb, 0, 2500)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[9]/div[1]/span/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="img-one"]/div[1]/div/div/ul[2]/li/a/img', now_whd, 1, 1, 0,
                            '/html/body//a[text()="游戏大小:"]', '', 'pc', 'alt', 0, '', '')
        my_tools.move_in(cwb, '//*[@id="img-one"]/div[2]/ul/li[2]/a')
        time.sleep(3)
        my_tools.ele_clicks(cwb, '//*[@id="img-one"]/div[1]/div/div/ul[3]/li/a/img', now_whd, 1, 1, 0,
                            '/html/body//a[text()="游戏大小:"]', '', 'pc', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="img-two"]/div[1]/div/div/ul[2]/li/a/img', now_whd, 1, 1, 0,
                            '/html/body//a[text()="游戏大小:"]', '', 'pc', 'alt', 0, '', '')
        my_tools.move_in(cwb, '//*[@id="img-two"]/div[2]/ul/li[2]/a')
        time.sleep(3)
        my_tools.ele_clicks(cwb, '//*[@id="img-two"]/div[1]/div/div/ul[3]/li/a/img', now_whd, 1, 1, 0,
                            '/html/body//a[text()="游戏大小:"]', '', 'pc', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="img-three"]/div[1]/div/div/ul[2]/li/a/img', now_whd, 1, 1, 0,
                            '/html/body//a[text()="游戏大小:"]', '', 'pc', 'alt', 0, '', '')
        my_tools.move_in(cwb, '//*[@id="img-three"]/div[2]/ul/li[2]/a')
        time.sleep(3)
        my_tools.ele_clicks(cwb, '//*[@id="img-three"]/div[1]/div/div/ul[3]/li/a/img', now_whd, 1, 1, 0,
                            '/html/body//a[text()="游戏大小:"]', '', 'pc', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="tab-seven"]/div[2]/div[1]/ul/li/a', now_whd, 1, 0, 0,
                            '/html/body//a[text()="游戏大小:"]', '', 'pc', '', 0, '', '')
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="tab-seven"]/div[1]/ul/li[2]'))
        time.sleep(1)
        my_tools.ele_clicks(cwb, '//*[@id="tab-seven"]/div[2]/div[2]/ul/li/a', now_whd, 1, 0, 0,
                            '/html/body//a[text()="游戏大小:"]', '', 'pc', '', 0, '', '')

    def test_07(self):
        my_tools.wintowh(cwb, 0, 3300)
        now_whd = cwb.current_window_handle
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="tab-eight"]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '//*[@id="tab-eight"]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="tab-eight"]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 1, 1, 0,
                                '/html/body//a[@title="下载地址"]', '', 'pc', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[10]/div[2]/div[1]/div[2]/ul/li/a/span', now_whd, 1, 1, 0,
                            '/html/body//a[@title="下载地址"]', '', 'pc', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="tab-nine"]/div[2]/div[1]/ul/li/a', now_whd, 1, 1, 0,
                            '/html/body//a[@title="下载地址"]', '', 'pc', '', 0, '', '')
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="tab-nine"]/div[1]/ul/li[2]'))
        time.sleep(2)
        my_tools.ele_clicks(cwb, '//*[@id="tab-nine"]/div[2]/div[2]/ul/li/a', now_whd, 1, 1, 0,
                            '/html/body//a[@title="下载地址"]', '', 'pc', '', 0, '', '')

    def test_08(self):
        my_tools.wintowh(cwb, 0, 3700)
        now_whd = cwb.current_window_handle
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="tab-ten"]/div[1]/div/ul/li/a'))+1):
            my_tools.move_in(cwb, '//*[@id="tab-ten"]/div[1]/div/ul/li[{}]/a'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="tab-ten"]/div[2]/div[{}]/ul/li/a/img'.format(i), now_whd, 0, 1, 0, '', ''
                                , '', 'alt', 0, '', '')

    def test_09(self):
        my_tools.wintowh(cwb, 0, 3900)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[12]/div[2]/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')


if __name__ == "__main__":
    unittest.main()