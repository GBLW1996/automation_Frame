import random
import time
import unittest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from fixdown_net.common.warning import message
# from fixdown_net.common.log import Logger
from fixdown_net.common.cappic import Cappic
from fixdown_net.pages.basepage import BasePage
import os
from selenium import webdriver
from fixdown_net.common.tools import PageTool
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
path = os.path.abspath('..') + '\\downloads\\'
pre_fs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
options.add_experimental_option('prefs', pre_fs)
cwb = webdriver.Chrome(chrome_options=options)
fix_net = BasePage(cwb)
# my_logger = Logger(logger='2').getlog()
my_tools = PageTool()

class WywNet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        fix_net.start_browser()

    @classmethod
    def tearDownClass(cls):
        fix_net.quit_browser()

    def test_01(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[1]/ul/li/a/img', now_whd, 1, 1, 0,
                            '//*[@id="main1k"]/div[3]/div[2]/div[2]/div[2]/div[1]/a', '', 'pc', 'alt', 0, '', '')

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[2]/dl[1]/dd/a', now_whd, 1, 0, 1,
                            '//*[@id="main1k"]/div[3]/div[2]/div[2]/div[2]/div[1]/a',
                            '//*[@id="zcgs"]/div[2]/ul/li[1]/a', '', '', 0, '', '')

    def test_03(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="main"]/div[2]/dl[2]/dd/a', now_whd, 1, 1, 1,
                            '//*[@id="main1k"]/div[3]/div[2]/div[2]/div[2]/div[1]/a',
                            '//*[@id="zcgs"]/div[2]/ul/li[1]/a', '', '', 0, '', '')

    def test_04(self):
        my_tools.wintowh(cwb, 0, 450)
        now_whd = cwb.current_window_handle
        for i in range(1, 6):
            my_tools.move_link(cwb, i, i+1, i, i+1, "/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/a[{}]/img",
                               "/html/body/div[2]/div[3]/div[1]/div[1]/div[1]/ul/li[{}]/a/img", "", True, now_whd, True)

    def test_05(self):
        my_tools.wintowh(cwb, 0, 450)
        now_whd = cwb.current_window_handle
        ele = cwb.find_element_by_xpath('//div[@id="news"]/ul/li[1]')
        ActionChains(cwb).move_to_element(ele).perform()
        my_tools.jump_link(cwb, 1, 7, "/html/body/div[2]/div[3]/div[2]/div/div[2]/ul[1]/li[{}]/a", "", True, now_whd, ""
                           , False, True, True)
        my_tools.jump_link(cwb, 8, 14, "/html/body/div[2]/div[3]/div[2]/div/div[2]/ul[1]/li[{}]/a", "", True, now_whd,
                           "", False, True, True)

        ele = cwb.find_element_by_xpath('//div[@id="news"]/ul/li[2]')
        ActionChains(cwb).move_to_element(ele).perform()
        my_tools.jump_link(cwb, 1, 7, "/html/body/div[2]/div[3]/div[2]/div/div[2]/ul[2]/li[{}]/a", "", True, now_whd, ""
                           , False, True, True)
        my_tools.jump_link(cwb, 8, 14, "/html/body/div[2]/div[3]/div[2]/div/div[2]/ul[2]/li[{}]/a", "", True, now_whd,
                           "", False, True, True)

        ele = cwb.find_element_by_xpath('//div[@id="news"]/ul/li[3]')
        ActionChains(cwb).move_to_element(ele).perform()
        my_tools.jump_link(cwb, 1, 7, "/html/body/div[2]/div[3]/div[2]/div/div[2]/ul[3]/li[{}]/a", "", True, now_whd, ""
                           , False, True, True)
        my_tools.jump_link(cwb, 8, 14, "/html/body/div[2]/div[3]/div[2]/div/div[2]/ul[3]/li[{}]/a", "", True, now_whd,
                           "", False, True, True)

        ele = cwb.find_element_by_xpath('//div[@id="news"]/ul/li[4]')
        ActionChains(cwb).move_to_element(ele).perform()
        my_tools.jump_link(cwb, 1, 7, "/html/body/div[2]/div[3]/div[2]/div/div[2]/ul[4]/li[{}]/a", "", True, now_whd, ""
                           , False, True, True)
        my_tools.jump_link(cwb, 8, 14, "/html/body/div[2]/div[3]/div[2]/div/div[2]/ul[4]/li[{}]/a", "", True, now_whd,
                           "", False, True, True)

    def test_06(self):
        my_tools.wintowh(cwb, 0, 450)
        now_whd = cwb.current_window_handle
        for i in range(1, 4):
            my_tools.move_link(cwb, i, i + 1, i, i + 1,
                               "/ html / body / div[2] / div[3] / div[3] / div[1] / div[1] / ul / li[{}]",
                               "/ html / body / div[2] / div[3] / div[3] / div[1] / div[2] / div[{}] / p[4] / a[2]", "",
                               True, now_whd, True)

    def test_07(self):
        my_tools.wintowh(cwb, 0, 450)
        now_whd = cwb.current_window_handle
        for i in range(1, 3):
            my_tools.move_link(cwb, i, i + 1, i, i + 1,
                               "/ html / body / div[2] / div[3] / div[3] / div[2] / div[3] / div[2] / a[{}]",
                               "/ html / body / div[2] / div[3] / div[3] / div[2] / div[1] / div / a[{}]", "",
                               True, now_whd, True)

    def test_08(self):
        my_tools.wintowh(cwb, 0, 450)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 2, 4, "/ html / body / div[2] / div[3] / div[1] / div[{}] / a", "target", False, now_whd
                           , '', True, True, True)

    def test_09(self):
        # 电脑软件排行榜
        my_tools.wintowh(cwb, 0, 1050)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 12,
                           "/ html / body / div[2] / div[4] / div[2] / div / div[2] / div[2] / dl[{}] / dt / a", "",
                           True, now_whd, "pc", False, True, False)

    def test_10(self):
        my_tools.wintowh(cwb, 0, 1050)
        now_whd = cwb.current_window_handle
        # my_tools.jump_link(cwb, 1, 16, "/ html / body / div[2] / div[4] / div[2] / div / div[1] / dl[{}] / dt / a", "",
        #                    True, now_whd, "", False, True, True)
        my_tools.jump_link_pg(cwb, 1, 16, '/ html / body / div[2] / div[4] / div[2] / div / div[1] / dl[{}] / dt / a',
                              now_whd, '//*[@id="main1k"]/div[2]/div[1]/div[3]/div/a', '//div[@class="hd"]/p/a')

    def test_11(self):
        my_tools.wintowh(cwb, 0, 1050)
        now_whd = cwb.current_window_handle
        for i in range(1, 16):
            my_tools.jump_link(cwb, 1, 5,
                               "/ html / body / div[2] / div[4] / div[2] / div / div[1] / dl[%d] / dd[{}] / a" % (i),
                               "target", False, now_whd, "", True, True, True)

    def test_12(self):
        my_tools.wintowh(cwb, 0, 1050)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 9, "/ html / body / div[2] / div[5] / div[2] / div[2] / div[2] / dl[{}] / dt / a", ""
                           , True, now_whd, "", False, True, True)

    def test_13(self):
        my_tools.wintowh(cwb, 0, 1600)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 13, "/ html / body / div[2] / div[5] / div[2] / div[1] / ul / li[{}] / p[1] / a",
                           "target", False, now_whd, "", True, True, True)
        ele = cwb.find_element_by_xpath('// *[ @ id = "z2"]')
        ActionChains(cwb).move_to_element(ele).perform()
        my_tools.jump_link(cwb, 1, 13, "/ html / body / div[2] / div[5] / div[3] / div[1] / ul / li[{}] / p[2] / a", "",
                           True, now_whd, "", False, True, True)

    def test_14(self):
        my_tools.wintowh(cwb, 0, 1900)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 13, '// *[ @ id = "ios"] / div[2] / div[1] / ul / li[{}] / p[2] / a', "", True,
                           now_whd, "", False, True, True)

    def test_15(self):
        my_tools.wintowh(cwb, 0, 1900)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 9, "/html/body/div[2]/div[6]/div[2]/div[2]/div[2]/dl[{}]/dt/a", "", True, now_whd, ""
                           , False, True, True)

    def test_16(self):
        # 每个移入元素随机选一个进入
        my_tools.wintowh(cwb, 0, 2500)
        now_whd = cwb.current_window_handle
        for i in range(1, 6):
            num1, num2 = my_tools.random_two_num(3, 11)
            ele = cwb.find_element_by_xpath('/ html / body / div[2] / div[7] / div[1] / ul / li[{}]'.format(i))
            ActionChains(cwb).move_to_element(ele).perform()
            BasePage(cwb).wait(10)
            xp = "/ html / body / div[2] / div[7] / div[2] / div[{}] / ul[{}] / li[{}] / a".format(i, num1, num2)
            str1 = cwb.find_element_by_xpath(xp).text
            my_tools.jump_pg(cwb, xp, now_whd, True, True, str1, "")

    def test_17(self):
        my_tools.wintowh(cwb, 0, 3000)
        now_whd = cwb.current_window_handle
        for i in range(1, 5):
            ran_num = random.randint(1, 50)
            ele = cwb.find_element_by_xpath('/html/body/div[2]/div[8]/div[1]/ul/li[{}]'.format(i))
            ActionChains(cwb).move_to_element(ele).perform()
            BasePage(cwb).wait(10)
            xp = '/ html / body / div[2] / div[8] / div[2] / div[{}] / ul / li[{}] / a'.format(i, ran_num)
            str1 = cwb.find_element_by_xpath(xp).text
            my_tools.jump_pg(cwb, xp, now_whd, True, True, str1, "")

    def test_18(self):
        my_tools.wintowh(cwb, 0, 3200)
        now_whd = cwb.current_window_handle
        my_tools.jump_link(cwb, 1, 12, '/html/body/div[2]/div[9]/div[2]/ul/li[{}]/a', '', False, now_whd, '', False,
                           False, True)

    def test_19(self):
        now_whd = cwb.current_window_handle
        my_tools.jump_without_hd(cwb, 2, 6, '/html/body/div[1]/div[3]/div/a[{}]', now_whd)

    def test_20(self):
        pass


if __name__ == "__main__":
    unittest.main()