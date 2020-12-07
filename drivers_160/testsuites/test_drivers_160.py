import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from drivers_160.common.warning import message
# from drivers_160.common.log import Logger
from drivers_160.common.cappic import Cappic
from drivers_160.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from drivers_160.common.tools import PageTool
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
        my_tools.move_in(cwb, '/html/body/div[3]/div/div/span')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/div/div/dl/dt/a', now_whd, is_judge_link=1, is_back=1,
                            mv_xp='/html/body/div[3]/div/div/span')
        my_tools.move_in(cwb, '/html/body/div[3]/div/div/span')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/div/div/dl/dd/a', now_whd, is_judge_link=1, is_back=1,
                            mv_xp='/html/body/div[3]/div/div/span')
        my_tools.test_input(cwb, ['QQ', '显卡', '万能网卡驱动', '无线驱动', '打印机驱动'], '//*[@id="search_n"]', now_whd)
        BasePage(cwb).back()
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/ul[2]/li/a', now_whd, is_judge_link=1, is_back=1)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div[1]/div[1]/div[1]/div[1]/ul/li/a', now_whd, is_judge_link=1,
                            is_back=1)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div[1]/div[1]/div[1]/div[2]/div/ul[1]/li/a/img', now_whd,
                            attr='alt')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div[1]/div[1]/div[2]/ul/li/a/img', now_whd, attr='src',
                            is_back=1)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div[1]/div[2]/div[2]/ul/li/a/p', now_whd, is_back=1,
                            is_judge_link=1)

    def test_02(self):
        # 装机必备
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 800)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div[3]/div/div[1]/div/a', now_whd, is_back=1, is_judge_link=1)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div[3]/div/div[2]/div[1]/ul/li/a/p', now_whd, is_back=1,
                            is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="softlist"]/ul/li[position()>1]/div[1]/a', now_whd, is_back=1, is_judge_link=1)

    def test_03(self):
        # 核心驱动
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1400)
        # 所有分类图片
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div/div/div[2]/div/div[1]/div[1]/ul/li/a/p', now_whd, is_back=1)
        # 所有分类中间a链接
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div/div/div[2]/div/div[2]/ul/li/a', now_whd, is_back=1)
        # 所有分类右边a链接
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div/div/div[2]/div/div[3]/div[2]/ul/li/div[1]/a', now_whd,
                            is_back=1)
        # 友情链接
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div/div[10]/div[2]/a', now_whd)

    def test_04(self):
        # 万能驱动
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '/html/body/div[3]/div/ul[1]/li[2]/a', now_whd, '万能驱动')
        my_tools.random_check(cwb, '/html/body/div[7]/div/div[2]/div[1]/div/ul/li/a', now_whd, is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[7]/div/div[2]/div[2]/div[1]/ul/li/a/p', now_whd, is_back=1,
                              is_judge_link=1)
        my_tools.random_check(cwb, '//*[@id="softlist"]/ul/li[position()>1]/div[1]/a', now_whd, is_back=1,
                              is_judge_link=1)
        my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[4]/div[2]/div/a'))

    def test_05(self):
        # 笔记本驱动
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '/html/body/div[3]/div/ul[1]/li[3]/a', now_whd, '笔记本驱动')
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[2]/div[2]/div[1]/ul/li/a/p', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[1]/ul/li/a', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[4]/div[2]/ul/li/a/div[2]/h3', now_whd,
                              is_judge_link=1)
        my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[2]/div[2]/div/a'))

    def test_06(self):
        # 打印机驱动
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '/html/body/div[3]/div/ul[1]/li[4]/a', now_whd, '打印机驱动')
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[2]/div[2]/div[1]/ul/li/a/p', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[3]/div[2]/ul/li/a', now_whd, is_back=1,
                              is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[4]/div[2]/div[1]/ul/li/a', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[5]/div[2]/ul/li/a/div[2]/h3', now_whd,
                              is_judge_link=1)
        my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[2]/div[2]/div/a'))

    def test_07(self):
        # 显卡驱动
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '/html/body/div[3]/div/ul[1]/li[5]/a', now_whd, '显卡驱动')
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[2]/div[2]/div[1]/ul/li/a/p', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[3]/div[2]/ul/li/a', now_whd, is_back=1,
                              is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[4]/div[2]/div[1]/ul/li/a', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[5]/div[2]/ul/li/a/div[2]/h3', now_whd,
                              is_judge_link=1)
        my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[2]/div[2]/div/a'))

    def test_08(self):
        # 无线网卡驱动
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '/html/body/div[3]/div/ul[1]/li[6]/a', now_whd, '无线网卡驱动')
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[2]/div[2]/div[1]/ul/li/a/p', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[3]/div[2]/ul/li/a', now_whd, is_back=1,
                              is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[4]/div[2]/div[1]/ul/li/a', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[5]/div[2]/ul/li/a/div[2]/h3', now_whd,
                              is_judge_link=1)
        my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[2]/div[2]/div/a'))

    def test_09(self):
        # 声卡驱动
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '/html/body/div[3]/div/ul[1]/li[7]/a', now_whd, '声卡驱动')
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[2]/div[2]/div[1]/ul/li/a/p', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[3]/div[2]/ul/li/a', now_whd, is_back=1,
                              is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[4]/div[2]/div[1]/ul/li/a', now_whd,
                              is_back=1, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[2]/div[5]/div[2]/ul/li/a/div[2]/h3', now_whd,
                              is_judge_link=1)
        my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[2]/div[2]/div/a'))

    def test_10(self):
        # 驱动大全
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '/html/body/div[3]/div/ul[1]/li[8]/a', now_whd, '驱动大全')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div/div/div[1]/span'))+1):
            my_tools.random_check(cwb, '/html/body/div[5]/div/div[2]/div[1]/div/div[{}]/div[2]/div/div[2]/a/h3'.format(i)
                                  , now_whd, is_judge_link=1, is_back=1)


if __name__ == "__main__":
    unittest.main()
    '/html/body/div[5]/div/div[2]/div[1]/div/div[{}]/div[2]/div/div[2]/a/h3'