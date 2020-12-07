import random
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from qq_xiazai.common.warning import message
# from qq_xiazai.common.log import Logger
from qq_xiazai.common.cappic import Cappic
from qq_xiazai.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from qq_xiazai.common.tools import PageTool
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
        my_tools.test_input(cwb, ["QQ", "微信", "陌陌", "soul", "钉钉"], '//*[@id="searchfield"]', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[1]/ul/li/a/span', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[2]/dl/dd/a', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="main1_l_bar_box"]/ul/li/a/p/span', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div[2]/a/div/p[1]', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="newsa"]/div/ul/li/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div[3]/div[1]/div[2]/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="main_news_r2_title"]/a', now_whd)

    def test_02(self):  # 必备软件
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1000)
        my_tools.ele_clicks(cwb, '//*[@id="a1a"]/div[1]/dl/dd/a/span[2]', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="a1a"]/div[2]/div[2]/dl/dt/a', now_whd, is_judge_link=1)

    def test_03(self):  # 手机游戏
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1600)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div[5]/div[2]/div/div[2]/ul/li/a/div[1]', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div[5]/div[2]/div/div[3]/div[2]/dl/dt/a', now_whd)

    def test_04(self):  # 分类
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2600)
        my_tools.ele_clicks(cwb, '//*[@id="fenla"]/div/ul/li/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="partner"]/ul/li/a', now_whd)  # 友情链接


if __name__ == "__main__":
    unittest.main()