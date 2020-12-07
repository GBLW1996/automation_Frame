import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from xi_tong_zhi_jia.common.warning import message
# from xi_tong_zhi_jia.common.log import Logger
from xi_tong_zhi_jia.common.cappic import Cappic
from xi_tong_zhi_jia.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from selenium import webdriver
from xi_tong_zhi_jia.common.tools import PageTool
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
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div/div/a', now_whd, is_judge_link=1)
        my_tools.move_in(cwb, '/html/body/div[2]/div/div/div/a')
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div/div/div/div/div/dl/dd/a', now_whd,
                            mv_xp='/html/body/div[2]/div/div/a')
        my_tools.test_input(cwb, ['QQ', '安卓', 'office', 'word', 'powerpoint'],
                            '//*[@id="top"]/div[2]/div/div/form/input[1]', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[4]/dl/dd/a', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="win7list"]/table/tbody/tr/td[2]/div/center/div/div/ul/li/a/img', now_whd,
                            is_judge_link=1, attr='alt')
        my_tools.ele_clicks(cwb, '//*[@id="win7list"]/table/tbody/tr/td[4]/div[1]/div/h1/a/font', now_whd,
                            is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="win7list"]/table/tbody/tr/td[4]/div[1]/ul/li/a', now_whd, is_judge_link=1,
                            is_back=1)

    def test_02(self):
        # win10系统下载
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 550)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div/div/div/div[2]/div[1]/div/div/ul/li/a/p', now_whd)
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="_jh"]'))
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div/div/div/div[2]/div[2]/div/div/div/ul/li/a/p', now_whd)
        # 所有a链接
        my_tools.ele_clicks(cwb, '//*[@id="xt_onload"]/div/div/ul/li/a', now_whd, is_judge_link=1, attr='title')

    def test_03(self):
        # win10专业版下载
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1200)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div/div/div/div[1]/div[2]/div/ul/li/div/a', now_whd,
                            is_judge_link=1, attr='title')
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div/div/div/div[2]/div[2]/p/a', now_whd, is_judge_link=1,
                            attr='title')

    def test_04(self):
        # 软件下载
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2200)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div/div/div[3]/div/ul/li/div/a[1]', now_whd)

    def test_05(self):
        # 友情链接
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2900)
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[3]/div/div[2]/a', now_whd)

    def test_06(self):
        # win10专业版
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="nav"]/ul/li[2]/a', now_whd, 'win10专业版')
        my_tools.random_check(cwb, '/html/body/div[3]/dl/dd/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[4]/div[1]/div[1]/div[1]/ul/li/h4/a', now_whd,
                              is_judge_link=1, attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[4]/div[1]/div[2]/div/div[1]/a', now_whd, is_back=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[4]/div[1]/div[2]/div/div[3]/ul/li/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[4]/div[1]/div[2]/div/div[5]/div[2]/ul/li/a[2]', now_whd,
                              is_judge_link=1, attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[4]/div[1]/div[2]/div/div[7]/ul/li/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[4]/div[1]/div[2]/div/div[9]/ul/li/a', now_whd, is_judge_link=1)

    def test_07(self):
        # win10纯净版
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="nav"]/ul/li[3]/a', now_whd, 'win10纯净版')
        my_tools.random_check(cwb, '/html/body/div[3]/dl/dd/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[1]/div[1]/ul/li/h4/a/b', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div[1]/a', now_whd, is_back=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div[3]/ul/li/a', now_whd, is_judge_link=1,
                              attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div[5]/div[2]/ul/li/a[2]', now_whd,
                              is_judge_link=1, attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div[7]/ul/li/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div[9]/ul/li/a', now_whd, is_judge_link=1)

    def test_08(self):
        # win7旗舰版
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="nav"]/ul/li[4]/a', now_whd, 'win7旗舰版')
        my_tools.random_check(cwb, '/html/body/div[3]/dl/dd/a', now_whd, is_judge_link=1, is_back=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[1]/div[2]/ul/li/h4/a/b', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div/div[3]/ul/li/a', now_whd, attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div/div[5]/div[2]/ul/li/a[2]', now_whd,
                              is_judge_link=1, attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div/div[7]/ul/li/a', now_whd,
                              is_judge_link=1, attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div/div[7]/div[3]/ul/li/a', now_whd,
                              is_judge_link=1, attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div/div[7]/div[5]/ul/li/a', now_whd,
                              is_judge_link=1, attr='title')

    def test_09(self):
        # win8系统
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="nav"]/ul/li[5]/a', now_whd, 'win8系统')
        my_tools.random_check(cwb, '/html/body/div[3]/dl/dd/a', now_whd, is_judge_link=1, is_back=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[1]/div[2]/ul/li/h4/a/b', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div[1]/ul/li/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div[3]/div[2]/ul/li/a[2]', now_whd,
                              is_judge_link=1, attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div[5]/ul/li/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div[1]/div[2]/div/div[7]/ul/li/a', now_whd, is_judge_link=1)

    def test_10(self):
        # 系统教程
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="nav"]/ul/li[6]/a', now_whd, '系统教程')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[1]/div[2]/ul/li/h4/a/b', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[2]/div/div[2]/ul/li/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[2]/div/div[4]/div[2]/ul/li/a[2]', now_whd,
                              is_judge_link=1, attr='title')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[2]/div/div[8]/ul/li/a', now_whd, is_judge_link=1)

    def test_11(self):
        # 软件下载
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="nav"]/ul/li[7]/a', now_whd, '软件下载')
        my_tools.random_check(cwb, '//*[@id="main"]/div[1]/ul/li/a/p', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[1]/div[1]/ul/li/h4/a/b', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[2]/div/div[2]/ul/li/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[2]/div/div[4]/div[2]/ul/li/a[2]', now_whd,
                              is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[2]/div/div[8]/ul/li/a', now_whd, is_judge_link=1)

    def test_12(self):
        # IT资讯
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="nav"]/ul/li[8]/a', now_whd, 'IT资讯')
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[1]/div[1]/ul/li/h4/a/b', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[2]/div/div[2]/ul/li/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[2]/div/div[4]/div[2]/ul/li/a[2]', now_whd,
                              is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="main"]/div[3]/div/div[2]/div/div[8]/ul/li/a', now_whd, is_judge_link=1)


if __name__ == "__main__":
    unittest.main()
    ''