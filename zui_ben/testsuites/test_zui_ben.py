import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from zui_ben.common.warning import message
# from zui_ben.common.log import Logger
from zui_ben.common.cappic import Cappic
from zui_ben.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from selenium import webdriver
from zui_ben.common.tools import PageTool
from selenium.webdriver import ActionChains
import requests
options = webdriver.ChromeOptions()
path = os.path.abspath('..') + '\\downloads\\'
pre_fs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
options.add_experimental_option('prefs', pre_fs)
# options.add_argument('--headless')
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
        # my_tools.move_in(cwb, '/html/body/div[1]/div/ul[2]/li/div[1]')
        # time.sleep(0.5)
        # my_tools.ele_clicks(cwb, '/html/body/div[1]/div/ul[2]/li/div[2]/div/dl/dd/a', now_whd, mv_xp=
        #                     '/html/body/div[1]/div/ul[2]/li/div[1]')
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div[2]/ul/li/div/p/a', now_whd, is_back=1)
        my_tools.move_in(cwb, '//*[@id="a1"]/a/span')
        time.sleep(0.5)
        my_tools.ele_clicks(cwb, '//*[@id="a1a"]/div[1]/ul/li/a/span[2]', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="a1a"]/div[2]/li/a', now_whd, is_judge_link=1)
        my_tools.move_in(cwb, '//*[@id="a2"]/a/span')
        time.sleep(0.5)
        my_tools.ele_clicks(cwb, '//*[@id="a2a"]/div[1]/ul/li/a/span[2]', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="a2a"]/div[2]/li/a', now_whd, is_judge_link=1)
        my_tools.move_in(cwb, '//*[@id="a3"]/a/span')
        time.sleep(0.5)
        my_tools.ele_clicks(cwb, '//*[@id="a3a"]/div[1]/ul/li/a/span[2]', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="a3a"]/div[2]/li/a', now_whd, is_judge_link=1)

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 450)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="slide"]/div[1]/a'))+1):
            my_tools.move_in(cwb, '//*[@id="slide"]/div[1]/a[{}]'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="slide"]/li[{}]/a'.format(i), now_whd, attr='title', is_judge_link=1, is_back=1)
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[1]/div[2]/dl/dd/p/span/a', now_whd, is_judge_link=1, is_back=1)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[3]/div[2]/div[2]/div/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[2]/div/div[{}]/div/a'.format(i+1), now_whd,
                                is_judge_link=1, is_back=1, mv_xp='/html/body/div[3]/div[2]/div[2]/div/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[2]/div/div[{}]/ul/li/a'.format(i + 1), now_whd,
                                is_back=1, mv_xp='/html/body/div[3]/div[2]/div[2]/div/div[1]/ul/li[{}]'.format(i))

    def test_03(self):
        # 安卓平台
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 950)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="adroid-plat"]/div[1]/ul/li/a'))+1):
            my_tools.move_in(cwb, '//*[@id="adroid-plat"]/div[1]/ul/li[{}]/a'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="adroid-plat"]/div[2]/div/div[{}]/div[1]/ul/li/a'.format(i), now_whd,
                                is_back=1, mv_xp='//*[@id="adroid-plat"]/div[1]/ul/li[{}]/a'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="adroid-plat"]/div[2]/div/div[{}]/div[2]/ul/li/a/span'.format(i), now_whd)
        my_tools.wintowh(cwb, 0, 1400)
        # 安卓专题
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[3]/div[3]/p/a/span', now_whd, is_judge_link=1, is_back=1)

    def test_04(self):
        # 苹果平台
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1700)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="ios-plat"]/div[1]/ul/li[position()<4]/a')) + 1):
            my_tools.move_in(cwb, '//*[@id="ios-plat"]/div[1]/ul/li[{}]/a'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="ios-plat"]/div[2]/div/div[{}]/div[1]/ul/li/a'.format(i), now_whd,
                                is_back=1, mv_xp='//*[@id="ios-plat"]/div[1]/ul/li[{}]/a'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="ios-plat"]/div[2]/div/div[{}]/div[2]/ul/li/a/span'.format(i), now_whd)
        my_tools.move_in(cwb, '//*[@id="ios-plat"]/div[1]/ul/li[5]/a')
        my_tools.ele_clicks(cwb, '//*[@id="ios-plat"]/div[2]/div/div[5]/div[1]/ul/li/a', now_whd,
                            is_back=1, mv_xp='//*[@id="ios-plat"]/div[1]/ul/li[5]/a')
        my_tools.ele_clicks(cwb, '//*[@id="ios-plat"]/div[2]/div/div[5]/div[2]/ul/li/a/span', now_whd)
        my_tools.wintowh(cwb, 0, 2200)
        # 苹果专题
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[4]/div[3]/p/a/span', now_whd, is_judge_link=1, is_back=1)

    def test_05(self):
        # 手游攻略
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2800)
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/ul[1]/li/p/a', now_whd, is_judge_link=1, is_back=1)
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/ul/li/div[1]/a', now_whd, is_judge_link=1)
        # 友情链接
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[6]/a', now_whd)

    def test_06(self):
        now_whd = cwb.current_window_handle  # 游戏模块
        my_tools.switch_frame(cwb, '/html/body/div[2]/div[2]/ul/li[2]/a', now_whd, '游戏')
        my_tools.random_check(cwb, '/html/body/div[3]/div[3]/div[2]/ul/li/h3/a', now_whd, is_judge_link=1, is_back=1)
        my_tools.random_check(cwb, '/html/body/div[3]/div[4]/div[1]/ul/li/a[2]', now_whd, is_judge_link=1, is_back=1)

    def test_07(self):
        now_whd = cwb.current_window_handle  # 应用模块
        my_tools.switch_frame(cwb, '/html/body/div[2]/div[2]/ul/li[3]/a', now_whd, '应用')
        my_tools.random_check(cwb, '/html/body/div[3]/div[3]/div[2]/ul/li/h3/a', now_whd, is_judge_link=1, is_back=1)
        my_tools.random_check(cwb, '/html/body/div[3]/div[4]/div[1]/ul/li/a[2]', now_whd, is_judge_link=1, is_back=1)

    def test_08(self):
        now_whd = cwb.current_window_handle  # 资讯模块
        my_tools.switch_frame(cwb, '/html/body/div[2]/div[2]/ul/li[4]/a', now_whd, '资讯')
        my_tools.random_check(cwb, '/html/body/div[3]/div[3]/div[2]/ul/li/h3/a', now_whd, is_judge_link=1, is_back=1)
        my_tools.random_check(cwb, '/html/body/div[3]/div[4]/div[1]/ul/li/a[2]', now_whd, is_judge_link=1, is_back=1)

    def test_09(self):
        now_whd = cwb.current_window_handle  # 专题模块
        my_tools.switch_frame(cwb, '/html/body/div[2]/div[2]/ul/li[5]/a', now_whd, '专题')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[3]/ul/li/div[2]/span/h2/a'))+1):
            my_tools.ele_clicks(cwb, '/html/body/div[3]/div[3]/ul/li[{}]/div[2]/span/h2/a'.format(i), now_whd,
                                is_judge_link=1, is_back=1)
            my_tools.random_check(cwb, '/html/body/div[3]/div[3]/ul/li[{}]/div[2]/span/a/i'.format(i), now_whd,
                                  is_judge_link=1, is_back=1)

    def test_10(self):
        now_whd = cwb.current_window_handle  # 电脑模块
        my_tools.switch_frame(cwb, '/html/body/div[2]/div[2]/ul/li[6]/a', now_whd, '电脑')
        my_tools.random_check(cwb, '/html/body/div[3]/div[4]/div[1]/ul/li/a[2]', now_whd, is_judge_link=1, is_back=1)

    def test_11(self):
        now_whd = cwb.current_window_handle  # APP大全
        my_tools.switch_frame(cwb, '/html/body/div[2]/div[2]/ul/li[7]/a', now_whd, 'APP大全')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[3]/ul[1]/li/div/h2/a', now_whd, is_judge_link=1)


if __name__ == "__main__":
    unittest.main()