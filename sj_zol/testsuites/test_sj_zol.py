import random
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sj_zol.common.warning import message
# from sj_zol.common.log import Logger
from sj_zol.common.cappic import Cappic
from sj_zol.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from sj_zol.common.tools import PageTool
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
        my_tools.test_input(cwb, ["QQ", "微信", "保卫萝卜", "部落冲突", "皇室战争"], '//*[@id="softSearch"]', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="indexModel"]/li/a/span', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/ul[2]/li/a/span', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="cacheModel"]/div[3]/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="jddiv"]/li/a/span', now_whd)

    def test_02(self):  # 明星软件推荐
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 600)
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[1]/div[1]/ul/li/h4/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/div[1]/div[2]/ul/li/a/span', now_whd)

    def test_03(self):  # 热门软件更新
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1000)
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[1]/div/ul/li/a[1]', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div/ul/li/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="showdiv"]/li/a/span', now_whd)

    def test_04(self):  # 安卓软件排行
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1400)
        my_tools.ele_clicks(cwb, '//*[@id="sjdt"]/li/a[1]', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="android-list"]/ul/li/a/span', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div[2]/div/div[2]/ul/li/a', now_whd)

    def test_05(self):  # iphone/ISO软件排行
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1800)
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[1]/div/ul/li/a[1]', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="ios-list"]/ul/li/a/span', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[2]/div/div[2]/ul/li/a', now_whd)

    def test_06(self):  # windows phone软件排行
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2200)
        my_tools.ele_clicks(cwb, '/html/body/div[12]/div[1]/div/ul/li/a[1]', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="wp-list"]/ul/li/a/span', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[12]/div[2]/div/div[2]/ul/li/a', now_whd)

    def test_07(self):  # java软件排行
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2600)
        my_tools.ele_clicks(cwb, '/html/body/div[13]/div[1]/div/ul/li/a[1]', now_whd)

    def test_08(self):  # 塞班软件排行
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2600)
        my_tools.ele_clicks(cwb, '//*[@id="symbian-list"]/ul/li/a/span', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="sl1"]/li/a', now_whd)

    def test_09(self):  # 手机关注排行
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3000)
        my_tools.ele_clicks(cwb, '/html/body/div[15]/div[1]/div/ul/li/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[15]/div[2]/div/div/ul/li/a', now_whd)
        # 友情链接
        my_tools.ele_clicks(cwb, '/html/body/div[16]/p/a', now_whd)


if __name__ == "__main__":
    unittest.main()