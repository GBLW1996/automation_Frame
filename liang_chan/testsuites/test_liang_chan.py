import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from liang_chan.common.warning import message
# from liang_chan.common.log import Logger
from liang_chan.common.cappic import Cappic
from liang_chan.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from liang_chan.common.tools import PageTool
from selenium.webdriver import ActionChains
import requests
from selenium import webdriver
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
        my_tools.test_input(cwb, ['QQ', '360', '金山', '电脑管家', '浏览器'], '//*[@id="keyword"]', now_whd)
        BasePage(cwb).back()
        my_tools.ele_clicks(cwb, '//*[@id="recapp"]/div/div/div/ul/li/a/strong', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div/div[2]/div/ul/li/a/p/strong', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/ul/li[position()<5]/a[1]/p/font', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[2]/div[2]/div/ul/li/p/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div/ul/li/a/p/strong', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div/ul/li/a/p', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div/div[2]/div[2]/div/ul/li/a/p', now_whd)

    def test_02(self):
        # 软件必备
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1000)
        my_tools.ele_clicks(cwb, '//*[@id="Spftware"]/div[2]/div[2]/div/ul/li/p/a', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="Spftware"]/div[2]/ul/li/a', now_whd, is_judge_link=1)

    def test_03(self):
        # 安卓必备
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1500)
        my_tools.ele_clicks(cwb, '//*[@id="Android"]/div[2]/div[2]/div/p/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="Android"]/div[2]/div[2]/div/ul/li/a/p', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="Android"]/div[2]/div[2]/div/ul[2]/li/a', now_whd)

    def test_04(self):
        # 资讯教程
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2000)
        my_tools.ele_clicks(cwb, '//*[@id="Article"]/div[2]/div[2]/div/ul[1]/li/a/strong', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="Article"]/div[2]/div[2]/div/ul[2]/a/p', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="Article"]/div[2]/div[2]/div/ul[2]/li/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="Article"]/div[2]/div[2]/div/ul[3]/li/a', now_whd)
        my_tools.wintobt(cwb)
        my_tools.ele_clicks(cwb, '//*[@id="links-box"]/ul/li/a', now_whd)


if __name__ == "__main__":
    unittest.main()