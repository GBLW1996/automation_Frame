import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from wangye_cn.common.warning import message
# from wangye_cn.common.log import Logger
from wangye_cn.common.cappic import Cappic
from wangye_cn.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from selenium import webdriver
from wangye_cn.common.tools import PageTool
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
        my_tools.ele_clicks(cwb, '/html/body/div[1]/div/div/div[1]/ul/li/a', now_whd)
        my_tools.move_in(cwb, '/html/body/div[1]/div/div/div[3]/a/span')
        my_tools.ele_clicks(cwb, '/html/body/div[1]/div/div/div[3]/div/dl/dd/a', now_whd,
                            mv_xp='/html/body/div[1]/div/div/div[3]/a/span')
        my_tools.test_input(cwb, ["QQ", "游戏", "斗鱼", "微信", "word"], '//*[@id="searchValue"]', now_whd)

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/a', now_whd, 0, is_judge_link=1)
        my_tools.ele_clicks(cwb, '/html/body/div[3]/ul[1]/li/a/span', now_whd, 0, is_judge_link=1)
        my_tools.ele_clicks(cwb, '/html/body/div[3]/ul[2]/li/a', now_whd, 0, is_judge_link=1)
        my_tools.wintowh(cwb, 0, 500)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[4]/div[1]/div[1]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[4]/div[1]/div[1]/div[2]/ul/li[{}]/a/img'.format(i), now_whd,
                                attr='src')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[4]/div[1]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[4]/div[1]/div[2]/div[2]/div[{}]/ul[1]/li/a/img'.format(i), now_whd,
                                is_judge_link=1, attr='alt')
            my_tools.ele_clicks(cwb, '/html/body/div[4]/div[1]/div[2]/div[2]/div[{}]/ul[2]/li/a'.format(i), now_whd,
                                is_judge_link=1, attr='title')
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[2]/div/div[2]/div[1]/div/h2/a', now_whd, 0, 1, 0, '', '', '', ''
                            , 0, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[4]/div[2]/div/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[4]/div[2]/div/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[4]/div[2]/div/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 1, 0,
                                '', '', '', '', 0, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[4]/div[3]/div/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[4]/div[3]/div/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[4]/div[3]/div/div[2]/ul/a[{}]/img'.format(i), now_whd, 0, 1, 0, '',
                                '', '', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[3]/ul/li/a', now_whd, 0, 1, 0, '', '', '', 'title', 0, '', '')

    def test_03(self):
        # 电脑必备/安卓必备/游戏下载
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 800)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div[1]/ul/li/div[1]/p/a', now_whd)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[1]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, attr='href')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[2]/h3/a', now_whd, 0, is_judge_link=1, attr='title')

    def test_04(self):
        # 最新下载
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1400)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[6]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[6]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[{}]/div[2]/ul/li/a'.format(i), now_whd, 0, 1, 0, '',
                                '', '', 'title', 0, '', '')

    def test_05(self):
        # 分类推荐
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2000)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[7]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[7]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[7]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 1, 0, '', '', '',
                                'title', 0, '', '')

    def test_06(self):
        # 最近更新
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2500)
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[1]/ul[1]/li/a', now_whd, 0, is_judge_link=1, attr='title')
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[1]/ul[2]/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/div[2]/h3/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_07(self):
        # 友情链接
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2800)
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_08(self):
        # 软件下载
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/ul/li[2]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"软件下载"模块，将执行随机函数')
        except:
            my_tools.my_logger.error('进入"软件下载"模块异常')
            # message('进入"软件下载"模块异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.random_check(cwb, '/html/body/div[3]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.random_check(cwb, '/html/body/div[4]/div[1]/ul[1]/li/a/span[1]', now_whd, 0, 1, 0, '', '', '', '', 0,
                              '', '')
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[1]/ul/li/a/span', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[2]/div[2]/div[1]/h3/a', now_whd, is_judge_link=0,
                              attr='title')
        my_tools.move_in(cwb, '/html/body/div[4]/div[2]/div[2]/div[1]/ul/li[2]')
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/h3/a', now_whd, is_judge_link=0,
                              attr='title')

    def test_09(self):
        # 应用下载
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/ul/li[3]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"应用下载"模块，将执行随机函数')
        except:
            my_tools.my_logger.error('进入"应用下载"模块异常')
            # message('进入"应用下载"模块异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.random_check(cwb, '/html/body/div[3]/ul/li/a', now_whd)
        my_tools.random_check(cwb, '/html/body/div[4]/div[1]/ul[1]/li/a/span[1]', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[1]/ul/li/a/span', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[2]/div[2]/div[1]/h3/a', now_whd, is_judge_link=0)
        my_tools.move_in(cwb, '/html/body/div[4]/div[2]/div[2]/div[1]/ul/li[2]')
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/h3/a', now_whd, is_judge_link=0)

    def test_10(self):
        # 游戏下载
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/ul/li[4]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"应用下载"模块，将执行随机函数')
        except:
            my_tools.my_logger.error('进入"应用下载"模块异常')
            # message('进入"应用下载"模块异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.random_check(cwb, '/html/body/div[3]/ul/li/a', now_whd)
        my_tools.random_check(cwb, '/html/body/div[4]/div[1]/ul[1]/li/a/span[1]', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[1]/ul/li/a/span', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[2]/div[2]/div[1]/h3/a', now_whd, is_judge_link=0)
        my_tools.move_in(cwb, '/html/body/div[4]/div[2]/div[2]/div[1]/ul/li[2]')
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/h3/a', now_whd, is_judge_link=0)

    def test_11(self):
        # 内容资讯
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/ul/li[5]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"应用下载"模块，将执行随机函数')
        except:
            my_tools.my_logger.error('进入"应用下载"模块异常')
            # message('进入"应用下载"模块异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.random_check(cwb, '/html/body/div[3]/ul/li/a', now_whd)
        my_tools.random_check(cwb, '/html/body/div[4]/div[1]/ul[1]/li/div/div/h4/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[1]/ul/li/a/span', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[2]/div[2]/div[1]/h3/a', now_whd, is_judge_link=0)
        my_tools.move_in(cwb, '/html/body/div[4]/div[2]/div[2]/div[1]/ul/li[2]')
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/h3/a', now_whd, is_judge_link=0)


if __name__ == "__main__":
    unittest.main()