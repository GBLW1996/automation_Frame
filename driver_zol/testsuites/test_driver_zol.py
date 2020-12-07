import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from driver_zol.common.warning import message
# from driver_zol.common.log import Logger
from driver_zol.common.cappic import Cappic
from driver_zol.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from selenium import webdriver
from driver_zol.common.tools import PageTool
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
        # BasePage(cwb).quit_browser()
        pass

    def test_01(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="headerWrap"]/div/div[1]/a', now_whd)
        my_tools.move_in(cwb, '//*[@id="headerWrap"]/div/div[3]/span')
        my_tools.ele_clicks(cwb, '//*[@id="headerWrap"]/div/div[3]/div/ul/li/a', now_whd,
                            mv_xp='//*[@id="headerWrap"]/div/div[3]/span')
        my_tools.test_input(cwb, ['windows7', '监控', 'QQ', '驱动', '硬盘'], '//*[@id="softSearch"]', now_whd)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[1]/div/div/div/div/a'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[1]/div/div/div[{}]/div/a'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div/div/div[{}]/dl/dd/a'.format(i), now_whd,
                                mv_xp='/html/body/div[5]/div[1]/div/div/div[{}]/div/a'.format(i))
        my_tools.ele_clicks(cwb, '//*[@id="driverSearchHotHardware"]/ul/li/a', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[2]/ul/li/a[2]', now_whd, is_judge_link=1)

    def test_02(self):
        # 办公驱动
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 600)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[1]/div/div/span/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[1]/div/div/strong/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/ul/li/a', now_whd)

    def test_03(self):
        # 硬件驱动
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1100)
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div[2]/div[1]/div/div/span/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div[2]/div[1]/div/div/strong/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div[2]/div/ul/li/a', now_whd)

    def test_04(self):
        # 网络驱动
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1600)
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/div[1]/div/div/span/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/div[1]/div/div/strong/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/div/ul/li/a', now_whd)

    def test_05(self):
        # 数码驱动
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1800)
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div[1]/div/div/span/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div[1]/div/div/strong/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div/ul/li/a', now_whd)

    def test_06(self):
        # 笔记本驱动
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1800)
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div[2]/div[1]/div/div/span/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div[2]/div[1]/div/div/strong/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div[2]/div/ul/li/a', now_whd)

    def test_07(self):
        # 品牌专区
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3000)
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[2]/ul/li/div/a', now_whd, attr='href')

    def test_08(self):
        # 常用测试软件
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3000)
        my_tools.ele_clicks(cwb, '/html/body/div[12]/div[2]/ul/li/ul/li/a', now_whd, is_judge_link=1)

    def test_09(self):
        # 最新驱动
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 5200)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[13]/div[2]/ul/li/a'))):
            my_tools.move_in(cwb, '/html/body/div[13]/div[2]/ul/li[{}]/a'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[13]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, is_judge_link=1)

    def test_10(self):
        # 装机必备软件
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 5200)
        my_tools.ele_clicks(cwb, '/html/body/div[14]/div[1]/ul/li/a/span', now_whd, is_judge_link=1)
        # 友情链接
        my_tools.ele_clicks(cwb, '/html/body/div[15]/ul/li/a', now_whd)


if __name__ == "__main__":
    unittest.main()
    '/html/body/div[15]/ul/li/a'