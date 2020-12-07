import time
import unittest
from jiegeng_net.pages.basepage import BasePage
import os
from selenium import webdriver
from jiegeng_net.common.tools import PageTool
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
        my_tools.ele_clicks(cwb, '//*[@id="indexLogo"]/a/img', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="eastplugin-weather-box"]/div/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="calendar"]/div/span[1]/a[1]', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="calendar"]/div/span[1]/a[3]', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="calendar"]/div/span[2]/a[2]', now_whd)
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="login"]/span[2]'))
        cwb.find_element_by_xpath('//*[@id="login_form"]/form/div[2]/input').send_keys('18855043070')
        cwb.find_element_by_xpath('//*[@id="login_form"]/form/div[3]/input').send_keys('wxwx1996918\n')
        time.sleep(3)
        txt1 = cwb.switch_to_alert().text
        if txt1 == '登录成功':
            my_tools.my_logger.info('登录正常')
        else:
            my_tools.my_logger.error('登录异常')
        try:
            cwb.switch_to_alert().accept()
            my_tools.my_logger.info('alert关闭')
        except Exception as e:
            my_tools.my_logger.error(e)
            my_tools.my_logger.info('alert关闭失败')
        my_tools.ele_clicks(cwb, '//*[@id="noticeslider"]/div/div/ul/li[2]/a', now_whd)
        my_tools.test_input(cwb, ['安徽', '滁州', '大熊猫', '京东', '淘宝'], '//*[@id="search-input"]', now_whd)
        my_tools.static_click(cwb, cwb.find_element_by_xpath('//*[@id="search-form"]/div[2]/div/a'))

    def test_02(self):
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="box-starbar"]/div/a', now_whd, is_judge_link=1)  # 电视剧/电影/...
        my_tools.ele_clicks(cwb, '//*[@id="site"]/div[1]/ul/li/a[1]', now_whd)  # 网站链接
        my_tools.ele_clicks(cwb, '//*[@id="box-famoussite"]/div/ul/li/a', now_whd)  # 网站链接
        my_tools.ele_clicks(cwb, '//*[@id="hlbar"]/span/a', now_whd)  # 网站链接
        my_tools.ele_clicks(cwb, '//*[@id="topzixun-over"]/div/p/a', now_whd)  # 推荐/社会/... & # 热剧/电影/...
        my_tools.ele_clicks(cwb, '//*[@id="infoflow-list"]/div/div[2]/p[1]/a', now_whd)  # 今日热点
        my_tools.ele_clicks(cwb, '//*[@id="layout-side"]/div[3]/div[3]/div/div/div/div/p/a/span', now_whd)  # 热游/页游
        my_tools.ele_clicks(cwb, '//*[@id="layout-side"]/div[3]/div[4]/div/div/div/div/p/a/span', now_whd)  # 竞猜/竞技彩
        my_tools.ele_clicks(cwb, '//*[@id="toplist-soft"]/div/div/div/div/p/a', now_whd)  # 必备软件/常用软件
        my_tools.ele_clicks(cwb, '//*[@id="navigate"]/a/span', now_whd)  # 电视剧/电影/新闻...
        my_tools.ele_clicks(cwb, '//*[@id="coolsite-group0"]/div/h4/a', now_whd)  # 影视/视频/游戏...
        my_tools.ele_clicks(cwb, '//*[@id="coolsite-group0"]/div/span/a', now_whd)  # 电视剧/电影/动漫...
        my_tools.ele_clicks(cwb, '//*[@id="coolsite-group0"]/div[4]/div/div/div/ul/li/div/a', now_whd)  # 图片
        my_tools.ele_clicks(cwb, '//*[@id="coolsite-group1"]/div[1]/a', now_whd)  # 软件/彩票/教育/...
        my_tools.ele_clicks(cwb, '//*[@id="coolsite-group1"]/div/h4/a', now_whd)  # 社交/汽车/软件/...
        my_tools.ele_clicks(cwb, '//*[@id="coolsite-group1"]/div/span/a', now_whd)  # 世纪佳缘/珍爱网/百合网...
        my_tools.ele_clicks(cwb, '//*[@id="coolsite-group1"]/div[5]/div/div/div/ul/li/div/a', now_whd)  # 图片

    def test_03(self):  # 玩游戏
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="gl_slider"]/div/div/ul/li/a', now_whd)  # 轮播图
        my_tools.ele_clicks(cwb, '//*[@id="ctab_game_yxdq"]/div[1]/div/div[2]/ul/li/a', now_whd)  # 轮播图下方游戏
        my_tools.ele_clicks(cwb, '//*[@id="gimgl2"]/a/img', now_whd)  # 游戏图片
        my_tools.ele_clicks(cwb, '//*[@id="gr_slider"]/div/div/ul/li/ul/li/a', now_whd)  # 左侧图片和文字
        my_tools.ele_clicks(cwb, '//*[@id="hao123-game"]/div/div[1]/div/div/a[2]', now_whd)  # 进入网页游戏
        my_tools.ele_clicks(cwb, '//*[@id="hao123-game"]/div/div[3]/div[1]/div/ul/li/a', now_whd)  # 左侧图片和文字
        my_tools.ele_clicks(cwb, '//*[@id="hao123-game"]/div/div[3]/div[2]/ul/li/a/span[1]', now_whd)  # 图片

    def test_04(self):  # 全网热播
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="shortvideo_slider1"]/div/div/ul/li/a', now_whd)  # 轮播图
        my_tools.ele_clicks(cwb, '//*[@id="hao123-shortvideo"]/div[2]/div[2]/div/a', now_whd)  # 底部图
        my_tools.ele_clicks(cwb, '//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div/a', now_whd)  # 图片

    def test_05(self):  # 生活这点事
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="slider_597985e4ce882"]/div/div/ul/li/div/div/div/div/div/ul/li/a', now_whd)
        # 轮播图
        my_tools.ele_clicks(cwb, '//*[@id="slider_597985e4ce882"]/div/div/ul/li/div/ul/li/a', now_whd)  # a链接
        my_tools.ele_clicks(cwb, '//*[@id="slider_597985e4ce882"]/div/div/ul/li/div/ul/li/a', now_whd)  # 轻松10分钟

    def test_06(self):  # 轻松10分钟
        now_whd = cwb.current_window_handle
        my_tools.ele_clicks(cwb, '//*[@id="relex"]/div[2]/div[1]/div/div/a', now_whd)  # 图片

    def test_07(self):  # 底部资讯
        now_whd = cwb.current_window_handle
        my_tools.wintowh(cwb, 0, 2500)
        my_tools.ele_clicks(cwb, '//*[@id="news"]/ul/li/div/div[2]/div[1]/h3/a', now_whd)
        my_tools.ele_clicks(cwb, '//*[@id="hotRecommend"]/ul/li/p/span/a', now_whd)  # 右边资讯


if __name__ == "__main__":
    unittest.main()