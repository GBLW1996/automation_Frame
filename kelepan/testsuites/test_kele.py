import random
import unittest
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from kelepan.common.warning import message
# from kelepan.common.log import Logger
from kelepan.common.cappic import Cappic
from kelepan.pages.basepage import BasePage
from selenium.webdriver.support.select import Select
import os
from kelepan.common.tools import PageTool
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
        my_tools.ele_clicks(cwb, '/html/body/div[3]/div/ul/li/a', now_whd, is_back=1)
        my_tools.ele_clicks(cwb, '/html/body/div[4]/div/div[1]/a', now_whd, is_back=1)
        my_tools.ele_clicks(cwb, '//*[@id="section-about"]/div/div/div[2]/div/a', now_whd, is_back=1)
        my_tools.ele_clicks(cwb, '//*[@id="section-pricing"]/div/div[2]/div/div/a', now_whd, is_back=1)


if __name__ == "__main__":
    unittest.main()