# -*-coding: utf-8-*-
from selenium import webdriver
from jiegengnavigate.common.log import Logger
from jiegengnavigate.pages.basepage import BasePage

logger = Logger(logger="frame_work").getlog()


class JieGengNavigate(BasePage):

    def to_page(self):
        self.start_browser()
        url = "https://www.jiegeng.com/"
        self.driver.get(url)
        title = self.get_title()
        if "桔梗导航" in title:
            logger.info("桔梗导航 - 页面跳转成功")
            self.sleep(1)

    def web_top(self):
        xpath_logo = '//*[@id="indexLogo"]/a/img'
        text_logo = "桔梗网logo"
        self.is_page(text_logo, xpath_logo)  # 页面Logo
        xpath_mas = '//*[@id="eastplugin-weather-box"]/div/a/span[1]'
        text_mas = self.get_text(xpath_mas)
        self.is_page(text_mas, xpath_mas)  # 城市天气按钮
        text_weather_pic = "天气图片logo"
        xpath_weather_pic = '//*[@id="eastplugin-weather-box"]/div/a/span[1]/i'
        self.is_page(text_weather_pic, xpath_weather_pic)  # 天气图片logo
        text_calendar = "日历搜索 - 日"
        xpath_calendar = '//*[@id="calendar"]/div/span[1]/a[1]'
        self.is_page(text_calendar, xpath_calendar)  # 日历 - 日
        text_calendar1 = "日历搜索 - 周"
        xpath_calendar1 = '//*[@id="calendar"]/div/span[1]/a[2]'
        self.is_page(text_calendar1, xpath_calendar1)  # 日历 - 周
        text_calendar2 = "日历搜索 - 农历"
        xpath_calendar2 = '//*[@id="calendar"]/div/span[2]/a[1]'
        self.is_page(text_calendar2, xpath_calendar2)  # 日历 - 农历
        xpath_sheng_xiao = '//*[@id="calendar"]/div/span[1]/a[3]'
        text_sheng_xiao = self.get_text(xpath_sheng_xiao)
        self.is_page(text_sheng_xiao, xpath_sheng_xiao)  # 生肖查询
        xpath_horoscope = '//*[@id="calendar"]/div/span[2]/a[2]'
        text_horoscope = self.get_text(xpath_horoscope)
        self.is_page(text_horoscope, xpath_horoscope)  # 星座运势
        xpath_register = '//*[@id="login"]/span[1]'  # 注册按钮
        text_register = self.get_text(xpath_register)
        try:
            self.click_by_xpath(xpath_register)
            logger.info(f"{text_register}按钮点击成功")
        except Exception:
            logger.error(f"{text_register}按钮点击失败")
        self.sleep(1)

        def web_log_in():  # 登录模块
            username = "z2492159o"
            password = "1989718"
            self.driver.find_element_by_name("username").send_keys(username)
            self.driver.find_element_by_name("password").send_keys(password)
            self.driver.find_element_by_xpath('//*[@id="login_form"]/form/div[4]/input').click()
            self.sleep(1)

        web_log_in()
        alt = self.driver.switch_to.alert
        alert_text_register = alt.text
        if alert_text_register == "用户名已注册":
            logger.info("注册功能无异常")
        else:
            logger.error("注册功能异常")
        alt.accept()
        xpath_log_in = '//*[@id="login"]/span[2]'  # 登录按钮
        text_log_in = self.get_text(xpath_log_in)
        try:
            self.click_by_xpath(xpath_log_in)
            logger.info(f"{text_log_in}按钮点击成功")
        except Exception:
            logger.error(f"{text_log_in}按钮点击失败")
        self.sleep(1)

        web_log_in()
        alt_log_in = self.driver.switch_to.alert
        alert_text_log_in = alt.text
        if alert_text_log_in == "登录成功":
            logger.info("登录功能无异常")
        else:
            logger.error("登录功能异常")
        alt_log_in.accept()

    def box_of_search(self):
        ele = self.driver.find_elements_by_xpath('//*[@class="ctrlBtn"]')
        self.driver.execute_script('arguments[0].click();', ele[1])
        xpath = '//*[@id="hotsearch-box"]/div[2]/ul/li/a'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) // 2 + 1):
            xpath_box = f'//*[@id="hotsearch-box"]/div[2]/ul/li[{i}]/a'
            ele = self.driver.find_elements_by_xpath(xpath_box)
            text = ele[1].text
            self.driver.execute_script('arguments[0].click();', ele[1])
            self.is_page_after_click(text, xpath_box)

    def navigate(self):
        xpath = '//*[@id="menus"]/li/a/span'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_i = f'//*[@id="menus"]/li[{i}]/a/span'
            text = self.get_text(xpath_i)
            if i > 1:
                self.is_page(text, xpath_i)
                self.sleep(1)
            else:
                self.click_by_xpath(xpath_i)
                title = self.get_title()
                if "桔梗导航" in title:
                    logger.info("桔梗导航 - 首页 - 点击成功")

    def left_box(self):
        for i in range(1, 10):
            for j in range(1, 3):
                xpath = f'//*[@id="box-starbar"]/div[{i}]/a[{j}]'
                text = self.get_text(xpath)
                self.is_page(text, xpath)

    def right_box(self):
        for i in range(1, 25):
            xpath = f'//*[@id="site"]/div[1]/ul/li[{i}]/a'
            xpath_ico = f'//*[@id="site"]/div[1]/ul/li[{i}]/a[1]'
            text = self.get_text(xpath)
            text_ico = self.get_text(xpath_ico)
            try:
                ele = self.driver.find_element_by_xpath(xpath)
                self.driver.execute_script('arguments[0].click();', ele)
                self.is_page_after_click(text, xpath)
            except:
                ele_ico = self.driver.find_element_by_xpath(xpath_ico)
                self.driver.execute_script('arguments[0].click();', ele_ico)
                self.is_page_after_click(text_ico, xpath_ico)

        for j in range(1, 19):
            xpath = f'//*[@id="box-famoussite"]/div/ul/li[{j}]/a'
            text = self.get_text(xpath)
            ele = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script('arguments[0].click();', ele)
            self.is_page_after_click(text, xpath)

    def left_box_2(self):
        xpath = '//*[@id="layout-side"]/div[3]/div[1]/div/div/div[1]/a'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_bar = f'//*[@id="layout-side"]/div[3]/div[1]/div/div/div[1]/a[{i}]'
            text_bar = self.get_text(xpath_bar)
            self.click_by_xpath(xpath_bar)
            logger.info(f"{text_bar} - 点击成功")
            self.sleep(1)
            for new in range(1, 10):
                xpath_new = f'//*[@id="topzixun-over"]/div/p[{new}]/a/span'
                xpath_new_all = self.driver.find_elements_by_xpath(xpath_new)
                text_new = xpath_new_all[i - 1].text
                xpath_new_all[i - 1].click()
                self.is_page_by_no_xpath(text_new)

    def mid_bar(self):
        xpath = '//*[@id="hlbar"]/span/a'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_mid_bar = f'//*[@id="hlbar"]/span[{i}]/a'
            text = self.get_text(xpath_mid_bar)
            self.is_page(text, xpath_mid_bar)

    def today_hot(self):
        xpath = '//*[@id="infoflow-list"]/div/div[2]/p[1]/a'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_c = f'//*[@id="infoflow-list"]/div[{i}]/div[2]/p[1]/a'
            text = self.get_text(xpath_c)
            self.is_page(text, xpath_c)

    def left_box_3(self):
        xpath = '//*[@id="layout-side"]/div[3]/div[2]/div/div/div[1]/a'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_bar = f'//*[@id="layout-side"]/div[3]/div[2]/div/div/div[1]/a[{i}]'
            text_bar = self.get_text(xpath_bar)
            self.click_by_xpath(xpath_bar)
            logger.info(f"{text_bar} - 点击成功")
            self.sleep(1)
            for new in range(1, 4):
                xpath_new = f'//*[@id="topzixun-over"]/div/p[{new}]/a/span'
                xpath_new_all = self.driver.find_elements_by_xpath(xpath_new)
                text_new = xpath_new_all[i + 4].text
                xpath_new_all[i + 4].click()
                self.is_page_by_no_xpath(text_new)

    def left_box_4(self):
        xpath = '//*[@id="layout-side"]/div[3]/div[3]/div/div/div[1]/a'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_bar = f'//*[@id="layout-side"]/div[3]/div[3]/div/div/div[1]/a[{i}]'
            text_bar = self.get_text(xpath_bar)
            self.click_by_xpath(xpath_bar)
            logger.info(f"{text_bar} - 点击成功")
            self.sleep(1)
            for li in range(2, 4):
                for we in range(1, 4):
                    xpath_new = f'//*[@id="layout-side"]/div[3]/div[3]/div/div/div[{i + 1}]/div[{li}]/p[{we}]/a/span'
                    text_new = self.get_text(xpath_new)
                    self.is_page(text_new, xpath_new)

    def left_box_5(self):
        xpath = '//*[@id="layout-side"]/div[3]/div[4]/div/div/div[1]/a'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_bar = f'//*[@id="layout-side"]/div[3]/div[4]/div/div/div[1]/a[{i}]'
            text_bar = self.get_text(xpath_bar)
            self.click_by_xpath(xpath_bar)
            logger.info(f"{text_bar} - 点击成功")
            self.sleep(1)
            for li in range(2, 4):
                for we in range(1, 4):
                    xpath_new = f'//*[@id="layout-side"]/div[3]/div[4]/div/div/div[{i + 1}]/div[{li}]/p[{we}]/a/span'
                    text_new = self.get_text(xpath_new)
                    self.is_page(text_new, xpath_new)

    def left_box_6(self):
        xpath = '//*[@id="toplist-soft"]/div/div/div[1]/a'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_bar = f'//*[@id="toplist-soft"]/div/div/div[1]/a[{i}]'
            text_bar = self.get_text(xpath_bar)
            self.click_by_xpath(xpath_bar)
            logger.info(f"{text_bar} - 点击成功")
            self.sleep(1)
            for li in range(1, 3):
                for we in range(1, 7):
                    xpath_new = f'//*[@id="toplist-soft"]/div/div/div[{i + 1}]/div[{li}]/p[{we}]/a'
                    text_new = self.get_text(xpath_new)
                    self.is_page(text_new, xpath_new)

    def mid_bar_2(self):
        for i in range(1, 6):
            for j in range(1, 8):
                self.driver.switch_to.frame("myFrame")
                xpath_new = f'//*[@id="wrapper"]/div[{i}]/ul/li[{j}]/a'
                text_new = self.get_text(xpath_new)
                ele = self.driver.find_element_by_xpath(xpath_new)
                self.driver.execute_script('arguments[0].click();', ele)
                self.is_page_after_click(text_new, xpath_new)
                self.driver.switch_to.default_content()

    def mid_bar_3(self):
        xpath_nav = '//*[@id="navigate"]/a/span'
        xpath_all_nav = self.driver.find_elements_by_xpath(xpath_nav)
        for nav in range(1, len(xpath_all_nav) + 1):
            xpath_nav_s = f'//*[@id="navigate"]/a[{nav}]/span'
            text_nav = self.get_text(xpath_nav_s)
            self.is_page(text_nav, xpath_nav_s)

        for classify in range(1, 9):
            if classify == 4:
                continue
            xpath_left = f'//*[@id="coolsite-group0"]/div[{classify}]/h4/a'
            text_left = self.get_text(xpath_left)
            self.is_page(text_left, xpath_left, flag=False)

            xpath_classify = f'//*[@id="coolsite-group0"]/div[{classify}]/span/a'
            xpath_all_classify = self.driver.find_elements_by_xpath(xpath_classify)
            for i in range(1, len(xpath_all_classify) - 1):
                xpath_s = f'//*[@id="coolsite-group0"]/div[{classify}]/span[{i}]/a'
                text = self.get_text(xpath_s)
                ele = self.driver.find_element_by_xpath(xpath_s)
                self.driver.execute_script('arguments[0].click();', ele)
                self.is_page_after_click(text, xpath_s, flag=False)

        xpath_mid_nav = '//*[@id="coolsite-group1"]/div[1]/a'
        xpath_all_mid_nav = self.driver.find_elements_by_xpath(xpath_mid_nav)
        for nav_1 in range(1, len(xpath_all_mid_nav) + 1):
            xpath_nav_s = f'//*[@id="coolsite-group1"]/div[1]/a[{nav_1}]'
            text_nav = self.get_text(xpath_nav_s)
            self.is_page(text_nav, xpath_nav_s)

        for classify_1 in range(2, 8):
            if classify_1 == 5:
                continue
            xpath_left = f'//*[@id="coolsite-group1"]/div[{classify_1}]/h4/a'
            text_left = self.get_text(xpath_left)
            self.is_page(text_left, xpath_left, flag=False)

            xpath_classify = f'//*[@id="coolsite-group1"]/div[{classify_1}]/span/a'
            xpath_all_classify = self.driver.find_elements_by_xpath(xpath_classify)
            for i in range(2, len(xpath_all_classify)):
                xpath_s = f'//*[@id="coolsite-group1"]/div[{classify_1}]/span[{i}]/a'
                text = self.get_text(xpath_s)
                ele = self.driver.find_element_by_xpath(xpath_s)
                self.driver.execute_script('arguments[0].click();', ele)
                self.is_page_after_click(text, xpath_s, flag=False)

    def play_game(self):

        self.driver.find_element_by_xpath('//*[@id="hao123-game"]/div/div[1]/div/div/a[1]').click()  # 热门游戏
        self.sleep(1)

        xpath_img = '//*[@id="gl_slider"]/div/div/ul/li[1]/a/span[2]'
        text_img = self.get_text(xpath_img)
        self.is_page(text_img, xpath_img)

        for i in range(1, 7):
            xpath = f'//*[@id="ctab_game_yxdq"]/div[1]/div/div[2]/ul/li[{i}]/a/span'
            text = self.get_text(xpath)
            self.is_page(text, xpath)

        for j in range(1, 25):
            xpath = f'//*[@id="gimgl2"]/a[{j}]/span'
            text = self.get_text(xpath)
            self.is_page(text, xpath)

        self.driver.find_element_by_xpath('//*[@id="hao123-game"]/div/div[1]/div/div/a[2]').click()  # 网页游戏
        self.sleep(1)

        xpath_web_img = '//*[@id="hao123-game"]/div/div[3]/div[1]/div/ul/li[1]/a/span[3]'
        text_web_img = self.get_text(xpath_web_img)
        self.is_page(text_web_img, xpath_web_img)

        for a in range(3, 7):
            xpath = f'//*[@id="hao123-game"]/div/div[3]/div[1]/div/ul/li[{a}]/a[1]'
            text = self.get_text(xpath)
            self.is_page(text, xpath)

        for b in range(1, 9):
            xpath = f'//*[@id="hao123-game"]/div/div[3]/div[2]/ul/li[{b}]/a/span[2]'
            text = self.get_text(xpath)
            self.is_page(text, xpath)

    def web_popular(self):  # 全网热播
        xpath = '//*[@id="shortvideo_slider1"]/div/div/ul/li/a/span[2]'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_1 = f'//*[@id="shortvideo_slider1"]/div/div/ul/li[{i}]/a/span[2]'
            text = self.get_text(xpath_1)
            while True:
                try:
                    self.click_by_xpath(xpath_1)
                    self.is_page_after_click(text, xpath_1)
                    break
                except:
                    xpath_next = '//*[@id="shortvideo_slider1"]/div/a[2]'
                    self.click_by_xpath(xpath_next)
                    self.sleep(0.5)

        xpath_2 = '//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div/a/span[2]'
        xpath_all_2 = self.driver.find_elements_by_xpath(xpath_2)
        for j in range(1, len(xpath_all_2) + 1):
            xpath_c = f'//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[{j}]/a/span[2]'
            text = self.get_text(xpath_c)
            self.is_page(text, xpath_c)

        xpath_3 = '//*[@id="hao123-shortvideo"]/div[2]/div[2]/div/a/span[2]'
        xpath_all_3 = self.driver.find_elements_by_xpath(xpath_3)
        for a in range(1, len(xpath_all_3) + 1):
            xpath_c = f'//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[{a}]/a/span[2]'
            text = self.get_text(xpath_c)
            self.is_page(text, xpath_c)

    def financial(self):  # 金融
        xpath = '//*[@id="service-licai"]/div[1]/div/ul/li/a'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all)):
            xpath_c = f'//*[@id="service-licai"]/div[1]/div/ul/li[{i}]/a'
            text = self.get_text(xpath_c)
            self.is_page(text, xpath_c)

        xpath_list = ['//*[@id="service-licai-inner"]/div[1]/div[1]/div[1]/div[1]/a',
                      '//*[@id="service-licai-inner"]/div[1]/div[1]/div[1]/div[2]/a',
                      '//*[@id="service-licai-inner"]/div[1]/div[1]/div[2]/a/img',
                      '//*[@id="service-licai-inner"]/div[1]/div[1]/div[2]/div/div[1]/a',
                      '//*[@id="service-licai-inner"]/div[1]/div[1]/div[2]/div/div[2]/a',
                      '//*[@id="service-licai-inner"]/div[1]/div[2]/div[1]/div/a',
                      '//*[@id="service-licai-inner"]/div[1]/div[2]/div[2]/div[1]/a[2]/div[2]',
                      '//*[@id="service-licai-inner"]/div[1]/div[2]/div[2]/div[2]/a[2]/div[2]',
                      '//*[@id="service-licai-inner"]/div[2]/div[2]/a[1]',
                      '//*[@id="service-licai-inner"]/div[2]/div[2]/a[2]',
                      '//*[@id="service-licai-inner"]/div[2]/div[2]/a[3]']

        for xpath_l in xpath_list:
            text = self.get_text(xpath_l)
            if text:
                self.is_page(text, xpath_l)
            else:
                text = self.driver.find_element_by_xpath(xpath_l).get_attribute("alt")
                self.is_page(text, xpath_l)

    def life_thing(self):  # 生活这点事
        xpath = '//*[@class="life-bd"]/div/div/div/ul/li/div/div/div/div/div/ul/li[1]/a/span[2]'
        xpath_all = self.driver.find_elements_by_xpath(xpath)
        for i in range(1, len(xpath_all) + 1):
            xpath_c = '//*[@class="life-bd"]/div/div/div/ul/li/div[%d]/div/div/div/div/ul/li[1]/a/span[2]' % i
            text = self.get_text(xpath_c)
            ele = self.driver.find_element_by_xpath(xpath_c)
            self.driver.execute_script('arguments[0].click();', ele)
            self.is_page_after_click(text, xpath_c)

        xpath_1 = '//*[@class="life-bd"]/div/div/div/ul/li/div/ul/li/a'
        xpath_all_1 = self.driver.find_elements_by_xpath(xpath_1)
        for j in xpath_all_1:
            text = j.text
            j.click()
            self.is_page_by_no_xpath(text)

    def minutes_of_relaxation(self):  # 轻松10分钟
        for i in range(1, 3):
            for j in range(1, 11):
                xpath = f'//*[@id="relex"]/div[2]/div[1]/div/div[{i}]/a[{j}]/span[2]'
                text = None
                try:
                    text = self.get_text(xpath)
                    self.is_page(text, xpath)
                except:
                    self.click_by_xpath('//*[@id="relex"]/div[2]/div[2]/a[1]')
                    self.sleep(0.5)
                    self.is_page(text, xpath)

    def bottom_flow(self):  # 底部信息流
        self.to_bottom()
        xpath_right_flow = '//*[@id="hotRecommend"]/ul/li/p/span/a'
        xpath_all_right_flow = self.driver.find_elements_by_xpath(xpath_right_flow)
        for i in range(1, len(xpath_all_right_flow) + 1):
            xpath_c = '//*[@id="hotRecommend"]/ul/li[%d]/p/span/a' % i
            text = self.get_text(xpath_c)
            ele = self.driver.find_element_by_xpath(xpath_c)
            self.driver.execute_script('arguments[0].click();', ele)
            self.is_page_after_click(text, xpath_c)

        xpath_left_flow = '//*[@id="news"]/ul/li/div/div[2]/div[1]/h3/a'
        xpath_all_left_flow = self.driver.find_elements_by_xpath(xpath_left_flow)
        for j in range(1, len(xpath_all_left_flow) + 1):
            xpath_c = '//*[@id="news"]/ul/li[%d]/div/div[2]/div[1]/h3/a' % j
            text = self.get_text(xpath_c)
            ele = self.driver.find_element_by_xpath(xpath_c)
            self.driver.execute_script('arguments[0].click();', ele)
            self.is_page_after_click(text, xpath_c)

    def main(self):
        self.to_page()
        self.web_top()
        self.box_of_search()
        self.navigate()
        self.left_box()
        self.right_box()
        self.left_box_2()
        self.mid_bar()
        self.today_hot()
        self.left_box_3()
        self.left_box_4()
        self.left_box_5()
        self.left_box_6()
        self.mid_bar_2()
        self.mid_bar_3()
        self.play_game()
        self.web_popular()
        self.financial()
        self.life_thing()
        self.minutes_of_relaxation()
        self.bottom_flow()
        self.quit_browser()
        self.log_to_wx()


if __name__ == "__main__":
    jg = JieGengNavigate(driver=webdriver.Chrome())
    jg.main()
