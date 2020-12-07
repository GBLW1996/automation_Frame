import random
import time
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lanzouyun.common.warning import message
# from lanzouyun.common.log import Logger
from lanzouyun.common.cappic import Cappic
from lanzouyun.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from lanzouyun.common.tools import PageTool
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
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/div[2]/div/a', now_whd, is_back=1)
        my_tools.ele_clicks(cwb, '/html/body/div[10]/div/div[4]/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[12]/div[2]/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[14]/div[2]/a', now_whd)
        my_tools.ele_clicks(cwb, '/html/body/div[16]/div[1]/div/a', now_whd)


if __name__ == "__main__":
    unittest.main()
