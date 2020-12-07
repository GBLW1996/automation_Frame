import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from xiazai_zol.common.warning import message
# from xiazai_zol.common.log import Logger
from xiazai_zol.common.cappic import Cappic
from xiazai_zol.pages.basepage import BasePage
import os
from selenium import webdriver
from xiazai_zol.common.tools import PageTool
from selenium.webdriver import ActionChains
import requests
options = webdriver.ChromeOptions()
path = os.path.abspath('..') + '\\downloads\\'
pre_fs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
options.add_experimental_option('prefs', pre_fs)
cwb = webdriver.Chrome(chrome_options=options)
net_183 = BasePage(cwb)
# my_logger = Logger(logger='2').getlog()
my_tools = PageTool()


class WywNet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        net_183.start_browser()

    @classmethod
    def tearDownClass(cls):
        # net_183.quit_browser()
        pass

    def test_01(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="headerWrap"]/div/div[1]/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/a', now_whd, 1, 1, 1,
                            '/html/body/div[7]/div/div[2]/div[1]/div/div[2]/div[1]/div/a', '//*[@id="downloader_main1"]'
                            , '', '', 0, '', '')
        str_list = ['QQ', 'aaa', '软件商店']
        my_tools.test_input(cwb, str_list, '//*[@id="softSearch"]', now_whd)

    def test_03(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div/ul/li/a/span', now_whd, 1, 1, 0, '//*[@id="downloader_main1"]',
                            '', 'pc', '', 0, '', '')

    def test_04(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div[1]/div[1]/div/div/a', now_whd, 0, 0, 0, '', '', '', '', 0, '',
                            '')
        my_tools.ele_clicks(cwb, '//*[@id="classification-items"]/li[11]/a', now_whd, 0, 0, 0, '', '', '', '', 0, '',
                            '')
        my_tools.ele_clicks(cwb, '//*[@id="classification-items"]/li/h4/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="classification-items"]/li/div/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', ''
                            )
        my_tools.ele_clicks(cwb, '//*[@id="focusSlideUl"]/li/a', now_whd, 0, 1, 0, '', '', '', 'title', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div[1]/div[2]/div[2]/ol/li/ul/li/a', now_whd, 0, 0, 0, '', '', '',
                            '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div[1]/div[2]/div[3]/div[2]/div[1]/ul/li/a/img', now_whd, 0, 1, 0,
                            '', '', '', 'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[7]/div[1]/div[2]/div[3]/div[2]/ul/li[2]/a')
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div[1]/div[2]/div[3]/div[2]/div[2]/ul/li/a/img', now_whd, 0, 1, 0
                            , '', '', '', 'title', 0, '/html/body/div[7]/div[1]/div[2]/div[3]/div[2]/ul/li[2]/a', '')
        my_tools.ele_clicks(cwb, '//*[@id="todayRecommend"]/h3/a', now_whd, 1, 1, 0, '//*[@id="downloader_main1"]', '',
                            'pc', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[7]/div[2]/div[3]/ul/li/h4/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')

    def test_07(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1150)
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[1]/div/ul[1]/li/a', now_whd, 0, 1, 0,
                            '', '', '', 'title', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[1]/div/ul[2]/li/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', 'title', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div/div[1]/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', 'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[9]/div[2]/div/ul/li[2]')
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div/div[2]/ul/li/a', now_whd, 1, 1, 0,
                             '//*[@id="downloader_main1"]', '', 'pc', 'title', 0, '', '')

    def test_08(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1650)
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[1]/div/div[2]/div[1]/ul/li/a[1]', now_whd, 1, 1, 0, '',
                            '//*[@id="tongjiId"]', 'app', 'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[11]/div[1]/div/div[2]/ul/li[2]')
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[1]/div/div[2]/div[2]/ul/li/a[1]', now_whd, 1, 1, 0, '',
                            '//*[@id="tongjiId"]', 'app', 'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[11]/div[1]/div/div[2]/ul/li[3]')
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[1]/div/div[2]/div[3]/ul/li/a[1]', now_whd, 1, 1, 0, '',
                            '//*[@id="tongjiId"]', 'app', 'title', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[2]/div/div[2]/div[1]/ul/li/a[1]', now_whd, 0, 1, 0, '', '', '',
                            'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[11]/div[2]/div/div[2]/ul/li[2]')
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[2]/div/div[2]/div[2]/ul/li/a[1]', now_whd, 0, 1, 0, '', '', '',
                            'title', 0, '', '')

    def test_09(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2150)
        my_tools.ele_clicks(cwb, '/html/body/div[13]/div[1]/div/div[2]/div[1]/ul/li/a[1]', now_whd, 1, 1, 0, '',
                            '//*[@id="tongjiId"]', 'app', 'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[13]/div[1]/div/div[2]/ul/li[2]')
        my_tools.ele_clicks(cwb, '/html/body/div[13]/div[1]/div/div[2]/div[2]/ul/li/a[1]', now_whd, 1, 1, 0, '',
                            '//*[@id="tongjiId"]', 'app', 'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[13]/div[1]/div/div[2]/ul/li[3]')
        my_tools.ele_clicks(cwb, '/html/body/div[13]/div[1]/div/div[2]/div[3]/ul/li/a[1]', now_whd, 1, 1, 0, '',
                            '//*[@id="tongjiId"]', 'app', 'title', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[13]/div[2]/div/div[2]/div[1]/ul/li/a[1]', now_whd, 0, 1, 0, '', '', '',
                            'title', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[13]/div[2]/div/div[2]/ul/li[2]')
        my_tools.ele_clicks(cwb, '/html/body/div[13]/div[2]/div/div[2]/div[2]/ul/li/a[1]', now_whd, 0, 1, 0, '', '', '',
                            'title', 0, '', '')

    def test_10(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2650)
        my_tools.move_in(cwb, '/html/body/div[14]/div[2]/div[2]/span[1]')
        my_tools.ele_clicks(cwb, '//*[@id="deskSlideDiv"]/ul[1]/li/a/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0,
                            '/html/body/div[14]/div[2]/div[2]/span[1]', '')
        my_tools.move_in(cwb, '/html/body/div[14]/div[2]/div[2]/span[2]')
        my_tools.ele_clicks(cwb, '//*[@id="deskSlideDiv"]/ul[2]/li/a/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0,
                            '/html/body/div[14]/div[2]/div[2]/span[2]', '')
        my_tools.move_in(cwb, '/html/body/div[14]/div[2]/div[2]/span[3]')
        my_tools.ele_clicks(cwb, '//*[@id="deskSlideDiv"]/ul[3]/li/a/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0,
                            '/html/body/div[14]/div[2]/div[2]/span[3]', '')
        my_tools.ele_clicks(cwb, '/html/body/div[14]/div[2]/div[3]/div/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_11(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2850)
        my_tools.move_in(cwb, '/html/body/div[15]/div[2]/div[2]/span[1]')
        my_tools.ele_clicks(cwb, '//*[@id="sjBiZhiSlideDiv"]/ul[1]/li/a/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0,
                            '/html/body/div[15]/div[2]/div[2]/span[1]', '')
        my_tools.move_in(cwb, '/html/body/div[15]/div[2]/div[2]/span[2]')
        my_tools.ele_clicks(cwb, '//*[@id="sjBiZhiSlideDiv"]/ul[2]/li/a/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0,
                            '/html/body/div[15]/div[2]/div[2]/span[2]', '')
        my_tools.move_in(cwb, '/html/body/div[15]/div[2]/div[2]/span[3]')
        my_tools.ele_clicks(cwb, '//*[@id="sjBiZhiSlideDiv"]/ul[3]/li/a/img', now_whd, 0, 1, 0, '', '', '', 'alt', 0,
                            '/html/body/div[15]/div[2]/div[2]/span[3]', '')
        my_tools.ele_clicks(cwb, '/html/body/div[15]/div[2]/div[3]/div/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_12(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3250)
        my_tools.ele_clicks(cwb, '/html/body/div[16]/ul/li/a', now_whd, 1, 1, 0, '//*[@id="downloader_main1"]', '', 'pc'
                            , 'title', 0, '', '')

    def test_13(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3250)
        my_tools.ele_clicks(cwb, '/html/body/div[17]/div[2]/ul/li/div/a', now_whd, 0, 0, 0, '', '', '', 'href', 0, '',
                            '')

    def test_14(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3650)
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[1]/div/a[position()<28]', now_whd, 0, 1, 0, '', '',
                            '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[1]/div/a[28]', now_whd, 0, 0, 0, '', '', '', '', 0,
                            '', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[1]/div/div[2]/ul/li[1]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[2]/div[1]/ul/li/a', now_whd, 0, 0, 0, '', '', '', ''
                            , 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[1]/div/div[2]/ul/li[2]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[2]/div[2]/ul/li/a', now_whd, 0, 0, 0, '', '', '', ''
                            , 0, '/html/body/div[18]/div[1]/div/div[2]/ul/li[2]/span', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[1]/div/div[2]/ul/li[3]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[2]/div[3]/ul/li/a', now_whd, 0, 0, 0, '', '', '', ''
                            , 0, '/html/body/div[18]/div[1]/div/div[2]/ul/li[3]/span', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[1]/div/div[2]/ul/li[4]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[2]/div[4]/ul/li/a', now_whd, 0, 0, 0, '', '', '', ''
                            , 0, '/html/body/div[18]/div[1]/div/div[2]/ul/li[4]/span', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[1]/div/div[2]/ul/li[5]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[2]/div[5]/ul/li/a', now_whd, 0, 0, 0, '', '', '', ''
                            , 0, '/html/body/div[18]/div[1]/div/div[2]/ul/li[5]/span', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[1]/div/div[2]/ul/li[6]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[2]/div[6]/ul/li/a', now_whd, 0, 0, 0, '', '', '', ''
                            , 0, '/html/body/div[18]/div[1]/div/div[2]/ul/li[6]/span', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[1]/div/div[2]/ul/li[7]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[2]/div[7]/ul/li/a', now_whd, 0, 0, 0, '', '', '', ''
                            , 0, '/html/body/div[18]/div[1]/div/div[2]/ul/li[7]/span', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[1]/div/div[2]/ul/li[8]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[2]/div[8]/ul/li/a', now_whd, 0, 0, 0, '', '', '', ''
                            , 0, '/html/body/div[18]/div[1]/div/div[2]/ul/li[8]/span', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[1]/div/div[2]/ul/li[9]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[1]/div/div[2]/div[9]/div/a', now_whd, 0, 0, 0, '', '', '', ''
                            , 0, '/html/body/div[18]/div[1]/div/div[2]/ul/li[9]/span', '')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[2]/div/div[1]/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[18]/div[2]/div/ul/li[2]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[18]/div[2]/div/div[2]/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')

    def test_15(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 3950)
        my_tools.ele_clicks(cwb, '/html/body/div[19]/div[1]/div/div[2]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, ''
                            , '')
        my_tools.ele_clicks(cwb, '/html/body/div[19]/div[1]/div/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[19]/div[2]/div/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, ''
                            , '')
        my_tools.move_in(cwb, '/html/body/div[19]/div[2]/div/ul/li[2]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[19]/div[2]/div/div[2]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, ''
                            , '')

    def test_16(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 4350)
        my_tools.ele_clicks(cwb, '/html/body/div[20]/ul/li/div/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_17(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 4350)
        my_tools.ele_clicks(cwb, '/html/body/div[22]/div[2]/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_18(self):
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 4350)
        my_tools.ele_clicks(cwb, '//*[@id="zolGlobalFooter"]/div/div/span/a', now_whd, 0, 1, 0, '', '', '', '', 1, '',
                            '')

    def test_19(self):
        # 软件分类模块
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[2]/a')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="deskSlideDiv"]/li/a', now_whd, 0, 0, 0, '', '', '', 'href', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="pnanelChild0"]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="pnanelChild1"]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[1]/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 600)
        my_tools.ele_clicks(cwb, '//*[@id="pnanelChild2"]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[2]/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1000)
        my_tools.ele_clicks(cwb, '//*[@id="pnanelChild3"]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[3]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1400)
        my_tools.ele_clicks(cwb, '//*[@id="pnanelChild4"]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[1]/div[2]/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')

    def test_20(self):
        # 装机必备
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[3]/a')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/div[1]/div[1]/div/div/div/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 1000)
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/div[1]/div[2]/div/ul/li/a/img', now_whd, 0, 1, 0, '', '', '',
                            'alt', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/div[2]/div[1]/div/ul/li/div/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/div[2]/div[2]/div/ul/li/div[1]/a', now_whd, 1, 0, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')

    def test_21(self):
        # 排行榜
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[4]/a')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div/div[2]/div/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div/div[2]/ul/li/a', now_whd, 0, 0, 0, '', '', '', 'href', 0,
                            '', '')

    def test_22(self):
        # 手机软件
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[5]/a')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="indexModel"]/li/a/span', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="indexModel"]/li/a/span', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.move_in(cwb, '//*[@id="indexModel"]/li[11]/span')
        my_tools.ele_clicks(cwb, '//*[@id="indexModel"]/li[11]/div/ul/li/a/span', now_whd, 0, 1, 0, '', '', '', '', 0,
                            '//*[@id="indexModel"]/li[11]/span', '')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/ul[2]/li/a/span', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="cacheModel"]/div[3]/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="jddiv"]/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 600)
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[1]/div[1]/ul/li/h4/a', now_whd, 0, 1, 0, '',
                            '//*[@id="tongjiId"]', 'app', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[8]/div[2]/div[1]/div[2]/ul/li/a', now_whd, 0, 1, 0, '',
                            '//*[@id="tongjiId"]', 'app', 'title', 0, '', '')
        my_tools.wintowh(cwb, 0, 900)
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[1]/div/ul/li/a[1]', now_whd, 0, 1, 0, '', '//*[@id="tongjiId"]',
                            'app', 'title', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[9]/div[2]/div/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="showdiv"]/li/a', now_whd, 0, 1, 0, '', '', '', 'title', 0, '', '')
        my_tools.wintowh(cwb, 0, 1300)
        my_tools.ele_clicks(cwb, '//*[@id="sjdt"]/li/a[1]', now_whd, 0, 1, 0, '', '//*[@id="tongjiId"]', 'app', 'title',
                            0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="android-list"]/ul[1]/li/a/span', now_whd, 0, 1, 0, '', '//*[@id="tongjiId"]',
                            'app', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div[2]/div/div[2]/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0,
                            '', '')
        my_tools.wintowh(cwb, 0, 1700)
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[1]/div/ul/li/a[1]', now_whd, 0, 1, 0, '', '//*[@id="tongjiId"]'
                            , 'app', 'title', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="ios-list"]/ul[1]/li/a/span', now_whd, 0, 1, 0, '', '//*[@id="tongjiId"]',
                            'app', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[11]/div[2]/div/div[2]/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0,
                            '', '')
        my_tools.wintowh(cwb, 0, 2000)
        my_tools.ele_clicks(cwb, '/html/body/div[12]/div[1]/div/ul/li/a[1]', now_whd, 0, 1, 0, '', '', '', 'title', 0,
                            '', '')
        my_tools.ele_clicks(cwb, '//*[@id="wp-list"]/ul[1]/li/a/span', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[12]/div[2]/div/div[2]/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, ''
                            , '')
        my_tools.wintowh(cwb, 0, 2300)
        my_tools.ele_clicks(cwb, '/html/body/div[13]/div[1]/div/ul/li/a[1]', now_whd, 0, 1, 0, '', '', '', 'title', 0,
                            '', '')
        my_tools.ele_clicks(cwb, '//*[@id="java-list"]/ul[1]/li/a/span', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[13]/div[2]/div/div[2]/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, ''
                            , '')
        my_tools.wintowh(cwb, 0, 2600)
        my_tools.ele_clicks(cwb, '/html/body/div[14]/div[1]/div/ul/li/a[1]', now_whd, 0, 1, 0, '', '', '', 'title', 0,
                            '', '')
        my_tools.ele_clicks(cwb, '//*[@id="symbian-list"]/ul[1]/li/a/span', now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="sl1"]/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.wintowh(cwb, 0, 2900)
        my_tools.ele_clicks(cwb, '/html/body/div[15]/div[1]/div/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '/html/body/div[15]/div[2]/div/div/ul/li/a', now_whd, 0, 0, 0, '', '', '', '', 0, '',
                            '')
        my_tools.ele_clicks(cwb, '/html/body/div[16]/p/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        ele = cwb.find_element_by_xpath('//*[@id="headerWrap"]/div/div[1]/a[4]')
        my_tools.static_click(cwb, ele)
        my_tools.swich_handle(cwb, now_whd)

    def test_23(self):
        # 资讯
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('//*[@id="J_MainNav"]/li[8]/a')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[2]/div[1]/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')
        my_tools.move_in(cwb, '/html/body/div[6]/div[2]/div[2]/ul/li[2]/span')
        my_tools.ele_clicks(cwb, '/html/body/div[6]/div[2]/div[2]/div[2]/ul/li/a', now_whd, 1, 1, 0,
                            '//*[@id="downloader_main1"]', '', 'pc', '', 0, '', '')
        ele = cwb.find_element_by_xpath('//*[@id="headerWrap"]/div/div[1]/a[4]')
        my_tools.static_click(cwb, ele)
        my_tools.swich_handle(cwb, now_whd)

    def test_24(self):
        # 今日更新
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('/html/body/div[4]/div/div/a[1]')
        my_tools.static_click(cwb, ele)
        time.sleep(2)
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="bida"]/dl[3]/dd/a', now_whd, 0, 1, 0, '', '', '', '', 1, '', '')


if __name__ == "__main__":
    unittest.main()