import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from da_bao_123.common.warning import message
# from da_bao_123.common.log import Logger
from da_bao_123.common.cappic import Cappic
from da_bao_123.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from da_bao_123.common.tools import PageTool
from selenium.webdriver import ActionChains
import requests
from selenium import webdriver
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
        my_tools.ele_clicks(cwb, '/html/body/div[4]/ul/li/a', now_whd, is_back=1)
        my_tools.ele_clicks(cwb, '//*[@id="main_box"]/div[2]/div/ul/li/a[2]', now_whd)
        my_tools.ele_clicks(cwb, '/html/body//*[@id="main_box"]/div[4]/div[2]/ul/li/a', now_whd)
        # 栏目推荐
        my_tools.ele_clicks(cwb, '//*[@id="main_box2"]/ul/li/span[2]/a', now_whd, is_back=1)
        my_tools.ele_clicks(cwb, '//*[@id="main_box2"]/div/ul/li/a', now_whd)

    def test_02(self):
        # 最新资源
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/ul/li/a', now_whd)

    def test_03(self):
        # 最新打包
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/ul/li/a', now_whd)

    def test_04(self):
        # 精品打包
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div[2]/ul/li/a', now_whd)

    def test_05(self):
        # 有声小说 小说打包....
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="main_box3"]/div/div/ul/li/a[2]', now_whd)

    def test_06(self):
        # 视频教程
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="main_box3"]/div[3]/ul/li/a', now_whd)
        # 友情链接
        my_tools.ele_clicks(cwb, '//*[@id="friendlink"]/ul/li/a', now_whd)


if __name__ == "__main__":
    unittest.main()