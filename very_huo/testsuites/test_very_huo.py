import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from very_huo.common.warning import message
# from very_huo.common.log import Logger
from very_huo.common.cappic import Cappic
from very_huo.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from selenium import webdriver
from very_huo.common.tools import PageTool
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
        my_tools.test_input(cwb, ["QQ", "安卓", "明日之后", "一人之下"], '//*[@id="bdcsMain"]', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[2]/div[1]/div/div[2]/div/a', now_whd, is_judge_link=1)
        my_tools.ele_clicks(cwb, '//*[@id="icon_lbBox"]/li/a', now_whd, attr='href')
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/a', now_whd, is_judge_link=1)
        my_tools.wintowh(cwb, 0, 400)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="fy-rolling1"]/ol/li'))+1):      # 轮播图
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="fy-rolling1"]/ol/li[{}]'.format(i)))
            my_tools.ele_clicks(cwb, '//*[@id="fy-rolling1"]/div/ul/li[{}]/a/img'.format(i), now_whd, is_judge_link=1,
                                attr='alt')
        # 最新资讯
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div[2]/dl[2]/dd/a', now_whd, is_judge_link=1, is_back=1)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[1]/div[2]/ul/li/a', now_whd, is_judge_link=1, is_back=1)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[2]/div/div[1]/a'))+1):
            my_tools.move_in(cwb, '/html/body/div[5]/div[2]/div/div[1]/a[{}]'.format(i))
            my_tools.ele_clicks(cwb, '/html/body/div[5]/div[2]/div/div[2]/ul[{}]/li/a'.format(i), now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[1]/ul/li/a/span', now_whd, is_judge_link=1)  # 热门手游
        my_tools.ele_clicks(cwb, '/html/body/div[5]/div[3]/div[2]/a/strong', now_whd, is_judge_link=1)  # 专题推荐

    def test_02(self):
        # 常用软件
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1000)
        my_tools.ele_clicks(cwb, '//*[@id="recnew-box"]/div/ul/li/div/p[1]/a', now_whd, is_judge_link=1)

    def test_03(self):
        # 最热安卓软件/游戏
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1500)
        my_tools.ele_clicks(cwb, '//*[@id="az_soft"]/div/ul/li/a/p', now_whd, is_judge_link=1)

    def test_04(self):
        # 最热苹果软件/游戏
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 1900)
        my_tools.ele_clicks(cwb, '//*[@id="pg-box"]/div[2]/div/div/ul/li/a/p', now_whd, is_judge_link=1)

    def test_05(self):
        # 游戏Game
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2300)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="Game-box"]/div[1]/div/a'))+1):
            my_tools.move_in(cwb, '//*[@id="Game-box"]/div[1]/div/a[{}]'.format(i))
            my_tools.ele_clicks(cwb, '//*[@id="Game-box"]/div[2]/div[{}]/div/ul/li/div/a'.format(i), now_whd,
                                is_judge_link=1)

    def test_06(self):
        # 安卓软件/游戏 苹果软件/游戏 电脑软件/游戏
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2750)
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div/div/strong/a', now_whd, is_back=1)
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div/dl/dd/a', now_whd, is_judge_link=1)
        # 友情链接
        my_tools.wintowh(cwb, 0, 2950)
        my_tools.ele_clicks(cwb, '/html/body/div[11]/p/a', now_whd)

    def test_07(self):
        # 电脑软件
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="li3"]/a', now_whd, '电脑软件')
        my_tools.swich_handle(cwb, now_whd)
        my_tools.random_check(cwb, '//*[@id="recnew-box"]/div/ul/li/div/p/a', now_whd)  # 新品推荐 最新更新
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[4]/div[position()>1]'))+1):  # 热门分类
            my_tools.random_check(cwb, '/html/body/div[4]/div[{}]/div[2]/a'.format(i+1), now_whd)
            my_tools.random_check(cwb, '/html/body/div[4]/div[{}]/ul/li/p/a'.format(i+1), now_whd, is_judge_link=1)
            my_tools.random_check(cwb, '/html/body/div[4]/div[{}]/div[3]/a/img'.format(i+1), now_whd, is_judge_link=1, attr='alt')
            my_tools.my_logger.info('"{}"随机完成'.format(cwb.find_element_by_xpath('/html/body/div[4]/div[{}]/div[1]/a'.format(i+1)).text))

    def test_08(self):
        # 安卓下载
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="li4"]/a', now_whd, '安卓下载')
        my_tools.random_check(cwb, '/html/body/div[3]/ul/li/a/p', now_whd, is_judge_link=1, is_back=1)
        my_tools.random_check(cwb, '//*[@id="commend"]/dl/dd/p/span/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/p/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[3]/div[2]/ul[1]/li/a[2]', now_whd, attr='href')
        my_tools.move_in(cwb, '/html/body/div[4]/div[2]/div[3]/div[1]/a[2]')
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[3]/div[2]/ul[2]/li/a[2]', now_whd, attr='href')
        my_tools.random_check(cwb, '/html/body/div[4]/div[3]/div[1]/ul/li/a/span', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[3]/div[2]/a/strong', now_whd, is_judge_link=1)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="rjdown"]/div[2]/div/div[1]/p/span'))+1):  # 安卓软件
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="rjdown"]/div[2]/div/div[1]/p/span[{}]'.format(i)))
            time.sleep(1)
            my_tools.random_check(cwb, '//*[@id="rjdown"]/div[2]/ul[{}]/li/a/span'.format(i), now_whd, is_judge_link=1)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="soft_tab1_0"]/div[2]/div/div[1]/p/span'))+1):  # 安卓游戏
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="soft_tab1_0"]/div[2]/div/div[1]/p/span[{}]'.format(i)))
            time.sleep(1)
            my_tools.random_check(cwb, '//*[@id="soft_tab1_0"]/div[2]/ul[{}]/li/a/span'.format(i), now_whd, is_judge_link=1)

    def test_09(self):
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="li5"]/a', now_whd, '苹果应用')
        my_tools.random_check(cwb, '/html/body/div[3]/ul/li/a/p', now_whd, is_judge_link=1, is_back=1)
        my_tools.random_check(cwb, '//*[@id="commend"]/dl/dd/p/span/a', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/p/a', now_whd, is_judge_link=1)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/a'))+1):
            my_tools.move_in(cwb, '/html/body/div[4]/div[2]/div[3]/div[1]/a[{}]'.format(i))
            my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[3]/div[2]/ul[{}]/li/a[2]'.format(i), now_whd, attr='href')
        my_tools.random_check(cwb, '/html/body/div[4]/div[3]/div[1]/ul/li/a/span', now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[3]/div[2]/a/strong', now_whd, is_judge_link=1)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="rjdown"]/dd/div/div[1]/p/span')) + 1):  # 苹果软件
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="rjdown"]/dd/div/div[1]/p/span[{}]'.format(i)))
            time.sleep(1)
            my_tools.random_check(cwb, '//*[@id="rjdown"]/dd/ul[{}]/li/a/span'.format(i), now_whd, is_judge_link=1)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="soft_tab1_0"]/dd/div/div[1]/p/span')) + 1):  # 苹果游戏
            my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="soft_tab1_0"]/dd/div/div[1]/p/span[{}]'.format(i)))
            time.sleep(1)
            my_tools.random_check(cwb, '//*[@id="soft_tab1_0"]/dd/ul[{}]/li/a/span'.format(i), now_whd, is_judge_link=1)

    def test_10(self):
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="li14"]/a', now_whd, '电脑游戏')
        my_tools.random_check(cwb, '/html/body/div[3]/div[1]/ul/li/a/p', now_whd, is_judge_link=1, is_back=1)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[4]/div[1]/div[1]/a'))+1):  # 游戏Game
            my_tools.move_in(cwb, '/html/body/div[4]/div[1]/div[1]/a[{}]'.format(i))
            my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[{}]/div[1]/ul/li/div/a'.format(i), now_whd, is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[4]/div[2]/div[1]/div[2]/div/ul/li/div[1]/a', now_whd, is_judge_link=1, is_back=1)
        my_tools.random_check(cwb, '/html/body/div[3]/div[1]/ul/li/a/p', now_whd, is_judge_link=1, is_back=1)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[5]/div[1]/div/a')) + 1):  # 游戏辅助
            my_tools.move_in(cwb, '/html/body/div[5]/div[1]/div/a[{}]'.format(i))
            my_tools.random_check(cwb, '/html/body/div[5]/div[2]/div[{}]/div[1]/ul/li/div/a'.format(i), now_whd,
                                  is_judge_link=1)
        my_tools.random_check(cwb, '/html/body/div[5]/div[2]/div[1]/div[2]/div/ul/li/div[1]/a', now_whd,
                              is_judge_link=1, is_back=1)
        my_tools.random_check(cwb, '/html/body/div[6]/div[2]/div/div/ul/li/a/strong', now_whd, is_back=1)

    def test_11(self):
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="li16"]/a', now_whd, '资讯教程')
        my_tools.random_check(cwb, '/html/body/div/div/ul/li/a/section/h3', now_whd, is_judge_link=1)

    def test_12(self):
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="li17"]/a', now_whd, '排行榜')
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[1]'))+1):
            my_tools.random_check(cwb, '/html/body/div[3]/div[2]/div[{}]/div[2]/ul/li/a[1]/strong'.format(i), now_whd, is_judge_link=1)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[4]/div/div[1]'))+1):
            my_tools.random_check(cwb, '/html/body/div[3]/div[4]/div[{}]/div[2]/ul/li/a[1]/strong'.format(i), now_whd, is_judge_link=1)
        for i in range(1, len(cwb.find_elements_by_xpath('/html/body/div[3]/div[6]/div/div[1]'))+1):
            my_tools.random_check(cwb, '/html/body/div[3]/div[6]/div[{}]/div[2]/ul/li/a[1]/strong'.format(i), now_whd)
        my_tools.random_check(cwb, '/html/body/div[3]/div[8]/div/ul/li/a', now_whd, is_judge_link=1)

    def test_13(self):
        now_whd = cwb.current_window_handle
        my_tools.switch_frame(cwb, '//*[@id="li32"]/a', now_whd, '专题')
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="mCnt"]/p'))+1):
            my_tools.random_check(cwb, '//*[@id="mCnt"]/p[{}]/a/span'.format(i), now_whd, is_judge_link=1)


if __name__ == "__main__":
    unittest.main()
    '//*[@id="mCnt"]/p[{}]/a/span'