import random
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from drv5.common.warning import message
# from drv5.common.log import Logger
from drv5.common.cappic import Cappic
from drv5.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from drv5.common.tools import PageTool
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
        my_tools.test_input(cwb, ['QQ', '微信', 'ps', '钉钉', '陌陌'], '//*[@id="keyword"]', now_whd)
        BasePage(cwb).back()
        my_tools.ele_clicks(cwb, '//*[@id="weektop"]/ul/li/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="monthtop"]/ul/li/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="zimu"]/p/a', now_whd, is_back=1)


if __name__ == "__main__":
    unittest.main()
    '//*[@id="zimu"]/p/a'