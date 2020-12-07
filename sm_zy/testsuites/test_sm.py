import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sm_zy.common.warning import message
# from sm_zy.common.log import Logger
from sm_zy.common.cappic import Cappic
from sm_zy.pages.basepage import BasePage
import os
from selenium import webdriver
from sm_zy.common.tools import PageTool
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
        my_tools.ele_clicks(cwb, '/html/body/div[1]/div/p[2]/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="recapp"]/div/div/div/ul/li/a/strong', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="recapp"]/p[1]/span/a[position()<9]', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="recapp"]/p[2]/span/a', now_whd, 1, 1, 1, '/html/body//p[text()="本地下载"]',
                            '//*[@id="address"]', '', '', 0, '', '')

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 450)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[1]/div/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[1]/div/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div/div[2]/div/ul/li[{}]/a/img'.format(i), now_whd, 0, 1,
                                0, '', '', '', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/ul/li/a[1]/p/font', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[1]/h1/a', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[1]/p/a', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[2]/div[2]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[2]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[2]/div[2]/div[{}]/ul/li/i/a'.format(i), now_whd, 0, 1
                                , 0, '', '', '', '', 0, '', '')
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[2]/div[2]/div[{}]/ul/li/p/a'.format(i), now_whd, 1, 1
                                , 1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[3]/div/div[1]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div/div[1]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div/ul/li[{}]/a/img'.format(i), now_whd
                                , 0, 1, 0, '', '', '', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div/ul/li/a/p', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div/div[2]/div[2]/div[1]/ul/li/a/p', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[5]/div[3]/div/div[2]/div[1]/div/ul/li[2]')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div/div[2]/div[2]/div[2]/ul/li/a/p', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')

    def test_03(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 850)
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/p/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div/ul/li[position()<5]/a/img', now_whd, 0, 1, 0, '', '',
                            '', 'alt', 0, '', '')
        for i in range(5, len(cwb.find_elements_by_xpath('/html/body/div[6]/div[2]/div/div/ul/li/a/img'))+1):
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[6]/div[2]/b[2]'))
            time.sleep(2)
            my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div/div/ul/li[{}]/a/img'.format(i), now_whd, 0, 1, 0, '',
                                '', '', 'alt', 0, '', '')

    def test_04(self):
        # 软件
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1250)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="Spftware"]/div[2]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '//*[@id="Spftware"]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="Spftware"]/div[2]/div[2]/div[{}]/ul/li/p/a/img'.format(i), now_whd, 1, 1,
                                1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', 'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="Spftware"]/div[2]/ul/li/a', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')

    def test_05(self):
        # 安卓
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1850)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="Android"]/div[2]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '//*[@id="Android"]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="Android"]/div[2]/div[2]/div[{}]/p/a'.format(i), now_whd, 0, 1, 0, '', '',
                                '', '', 0, '', '')
            my_tools.ele_clicks(cwb, '//*[@id="Android"]/div[2]/div[2]/div[{}]/ul[1]/li/a/p'.format(i), now_whd, 1, 1, 1
                                , '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
            my_tools.ele_clicks(cwb, '//*[@id="Android"]/div[2]/div[2]/div[{}]/ul[2]/li/a'.format(i), now_whd, 1, 1, 1
                                , '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')

    def test_06(self):
        # 苹果
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2450)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="iOS"]/div[2]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '//*[@id="iOS"]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="iOS"]/div[2]/div[2]/div[{}]/p/a'.format(i), now_whd, 0, 1, 0, '',
                                '', '', '', 0, '', '')
            my_tools.ele_clicks(cwb, '//*[@id="iOS"]/div[2]/div[2]/div[{}]/ul[1]/li/a/p'.format(i), now_whd, 1, 1, 1
                                , '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
            my_tools.ele_clicks(cwb, '//*[@id="iOS"]/div[2]/div[2]/div[{}]/ul[2]/li/a'.format(i), now_whd, 1, 1, 1
                                , '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')

    def test_07(self):
        # 资讯教程
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2850)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="Article"]/div[2]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '//*[@id="Article"]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="Article"]/div[2]/div[2]/div[{}]/ul[1]/li/a/strong'.format(i), now_whd, 0,
                                1, 0, '', '', '', '', 0, '', '')
            my_tools.ele_clicks(cwb, '//*[@id="Article"]/div[2]/div[2]/div[{}]/ul[2]/a/p'.format(i), now_whd, 0, 1, 0,
                                '', '', '', '', 0, '', '')
            my_tools.ele_clicks(cwb, '//*[@id="Article"]/div[2]/div[2]/div[{}]/ul[2]/li/a'.format(i), now_whd, 0, 1, 0,
                                '', '', '', '', 0, '', '')
            my_tools.ele_clicks(cwb, '//*[@id="Article"]/div[2]/div[2]/div[{}]/ul[3]/li/a'.format(i), now_whd, 0, 1, 0,
                                '', '', '', '', 0, '', '')

    def test_08(self):
        # 友情链接
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3050)
        my_tools.ele_clicks(cwb, '//*[@id="links-box"]/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_09(self):
        # 文章频道
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[3]/ul/li[2]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"文章频道"')
        except:
            my_tools.my_logger.error('进入"文章频道"异常')
            message('进入"文章频道"异常')
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/dl[1]/dt/ul/li/a', now_whd, 0, 1, 0, '', '', '', 'title', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/dl[1]/dd[1]/h2/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/dl[1]/dd[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/dl[1]/dd[2]/div[1]/ul/li/p/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/dl[1]/dd[2]/div[2]/div[2]/i'))+1):
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/dl[1]/dd[2]/div[2]/div[2]/i[{}]'.format(i)))
            my_tools.ele_clicks(cwb, '/html/body/dl[1]/dd[2]/div[2]/div[1]/ul/li[{}]/a/img'.format(i), now_whd, 0, 1, 0,
                                '', '', '', 'alt', 0, '', '')
        my_tools.wintowh(cwb, 0, 600)
        # 游戏攻略秘籍
        my_tools.ele_clicks(cwb, '/html/body/div[3]/h4/span[2]/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/div/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1000)
        # 安卓手游攻略
        my_tools.ele_clicks(cwb, '/html/body/dl[2]/dd/div[1]/ul/li/a/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/dl[2]/dd/div/ul/li/p/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/dl[2]/dt/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        # 安卓教程
        my_tools.ele_clicks(cwb, '/html/body/dl[3]/dd/div[1]/ul/li/a/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/dl[3]/dd/div/ul/li/p/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/dl[3]/dt/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1400)
        # MAC教程
        my_tools.ele_clicks(cwb, '/html/body/dl[4]/dd/div[1]/ul/li/a/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/dl[4]/dd/div/ul/li/p/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/dl[4]/dt/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 0)
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[2]/div/a/img'))
            my_tools.my_logger.info('进入"首页"')
        except:
            my_tools.my_logger.error('进入"首页"异常')
            message('进入"首页"异常')

    def test_10(self):
        # 软件下载
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[3]/ul/li[3]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"软件下载"')
        except:
            my_tools.my_logger.error('进入"软件下载"异常')
            message('进入"软件下载"异常')
        # 新品推荐/最近更新
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[2]/div[1]/ul[1]/li/div/p[1]/a', now_whd, 1, 1, 1
                            , '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[2]/div[1]/ul[2]/li/a/strong', now_whd, 1, 1, 1
                            , '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[2]'))
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[2]/div[2]/ul/li/div/p[1]/a', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 600)
        # 热门分类
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div/p[2]/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div/ul/li/div/p[1]/a', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 900)
        # 安全相关/行业软件
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div/p[2]/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div/ul/li/div/p[1]/a', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1400)
        # 图文处理/媒体工具
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div/p[2]/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div/ul/li/div/p[1]/a', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1800)
        # 联络聊天/教育教学
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div/p[2]/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div/ul/li/div/p[1]/a', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 2200)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[9]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[9]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div[{}]/ul/li/a/strong'.format(i), now_whd, 1, 1, 1,
                                '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')

    def test_11(self):
        # 安卓下载
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[3]/ul/li[4]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"安卓下载"')
        except:
            my_tools.my_logger.error('进入"安卓下载"异常')
            message('进入"安卓下载"异常')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[3]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[{}]/ul/li/a/strong'.format(i), now_whd, 1, 1, 1,
                                '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/div/ul/li/div[2]/a', now_whd, 1, 0, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', 'href', 0, '', '')
        my_tools.wintowh(cwb, 0, 600)
        # 安卓游戏
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[1]/div[1]/div/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[1]/div[1]/div/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div[2]/div[{}]/ul/li/a/strong'.format(i), now_whd, 1, 1,
                                1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        for x in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[2]/div[1]/div/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[2]/div[1]/div/ul/li[{}]'.format(x))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[2]/div[{}]/ul/li/a[2]'.format(x), now_whd, 1, 1,
                                1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1000)
        # 游戏专题
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div/a/strong', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1400)
        # 安卓软件
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[7]/div[1]/div[1]/div/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[7]/div[1]/div[1]/div/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[7]/div[1]/div[2]/div[{}]/ul/li/a/strong'.format(i), now_whd, 1, 1,
                                1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        for x in range(1, len(cwb.find_elements_by_xpath('/html/body/div[7]/div[2]/div[1]/div/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[7]/div[2]/div[1]/div/ul/li[{}]'.format(x))
            my_tools.ele_clicks(cwb, '/html/body/div[7]/div[2]/div[2]/div[{}]/ul/li/a[2]'.format(x), now_whd, 1, 1,
                                1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1700)
        # 软件专题
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/div/div/ul/li/a/strong', now_whd, 0, 1, 0, '', '', '', '', 0,
                            '', '')
        my_tools.wintowh(cwb, 0, 2100)
        # 安卓游戏
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div/ul/li/a/strong', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 2600)
        # 安卓软件
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div[2]/div/ul/li/a/strong', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 3100)
        # 手游攻略/应用教程
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[2]/div/a/img'))
            time.sleep(2)
            my_tools.my_logger.info('已返回首页')
        except:
            my_tools.my_logger.error('返回首页异常')
            message('返回首页异常')

    def test_12(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[3]/ul/li[5]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"苹果下载"')
        except:
            my_tools.my_logger.error('进入"苹果下载"异常')
            message('进入"苹果下载"异常')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[1]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[3]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[{}]/ul/li/a/strong'.format(i), now_whd, 1, 1, 1,
                                '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/div/ul/li/div[2]/a', now_whd, 1, 0, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', 'href', 0, '', '')
        my_tools.wintowh(cwb, 0, 600)
        # 苹果游戏
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[1]/div[1]/div/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[1]/div[1]/div/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div[2]/div[{}]/ul/li/a/strong'.format(i), now_whd, 1, 1,
                                1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        for x in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[2]/div[1]/div/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[2]/div[1]/div/ul/li[{}]'.format(x))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[2]/div[{}]/ul/li/a[2]'.format(x), now_whd, 1, 1,
                                1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 900)
        # 游戏专题
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div/a/strong', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1500)
        # 苹果软件
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[7]/div[1]/div[1]/div/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/div[7]/div[1]/div[1]/div/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[7]/div[1]/div[2]/div[{}]/ul/li/a/strong'.format(i), now_whd, 1, 1,
                                1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        for x in range(1, len(cwb.find_elements_by_xpath('/html/body/div[7]/div[2]/div[1]/div/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[7]/div[2]/div[1]/div/ul/li[{}]'.format(x))
            my_tools.ele_clicks(cwb, '/html/body/div[7]/div[2]/div[2]/div[{}]/ul/li/a[2]'.format(x), now_whd, 1, 1,
                                1, '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1900)
        # 软件专题
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/div/div/ul/li/a/strong', now_whd, 0, 1, 0, '', '', '', '', 0,
                            '', '')
        my_tools.wintowh(cwb, 0, 2300)
        # 苹果游戏
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div/ul/li/a/strong', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 2600)
        # 苹果软件
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div[2]/div/ul/li/a/strong', now_whd, 1, 1, 1,
                            '/html/body//p[text()="本地下载"]', '//*[@id="address"]', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 2900)
        # 手游攻略/应用教程
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[2]/div/a/img'))
            time.sleep(2)
            my_tools.my_logger.info('已返回首页')
        except:
            my_tools.my_logger.error('返回首页异常')
            message('返回首页异常')

    def test_13(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[3]/ul/li[6]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"MAC下载"')
        except:
            my_tools.my_logger.error('进入"MAC下载"异常')
            message('进入"MAC下载"异常')
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="slideBox"]/div[2]/ul/li/img'))+1):
            my_tools.move_in(cwb, '//*[@id="slideBox"]/div[2]/ul/li[{}]/img'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="slideBox"]/div[1]/ul/li[{}]/a[1]'.format(i), now_whd, 0, 0, 0, '', '', ''
                                , 'href', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[1]/div[2]/a', now_whd, 0, 0, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[1]/div[2]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.wintowh(cwb, 0, 600)
        # MAC软件
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div[1]/p/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div[2]/div[1]/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[2]/div[2]/div[2]/div/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[2]/div[2]/div[2]/div/div/div[{}]/ul/li/a[2]'.format(i), now_whd, 0,
                                1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div[2]/div[3]/ul/li/a/abc', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.wintowh(cwb, 0, 1100)
        # MAC游戏
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[1]/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[3]/div[2]/div[2]/div/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[2]/div/div/div[{}]/ul/li[1]/a[2]'.format(i), now_whd, 0,
                                1, 0, '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[3]/ul/li/a/abc', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')
        my_tools.wintowh(cwb, 0, 1700)
        # MAC 软件必备推荐
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[2]/div/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.wintowh(cwb, 0, 2500)
        # MAC 游戏必备推荐
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div/div[2]/a'))
            time.sleep(2)
            my_tools.my_logger.info('已返回首页')
        except:
            my_tools.my_logger.error('返回首页异常')
            message('返回首页异常')

    def test_14(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[3]/ul/li[7]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"素材下载"')
        except:
            my_tools.my_logger.error('进入"素材下载"异常')
            message('进入"素材下载"异常')
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div/div/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        my_tools.wintowh(cwb, 0, 400)
        # 专题推荐区
        time.sleep(2)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/ul/li'))+1):
            my_tools.move_in(cwb, '/html/body/div[3]/div[1]/div[2]/div[2]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[{}]/a[2]'.format(i), now_whd, 0, 1, 0
                                , '', '', '', '', 1, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[1]/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[1]/ul/li/a'))+1):
            my_tools.move_in(cwb, '/html/body/div[3]/div[2]/div/div[1]/ul/li[{}]/a'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div/div[2]/div[{}]/ul[1]/li/a'.format(i), now_whd, 0, 0,
                                0, '', '', '', '', 1, '/html/body/div[3]/div[2]/div/div[1]/ul/li[{}]/a'.format(i), '')
            my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div/div[2]/div[{}]/ul[2]/li/a'.format(i), now_whd, 0, 0,
                                0, '', '', '', '', 1, '/html/body/div[3]/div[2]/div/div[1]/ul/li[{}]/a'.format(i), '')
        my_tools.wintowh(cwb, 0, 850)
        # 行业软件
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/div[4]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[4]/div[2]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 0, 0, '',
                                '', '', '', 1, '/html/body/div[4]/div[2]/div[1]/ul/li[{}]'.format(i), '')
        my_tools.wintowh(cwb, 0, 1350)
        # 视频模板
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[2]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 0, 0, '',
                                '', '', '', 1, '/html/body/div[5]/div[2]/div[1]/ul/li[{}]'.format(i), '')
        my_tools.wintowh(cwb, 0, 1850)
        # PSD模板
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[6]/div[2]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/div[6]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 0, 0, '',
                                '', '', '', 1, '/html/body/div[6]/div[2]/div[1]/ul/li[{}]'.format(i), '')
        my_tools.wintowh(cwb, 0, 2350)
        # 平面素材
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[7]/div[2]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/div[7]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[7]/div[2]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 0, 0, '',
                                '', '', '', 1, '/html/body/div[7]/div[2]/div[1]/ul/li[{}]'.format(i), '')
        my_tools.wintowh(cwb, 0, 2850)
        # 3D模型
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[8]/div[2]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/div[8]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 0, 0, '',
                                '', '', '', 1, '/html/body/div[8]/div[2]/div[1]/ul/li[{}]'.format(i), '')
        my_tools.wintowh(cwb, 0, 3350)
        # 音频素材推荐
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[9]/div[2]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/div[9]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 0, 0, '',
                                '', '', '', 1, '/html/body/div[9]/div[2]/div[1]/ul/li[{}]'.format(i), '')
        my_tools.wintowh(cwb, 0, 3850)
        # 在线PS处理推荐
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[10]/div[2]/div[1]/ul/li')) + 1):
            my_tools.move_in(cwb, '/html/body/div[10]/div[2]/div[1]/ul/li[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[10]/div[2]/div[2]/div[{}]/ul/li/a'.format(i), now_whd, 0, 0, 0, '',
                                '', '', '', 1, '/html/body/div[10]/div[2]/div[1]/ul/li[{}]'.format(i), '')
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/a'))
            time.sleep(2)
            my_tools.my_logger.info('已返回首页')
        except:
            my_tools.my_logger.error('返回首页异常')
            message('返回首页异常')

    def test_15(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('/html/body/div[3]/ul/li[8]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"专题合集"')
        except:
            my_tools.my_logger.error('进入"专题合集"异常')
            message('进入"专题合集"异常')
        time.sleep(2)
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/div/ul/li[position()<5]/a/strong', now_whd, 0, 1, 0, '', '', '',
                            '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div/div[2]/ul/li/a/span', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')


if __name__ == "__main__":
    unittest.main()