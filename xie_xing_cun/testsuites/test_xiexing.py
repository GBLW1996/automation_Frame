import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from xie_xing_cun.common.warning import message
# from xie_xing_cun.common.log import Logger
from xie_xing_cun.common.cappic import Cappic
from xie_xing_cun.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from selenium import webdriver
from xie_xing_cun.common.tools import PageTool
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
        try:
            cwb.find_element_by_xpath('//*[@id="Keyword"]').send_keys('语文\n')
            time.sleep(2)
            if my_tools.page_tt_code(cwb.title):
                my_tools.my_logger.info('搜索框正常')
            else:
                my_tools.my_logger.error('搜索框异常')
                # message('搜索框异常')
        except:
            my_tools.my_logger.error('搜索框异常')
            # message('搜索框异常')
        my_tools.close_hd_back(cwb, now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="top"]/div/table/tbody/tr/td[2]/b/b/font/a', now_whd, 0, 1, 0, '', '', '', '',
                            0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="top"]/div/table/tbody/tr/td[2]/b/b/a', now_whd, 0, 0, 0, '', '', '', '', 0,
                            '', '')
        my_tools.ele_clicks(cwb, '//*[@id="top"]/div/table/tbody/tr/td[3]/div/b/a[position()>1 and position()<5]',
                            now_whd, 0, 1, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/strong/a', now_whd
                            , 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[3]/tbody/tr/td/table/tbody/tr/td/div/a', now_whd, 0, 0,
                            0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/div[1]/table/tbody/tr/td[3]/div/font/a', now_whd, 0, 0, 0, ''
                            , '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table/tbody/tr/td/div/table/tbody/tr/td/div/a', now_whd, 0, 0, 0, ''
                            , '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="table4"]/tbody/tr/td[2]/div/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="table4"]/tbody/tr/td/div/strong/a', now_whd, 0, 0, 0, '', '', '', '', 0, '',
                            '')
        my_tools.ele_clicks(cwb, '//*[@id="table4"]/tbody/tr/td[2]/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="table4"]/tbody/tr[1]/td/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="table4"]/tbody/tr[2]/td/a', now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/p[1]/table/tbody/tr[2]/td/table/tbody/tr/td/p/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb,
                            '//*[@id="header"]/p[1]/table/tbody/tr[2]/td/table/tbody/tr/td/p/table/tbody/tr/td[2]/a',
                            now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_02(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[2]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"小学"')
        except:
            my_tools.my_logger.error('进入"小学"异常')
            message('进入"小学"异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/strong/a', now_whd
                            , 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[3]/tbody/tr/td/table/tbody/tr/td/div/a/img', now_whd, 0
                            , 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/div/a', now_whd, 0, 0,
                            0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td/b/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="space"]/tr[1]/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0, '', '', '', '',
                            0, '', '')
        my_tools.ele_clicks(cwb,
                            '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/'
                            'tbody/tr[2]/td/table/tbody/tr[1]/td[2]/a/font',
                            now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a'
                            , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.select_test(cwb, '//*[@id="space"]/tr[2]/td/center/select', 0, 0, 0, '', '', now_whd, '', 0, '', '')

    def test_03(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[3]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"初中"')
        except:
            my_tools.my_logger.error('进入"初中"异常')
            message('进入"初中"异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/strong/a', now_whd
                            , 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[3]/tbody/tr/td/table/tbody/tr/td/div/a/img', now_whd, 0
                            , 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/div/a', now_whd, 0, 0,
                            0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td/b/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="space"]/tr[1]/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0, '', '', '', '',
                            0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a'
                            , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.select_test(cwb, '//*[@id="space"]/tr[2]/td/center/select', 0, 0, 0, '', '', now_whd, '', 0, '', '')

    def test_04(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[4]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"高中"')
        except:
            my_tools.my_logger.error('进入"高中"异常')
            message('进入"高中"异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/strong/a', now_whd
                            , 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[3]/tbody/tr/td/table/tbody/tr/td/div/a/img', now_whd, 0
                            , 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/div/a', now_whd, 0, 0,
                            0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td/b/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="space"]/tr[1]/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0, '', '', '', '',
                            0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a'
                            , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.select_test(cwb, '//*[@id="space"]/tr[2]/td/center/select', 0, 0, 0, '', '', now_whd, '', 0, '', '')
        my_tools.ele_clicks(cwb,
                            '//*[@id="header"]/div[3]/table/tbody/tr[1]/td/div[1]/table/tbody/tr/td/table/tbody/tr/td/a'
                            , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_05(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[5]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"小考"')
        except:
            my_tools.my_logger.error('进入"小考"异常')
            message('进入"小考"异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/strong/a', now_whd
                            , 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[3]/tbody/tr/td/table/tbody/tr/td/div/a/img', now_whd, 0
                            , 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/div/a', now_whd, 0, 0,
                            0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td/b/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a'
                            , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb,
                            '//*[@id="header"]/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/div/a',
                            now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb,
                            '//*[@id="header"]/div[3]/table/tbody/tr[1]/td/div[1]/table/tbody/tr/td/table/tbody/tr/td/a'
                            , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_06(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[6]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"中考"')
        except:
            my_tools.my_logger.error('进入"中考"异常')
            message('进入"中考"异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/strong/a', now_whd
                            , 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[3]/tbody/tr/td/table/tbody/tr/td/div/a/img', now_whd, 0
                            , 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/div/a', now_whd, 0, 0,
                            0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td/b/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="space"]/tr[1]/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0, '', '', '', '',
                            0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a'
                            , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.select_test(cwb, '//*[@id="space"]/tr[2]/td/center/select', 0, 0, 0, '', '', now_whd, '', 0, '', '')

    def test_07(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[7]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"高考"')
        except:
            my_tools.my_logger.error('进入"高考"异常')
            message('进入"高考"异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/strong/a', now_whd
                            , 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[3]/tbody/tr/td/table/tbody/tr/td/div/a/img', now_whd, 0
                            , 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/div/a', now_whd, 0, 0,
                            0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td/b/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="space"]/tr[1]/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0, '', '', '', '',
                            0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a'
                            , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.select_test(cwb, '//*[@id="space"]/tr[2]/td/center/select', 0, 0, 0, '', '', now_whd, '', 0, '', '')

    def test_08(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[8]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"中职"')
        except:
            my_tools.my_logger.error('进入"中职"异常')
            message('进入"中职"异常')
        my_tools.swich_handle(cwb, now_whd)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[2]/tbody/tr/td/table/tbody/tr/td/div/strong/a', now_whd
                            , 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/div[1]/table[3]/tbody/tr/td/table/tbody/tr/td/div/a/img', now_whd, 0
                            , 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/div/a', now_whd, 0, 0,
                            0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td/b/a', now_whd, 0, 0, 0,
                            '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb,
                            '//*[@id="header"]/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/div/a',
                            now_whd, 0, 0, 0, '', '', '', '', 0, '', '')
        my_tools.ele_clicks(cwb, '//*[@id="header"]/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a'
                            , now_whd, 0, 0, 0, '', '', '', '', 0, '', '')

    def test_09(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[9]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"阅读"')
        except:
            my_tools.my_logger.error('进入"阅读"异常')
            message('进入"阅读"异常')
        my_tools.close_hd_back(cwb, now_whd)

    def test_10(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[10]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"名师"')
        except:
            my_tools.my_logger.error('进入"名师"异常')
            message('进入"名师"异常')
        my_tools.close_hd_back(cwb, now_whd)

    def test_11(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[11]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"文言"')
        except:
            my_tools.my_logger.error('进入"文言"异常')
            message('进入"文言"异常')
        my_tools.close_hd_back(cwb, now_whd)

    def test_12(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[12]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"作文"')
        except:
            my_tools.my_logger.error('进入"作文"异常')
            message('进入"作文"异常')
        my_tools.close_hd_back(cwb, now_whd)

    def test_13(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[13]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"美文"')
        except:
            my_tools.my_logger.error('进入"美文"异常')
            message('进入"美文"异常')
        my_tools.close_hd_back(cwb, now_whd)

    def test_14(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[14]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"影音"')
        except:
            my_tools.my_logger.error('进入"影音"异常')
            message('进入"影音"异常')
        my_tools.close_hd_back(cwb, now_whd)

    def test_15(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[15]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"悦读"')
        except:
            my_tools.my_logger.error('进入"悦读"异常')
            message('进入"悦读"异常')
        my_tools.close_hd_back(cwb, now_whd)

    def test_16(self):
        now_whd = cwb.current_window_handle
        try:
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[16]/a'))
            time.sleep(2)
            my_tools.my_logger.info('进入"宝典"')
        except:
            my_tools.my_logger.error('进入"宝典"异常')
            message('进入"宝典"异常')
        my_tools.close_hd_back(cwb, now_whd)


if __name__ == "__main__":
    unittest.main()
    '//*[@id="header"]/div[1]/nav/ul/li[12]/a'
    # link