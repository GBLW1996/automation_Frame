import random
import time
import unittest

import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from bz_net.common.warning import message
# from bz_net.common.log import Logger
from te18183_com.common.cappic import Cappic
from bz_net.pages.basepage import BasePage
import os
from selenium import webdriver
from bz_net.common.tools import PageTool
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
path = os.path.abspath('..') + '\\downloads\\'
pre_fs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
options.add_experimental_option('prefs', pre_fs)
cwb = webdriver.Chrome(chrome_options=options)
bz = BasePage(cwb)
# my_logger = Logger(logger='2').getlog()
my_tools = PageTool()


class WywNet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        bz.start_browser()

    @classmethod
    def tearDownClass(cls):
        # bz.quit_browser()
        pass

    def test_01(self):
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '', True, 'alt', '首页 ', 'logo', False, False, '//*[@id="newlogo"]', True, False, now_whd
                           , False, False)

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '//*[@id="nav"]/ul/li/a', False, '', "首页", '右上角超链接', True, True, '', True, False,
                           now_whd, False, False)

    def test_03(self):
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '', True, 'class', '首页', '第一页滑动div', False, False, '//*[@id="header-wrapper"]/div[5]',
                           False, False, now_whd, False, False)

    def test_04(self):
        my_tools.wintowh(cwb, 0, 700)
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '//*[@id="intro"]/div/div/img', True, "alt", '首页', '企业价值观图片', True, True, '', True,
                           False, now_whd, False, False)

    def test_05(self):
        # 滑动链接
        my_tools.wintowh(cwb, 0, 700)
        now_whd = cwb.current_window_handle
        res = cwb.find_elements_by_xpath('//*[@id="home_content_wrap_1"]/li/a')
        res1 = cwb.find_elements_by_xpath('//*[@id="home_content_wrap_1"]/li/a/span[3]')
        my_tools.find_eles(cwb, '', True, 'href', '首页', '固定滚动条', False, False, '//*[@id="dongtai"]/div/div[2]/a/span[3]', False, True, now_whd, False, False)
        list_1 = []
        list_2 = []
        for i in res:
            list_1.append(i.get_attribute('href'))
        for i in res1:
            list_2.append(i.text)
        for i in list_1:
            response = requests.get(i)
            if "20" in str(response.status_code):
                my_tools.my_logger.info('首页滚动链接{}返回码正常，共{}个，目前第{}个'.format(list_2[list_1.index(i)], len(list_1), list_1.index(i)+1))
            else:
                my_tools.my_logger.error('首页滚动链接{}返回码异常，共{}个，目前第{}个'.format(list_2[list_1.index(i)], len(list_1), list_1.index(i)+1))
                message('首页滚动链接{}返回码异常，共{}个，目前第{}个'.format(list_2[list_1.index(i)], len(list_1), list_1.index(i)+1))

    def test_06(self):
        my_tools.wintowh(cwb, 0, 1350)
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '', False, '', '首页', '第三页', False, False, '//*[@id="intro"]/div[1]/div/p[1]/span', True,
                           False, now_whd, False, False)

    def test_07(self):
        my_tools.wintowh(cwb, 0, 1350)
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="intro"]/div[2]/ul/li/div/a/span/img', now_whd, False, True, False, '', '', ''
                            , True, 'alt')

    def test_08(self):
        my_tools.wintowh(cwb, 0, 1950)
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '', True, 'title', '首页', '第四页图片', False, False, '//*[@id="features"]/div/img[1]', True,
                           False, now_whd, False, False)

    def test_09(self):
        my_tools.wintowh(cwb, 0, 2550)
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '', True, 'title', '首页', '第五页图片', False, False, '//*[@id="intro"]/div/img[1]', True,
                           False, now_whd, False, False)

    def test_10(self):
        my_tools.wintowh(cwb, 0, 3200)
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '//*[@id="features"]/div[1]/div/p/span', False, '', "首页", '六七八页文字', False, True, ''
                           , True, False, now_whd, False, False)

    def test_11(self):
        my_tools.wintowh(cwb, 0, 3200)
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '//*[@id="features"]/div[2]/div[1]/ul/li/a/img', True, 'title', '首页', '合作伙伴', True, True
                           , '', True, True, now_whd, False, False)

    def test_12(self):
        my_tools.wintowh(cwb, 0, 3900)
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '//*[@id="features"]/ul/li/div/span', True, 'class', '首页', '福利', True, True, '', False,
                           False, now_whd, False, False)

    def test_13(self):
        my_tools.wintowh(cwb, 0, 3900)
        now_whd = cwb.current_window_handle
        my_tools.jump_in_current(7, 8, cwb, '/html/body/div[1]/div[{}]/div/div/a', False, True, 'class')
        # my_tools.jump_eles_in_current(cwb, '//*[@id="features"]/a', False, True, 'href')

    def test_14(self):
        my_tools.wintowh(cwb, 0, 4700)
        now_whd = cwb.current_window_handle
        my_tools.find_eles(cwb, '//*[@id="features"]/ul/li/a/div', True, 'class', '首页', '联系方式、位置', True, True, '', False
                           , False, now_whd, False, False)

    def test_15(self):
        my_tools.wintowh(cwb, 0, 4750)
        now_whd = cwb.current_window_handle
        my_tools.jump_in_current(8, 9, cwb, '/html/body/div[1]/div[{}]/div/div/a', False, True, 'class')

    def test_16(self):
        my_tools.wintowh(cwb, 0, 4850)
        now_whd = cwb.current_window_handle
        for i in range(2, 8):
            # my_tools.jump_in_current(cwb, '//*[@id="features"]/div[1]/span/a[{}]'.format(i), False, True, 'class')
            my_tools.jump_in_current(1, 2, cwb, '//*[@id="features"]/div[{}]/span/a[%d]' % (i), False, True, 'class')
        my_tools.find_eles(cwb, '', False, '', '首页', '底部信息', False, False, '//*[@id="features"]/div[1]/span/a[1]', True,
                           False, now_whd, False, False)
        my_tools.find_eles(cwb, '', False, '', '首页', '底部信息', False, False, '//*[@id="features"]/div[2]/span', True,
                           False, now_whd, False, False)
        my_tools.find_eles(cwb, '', False, '', '官网', '底部信息', False, False, '//*[@id="features"]/div[3]/span/a', True,
                           False, now_whd, False, False)
        my_tools.ele_clicks(cwb, '//*[@id="features"]/div[4]/span/a', now_whd, False, False, False, '', '', '', False,
                            '')
        my_tools.find_eles(cwb, '', False, 'id', '首页', '返回顶部div', True, False, '//*[@id="scrollTop"]', False, False,
                           now_whd, False, False)
        try:
            cwb.find_element_by_xpath('//*[@id="scrollTop"]').click()
            my_tools.my_logger.info('首页回到顶部元素正常点击')
        except:
            my_tools.my_logger.error('首页回到顶部元素不能点击')
            # message('首页回到顶部元素不能点击')

    def test_17(self):
        # 发展历程
        try:
            cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
            if '百助' in cwb.title:
                my_tools.my_logger.info('跳转到”发展历程“')
            else:
                my_tools.my_logger.info('跳转到”{}“,注意'.format(cwb))
        except:
            my_tools.my_logger.error('发展历程跳转异常')
            message('发展历程跳转异常')

    def test_18(self):
        cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
        now_whd = cwb.current_window_handle
        my_tools.jump_in_current(1, 4, cwb, '//*[@id="introduction"]/a[{}]', False, True, 'class')

    def test_19(self):
        cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
        now_whd = cwb.current_window_handle
        my_tools.click_a(cwb, '//*[@id="page-wrapper"]/div[3]/div/div[2]/div/dl/dd/div[3]/div[1]/a', False, '', '发展历程')
        my_tools.find_eles(cwb, '//*[@id="page-wrapper"]/div[3]/div/div[2]/div/dl/dd/div/div/div/div/img', True, 'class'
                           , '发展历程', '图片', True, True, '', False, False, now_whd, False, False)
        # my_tools.ele_clicks(cwb, '//*[@id="newsLink"]/a', now_whd, False, False, False, '', '', '', True, 'href')
        my_tools.find_eles1(cwb, '//*[@id="newsLink"]/a', True, 'href', '发展历程', '超链接', True, True, '', True, True,
                           now_whd, False, False)

    def test_20(self):
        cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/a').click()
        list_ran = ["CEO", "你好", "北京", "中国", "马鞍山", "程磊", "哈哈"]
        keys = list_ran[random.randint(0, 6)]
        cwb.find_element_by_xpath('//*[@id="intro-wrapper"]/ul/li[1]/form/input[6]').send_keys(keys+"\n")
        time.sleep(2)
        res = my_tools.judgestr(keys, cwb.title)
        if res:
            my_tools.my_logger.info('新闻动态模块搜索框正常')
        else:
            my_tools.my_logger.info('新闻动态模块搜索框异常')
        BasePage(cwb).back()
        time.sleep(2)

    def test_21(self):
        cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/a').click()
        sum_txt = cwb.find_element_by_xpath('//*[@id="pages"]/a[12]').text
        sum_num = int(sum_txt)
        now_whd = cwb.current_window_handle
        for i in range(sum_num-1):
            my_tools.ele_clicks(cwb, '//*[@id="intro-wrapper"]/ul/li/div/a[1]', now_whd, False, False, False, '', '', ''
                                , True, 'href')
            cwb.find_element_by_xpath('//*[@id="pages"]/a[13]').click()

    def test_22(self):
        cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[4]/a').click()
        now_whd = cwb.current_window_handle
        my_tools.find_eles1(cwb, '//*[@id="intro-wrapper"]/ul/li/span/img', True, 'alt', '人在百助', '大图', True, True, '',
                           True, False, now_whd, False, False)
        my_tools.find_eles1(cwb, '//*[@id="intro-wrapper"]/ul/li[2]/div/span/img', True, 'alt', '人在百助', '小图', True,
                            True, '', True, False, now_whd, False, False)

    def test_23(self):
        cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[5]/a').click()
        time.sleep(2)
        now_whd = cwb.current_window_handle
        my_tools.click_a(cwb, '//*[@id="intro-wrapper"]/div[3]/div/div/p/span[1]', False, '', '加入百助')

    def test_24(self):
        cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[5]/a').click()
        for i in range(1, 8):
            a_l = cwb.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/ul/li[{}]/a'.format(i))
            cwb.execute_script("arguments[0].click();", a_l)
            time.sleep(2)
            p_tt = cwb.title
            if p_tt:
                my_tools.my_logger.info('加入百助模块‘{}’跳转成功'.format(p_tt))
            else:
                my_tools.my_logger.error('加入百助模块‘{}’跳转异常'.format(p_tt))
                #     # message('加入百助模块‘{}’跳转成功'.format(a_txt))
            my_tools.click_a(cwb, '//*[@id="intro-wrapper"]/div[3]/div/div/p/span[1]', False, '', '加入百助')

    def test_25(self):
        cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[6]/a').click()
        res = cwb.find_elements_by_xpath('//*[@id="header-wrapper"]/div[4]/div/div/div[1]/div')
        for i in res:
            cwb.execute_script("arguments[0].click();", i)
            time.sleep(1)
            try:
                div = cwb.find_element_by_xpath('//*[@id="header-wrapper"]/div[4]/div[{}]/div/div[2]'.format(res.index(i)+1))
                my_tools.my_logger.info('管理团队模块第{}张照片详细介绍正常显示'.format(res.index(i)+1))
            except:
                my_tools.my_logger.error('管理团队模块第{}张照片详细介绍显示异常'.format(res.index(i)+1))
                message('管理团队模块第{}张照片详细介绍显示异常'.format(res.index(i)+1))
            r1 = cwb.find_element_by_xpath('//*[@id="header-wrapper"]/div[4]/div[{}]/div/div[2]/div[1]'.format(res.index(i)+1))
            cwb.execute_script("arguments[0].click();", r1)
            time.sleep(1)

    def test_26(self):
        now_whd = cwb.current_window_handle
        cwb.find_element_by_xpath('//*[@id="nav"]/ul/li[7]/a').click()
        my_tools.find_eles(cwb, '', True, 'src', '联系我们', '图片1', True, False, '//*[@id="intro-wrapper"]/div/div[1]/img',
                           False, False, now_whd, False, False)
        my_tools.find_eles(cwb, '//*[@id="intro-wrapper"]/div/div/div/img', True, 'src', '联系我们', '第二模块图片', True, True, ''
                           , False, False, now_whd, False, False)
        my_tools.find_eles(cwb, '//*[@id="intro-wrapper"]/div/div/p[1]', True, 'src', '联系我们', '第二块模块文字', True, True, ''
                           , False, False, now_whd, False, False)
        my_tools.find_eles(cwb, '//*[@id="intro-wrapper"]/div/div/p[2]', True, 'src', '联系我们', '第二块模块文字', True, True, ''
                           , False, False, now_whd, False, False)
        my_tools.find_eles(cwb, '//*[@id="intro-wrapper"]/div/div/a[1]/p', True, 'src', '联系我们', '第二块模块文字', True, True, ''
                           , False, False, now_whd, False, False)
        my_tools.find_eles(cwb, '//*[@id="intro-wrapper"]/div/div/a[2]/p', True, 'src', '联系我们', '第二块模块文字', True, True,
                           '', False, False, now_whd, False, False)
        my_tools.find_eles(cwb, '', True, 'src', '联系我们', '地图模块', True, False, '//*[@id="intro-wrapper"]/div/div[5]/div/a/img', False, True, now_whd, False, False)


if __name__ == "__main__":
    unittest.main()