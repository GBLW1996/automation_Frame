from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from wyw_net.common import some_tools
from wyw_net.common.basepage import *
from wyw_net.common.cappic import *
from wyw_net.common.log import Logger
# from wyw_net.common.certificateDll import *

options = webdriver.ChromeOptions()
path = os.path.abspath('..') + '\\downloads\\'
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
options.add_experimental_option('prefs', prefs)
cwb = webdriver.Chrome(chrome_options=options)

wyw_hm = BasePage(cwb)
mylogger = Logger(logger='2').getlog()


class WywNet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        wyw_hm.start_browser()

    @classmethod
    def tearDownClass(cls):
        wyw_hm.quit_browser()

    def test01(self):
        time.sleep(2)
        monsterpagetxt = cwb.find_element_by_xpath("/html/body/div[1]/div/h1/a").text
        now_winhd = cwb.current_window_handle
        if monsterpagetxt == "玩一玩游戏网":
            mylogger.info("wyw主页logo正常")
        else:
            mylogger.error("wyw主页logo出错")
            message("wyw主页logo出错")
        some_tools.ele_clicks(cwb, '/html/body/div[1]/div/div/ul/li/a', now_winhd, 0, 1, 0, '', '', '', 'title', 0, '')
        time.sleep(2)

    def test02(self):
        now_winhd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[1]/ul/li/a', now_winhd, False, True, False, '', '', '',
                              'title', False, '')
        time.sleep(2)
        cwb.find_element_by_xpath('//*[@id="bdcs-search-form-input"]').send_keys("超级玛丽\n")
        some_tools.swich_handle(cwb, now_winhd)
        try:
            cwb.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/a/img")
        except:
            mylogger.error("wyw首页搜索框错误")
            message("wyw首页搜索框错误")
        time.sleep(1)
        some_tools.close_hd_back(cwb, now_winhd)

    def test03(self):
        # 热门
        now_winhd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[2]/div[1]/ul/li/a', now_winhd, True, True, True,
                              '//*[@id="pc_download_link"]', '//*[@id="android_download_link"]', '', 'title', False,
                              '/html/body/div[3]/div[2]/div[1]/ul/li[1]')
        # 专区
        some_tools.move_in(cwb, '/html/body/div[3]/div[2]/div[1]/ul/li[2]')
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[2]/div[2]/div[2]/ul/li/a', now_winhd, True, True, True,
                              '//*[@id="pc_download_link"]', '//*[@id="android_download_link"]', '', 'title', False,
                              '/html/body/div[3]/div[2]/div[1]/ul/li[2]')

    def test04(self):
        now_whd = cwb.current_window_handle
        some_tools.jump_tt_test_large_bt(cwb, 2, 14, "/ html / body / div[3] / div[3] / ul / li[{}] / a", now_whd)

    def test05(self):
        now_whd = cwb.current_window_handle
        cwb.find_element_by_xpath("/ html / body / div[3] / div[4] / a / img").click()
        time.sleep(2)
        some_tools.swich_handle(cwb, now_whd)
        tt = cwb.title
        res = some_tools.page_tt_code(tt)
        if res:
            mylogger.info("wyw首页第五行长图超链接跳转正常")
        else:
            mylogger.error("wyw首页第五行长图超链接跳转异常")
            message("wyw首页第五行长图超链接跳转异常")
        some_tools.close_hd_back(cwb, now_whd)

    def test06(self):
        # 轮播图
        now_whd = cwb.current_window_handle
        some_tools.wintowh(cwb, 0, 500)
        for i in range(1, len(cwb.find_elements_by_xpath('//*[@id="slideBox"]/div[1]/ul/li'))+1):
            some_tools.move_in(cwb, '//*[@id="slideBox"]/div[1]/ul/li[{}]'.format(i))
            time.sleep(2)
            some_tools.ele_clicks(cwb, '//*[@id="slideBox"]/div[2]/ul/li[{}]/a/img'.format(i), now_whd, 0, 0, 0, '',
                                  '', '', 'src', 0, '')

    def test07(self):
        some_tools.wintowh(cwb, 0, 500)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/div[2]/div/h2[1]/a', now_whd, 0, 1, 0, '', '', '', '', 0,
                              '')
        time.sleep(2)
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/div[2]/ul/li/a', now_whd, 0, 1, 0, '', '', '', 'title', 0,
                              '')

    def test08(self):
        some_tools.wintowh(cwb, 0, 500)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/div[3]/div[1]/div[2]/a', now_whd, 1, 1, 1,
                              '//*[@id="pc_download_link"]', '', '', 'title', 0, '')

    def test09(self):
        some_tools.wintowh(cwb, 0, 500)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/div[3]/div[1]/ul/li/a', now_whd, 1, 1, 1,
                              '//*[@id="pc_download_link"]', '//*[@id="android_download_link"]', '', 'title', False, '')

    def test10(self):
        some_tools.wintowh(cwb, 0, 500)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/div[3]/div[2]/ul/li/a', now_whd, 0, 1, 0, '', '', '',
                              'title', 0, '')

    def test11(self):
        some_tools.wintowh(cwb, 0, 500)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/div[1]/div[2]/ul[1]/li/a', now_whd, 0, 1, 0, '', '', '',
                              'title', 0, '')

    def test12(self):
        some_tools.wintowh(cwb, 0, 500)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[5]/div[1]/div[2]/ul[2]/li/a', now_whd, 0, 0, 0, '', '', '', ''
                              , 0, '')


    def test13(self):
        some_tools.wintowh(cwb, 0, 1150)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[6]/div/a', now_whd, 0, 0, 0, '', '', '', 'target', 0, '')

    def test14(self):
        some_tools.wintowh(cwb, 0, 1150)
        now_whd = cwb.current_window_handle
        some_tools.move_in(cwb, '/html/body/div[3]/div[7]/ul/li[1]/a/img')
        time.sleep(1)
        some_tools.ele_clicks(cwb, '/ html / body / div[3] / div[7] / ul / li[1] / a / span / span[3]', now_whd, 0, 0, 0
                              , '', '', '', '', 0, '')
        some_tools.move_in(cwb, '/html/body/div[3]/div[7]/ul/li[2]/a/img')
        time.sleep(1)
        some_tools.ele_clicks(cwb, '/ html / body / div[3] / div[7] / ul / li[2] / a / span / span[3]', now_whd, 0, 0, 0
                              , '', '', '', '', 0, '')

    def test15(self):
        some_tools.wintowh(cwb, 0, 1650)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[8]/div/div/div/a', now_whd, 0, 0, 0, '', '', '', '', 0, '')

    def test16(self):
        some_tools.wintowh(cwb, 0, 1650)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[8]/div/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', 'title',
                              0, '')

    def test17(self):
        some_tools.wintowh(cwb, 0, 1650)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[8]/div/div[2]/ul/li/a', now_whd, 0, 1, 0, '', '', '', 'title',
                              0, '')

    def test18(self):
        some_tools.wintowh(cwb, 0, 1650)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[8]/div/div[3]/ul/li/a', now_whd, 0, 1, 0, '', '', '', '', 0,
                              '')

    def test19(self):
        some_tools.wintowh(cwb, 0, 1650)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[8]/div/div[3]/dl/dd/div/a[1]', now_whd, 1, 0, 1,
                              '//*[@id="pc_download_link"]', '//*[@id="android_download_link"]', '', '', 0, '')

    def test20(self):
        some_tools.wintowh(cwb, 0, 1650)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[10]/div/ul[1]/li/a', now_whd, 1, 1, 0,
                              '//*[@id="pc_download_link"]', '', 'pc', 'title', 0, '')

    def test21(self):
        some_tools.wintowh(cwb, 0, 2200)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[10]/div/ul[2]/li/a', now_whd, 0, 1, 0, '', '', '', 'title', 0,
                              '')

    def test22(self):
        some_tools.wintowh(cwb, 0, 2200)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[11]/div/div/div/a', now_whd, 0, 0, 0, '', '', '', '', 0, '')

    def test23(self):
        some_tools.wintowh(cwb, 0, 2400)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[11]/div/div[2]/ul/li/a', now_whd, 0, 1, 0, '', '', '', 'title'
                              , 0, '')

    def test24(self):
        some_tools.wintowh(cwb, 0, 2200)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[11]/div/div[1]/ul/li/a', now_whd, 0, 1, 0, '', '', '', 'title'
                              , 0, '')

    def test25(self):
        some_tools.wintowh(cwb, 0, 2900)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[11]/div/ul/li/div/a', now_whd, 0, 1, 0, '', '', '', 'title', 0
                              , '')
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[11]/div/ul/li[2]/a', now_whd, 0, 1, 0, '', '', '', 'title', 0
                              , '')

    def test26(self):
        some_tools.wintowh(cwb, 0, 3450)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[11]/div/div[position()>7]/ul/li/a', now_whd, 1, 1, 1,
                              '//*[@id="pc_download_link"]', '//*[@id="android_download_link"]', '', 'title', 0, '')

    def test28(self):
        some_tools.wintowh(cwb, 0, 3950)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[13]/div/ul/li/a', now_whd, 1, 1, 1,
                              '//*[@id="pc_download_link"]', '//*[@id="android_download_link"]', '', 'title', 0, '')

    def test_29(self):
        some_tools.wintowh(cwb, 0, 3950)
        now_whd = cwb.current_window_handle
        cwb.find_element_by_xpath('/html/body/div[3]/div[13]/div/div[2]/ul/li[1]').click()
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[13]/div/div[2]/div/div[1]/div/ul/li/a', now_whd, 0, 1, 0, '',
                              '', '', '', 0, '')
        cwb.find_element_by_xpath('/html/body/div[3]/div[13]/div/div[2]/ul/li[2]').click()
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[13]/div/div[2]/div/div[2]/div/ul/li/a', now_whd, 0, 1, 0, '',
                              '', '', '', 0, '')
        cwb.find_element_by_xpath('/html/body/div[3]/div[13]/div/div[2]/ul/li[3]').click()
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[13]/div/div[2]/div/div[3]/div/ul/li/a', now_whd, 1, 1, 1,
                              '//*[@id="pc_download_link"]', '//*[@id="android_download_link"]', '', '', 0, '')
        cwb.find_element_by_xpath('/html/body/div[3]/div[13]/div/div[2]/ul/li[4]').click()
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[13]/div/div[2]/div/div[4]/div/ul/li/a', now_whd, 1, 1, 1,
                              '//*[@id="pc_download_link"]', '//*[@id="android_download_link"]', '', '', 0, '')

    def test30(self):
        some_tools.wintowh(cwb, 0, 4550)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, '/html/body/div[3]/div[13]/div/div[4]/a', now_whd, 0, 1, 0, '', '', '', '', 0, '')

    def test_31(self):
        some_tools.wintowh(cwb, 0, 4550)
        now_whd = cwb.current_window_handle
        some_tools.ele_clicks(cwb, "/html/body/div[4]/div[1]/dl/dd/ul[@class='clearfix']/li/a", now_whd, 0, 0, 0, '', ''
                              , '', '', 0, '')
        some_tools.ele_clicks(cwb, "/html/body/div[4]/div[3]/div/p[@class='bottom_nav']/a", now_whd, 0, 0, 0, '', ''
                              , '', '', 0, '')
        some_tools.ele_clicks(cwb, "/html/body/div[4]/div[3]/div/p[@class='copyright']/a", now_whd, 0, 0, 0, '', ''
                              , '', '', 0, '')
        some_tools.ele_clicks(cwb, "/html/body/div[4]/div[3]/div/div[@class='safety']/a", now_whd, 0, 0, 0, '', ''
                              , '', '', 0, '')


if __name__ == "__main__":
    unittest.main()