# coding = utf - 8
import re
import time
import os
import requests
from selenium.webdriver import ActionChains
from jiegengnavigate.common.log import Logger

logger = Logger(logger="base_page").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 浏览器刷新操作
    def refresh(self):
        self.driver.refresh()

    def action_chains(self, xpath):
        article = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).move_to_element(article).perform()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("隐性等待%d秒" % seconds)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    def close(self):
        self.driver.close()

    def get_title(self):
        title = self.driver.title
        return title

    @staticmethod
    def wx_message(message):
        uid_list = ["UID_sXMzQWYSxApLNCCQe1Jdx77qVupN", "UID_EQd6wPfuhxH2J3gkZeeWLpOLgn6H",
                    "UID_Owfq9ocQqspnCFcQFLNcy10d43xb", "UID_GlMD6mRYXC4xeQyYeqGQUmCxbHQy"]  # 张浩， 汪航， 杨文娇， 王兴
        url = "http://support.bz.cn/pushWeChat/pushMsg"
        for uid in uid_list:
            datas = {
                'content': message,
                'uid': uid
            }
            requests.post(url, json=datas)

    def log_to_wx(self):
        path = os.path.abspath(".." + '\\Logs\\error_logs')
        for root, dirs, files in os.walk(path):
            file_name = files[-1]
            log = os.path.join(path, file_name)
            with open(log, "r", encoding="utf-8") as result:
                message = ""
                while True:
                    try:
                        fp = result.readline().split("- ERROR - ")[1]
                        message = fp + message
                    except:
                        break
                self.wx_message(message)

    @staticmethod
    # 获取桌面路径
    def get_desktop():
        get_desktop = os.path.join(os.path.expanduser('~'), "Desktop")
        return get_desktop

    def start_browser(self):
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def start_browser_stop(self):
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(5)
        self.driver.maximize_window()

    def quit_browser(self):
        self.driver.quit()

    def click_by_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        self.sleep(1)

    def is_page_after_click(self, text, xpath, flag=True):
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[1])
            self.sleep(0.5)
            url = self.driver.current_url
            result = re.search(r'\D[4][0][4]\D', url)
            if result is None:
                title = self.get_title()
                for world in text:
                    if world != " " and world in title:
                        self.close()
                        self.driver.switch_to.window(handles[0])
                        logger.info(f"{text} - 页面跳转成功")
                        break
                else:
                    self.close()
                    self.driver.switch_to.window(handles[0])
                    logger.warning(f"{text} - 元素跳转至 - {title} - xpath={xpath}")
            else:
                self.close()
                self.driver.switch_to.window(handles[0])
                logger.error(f"{text} - 页面跳转404 - xpath={xpath}")

        elif len(handles) == 1 and flag is True:
            url = self.driver.current_url
            if "404" not in url:
                title = self.get_title()
                for world in text:
                    if world != " " and world in title:
                        self.back()
                        logger.info(f"{text} - 页面跳转成功")
                        break
                else:
                    self.back()
                    logger.warning(f"{text} - 页面title异常 - xpath={xpath}")
            else:
                self.back()
                logger.error(f"{text} - 页面跳转404 - xpath={xpath}")

        elif len(handles) == 1 and flag is False:
            url = self.driver.current_url
            result = re.search(r'\D[4][0][4]\D', url)
            if result is None:
                title = self.get_title()
                for world in text:
                    if world != " " and world in title:
                        logger.info(f"{text} - 页面跳转成功")
                        break
                else:
                    logger.warning(f"{text} - 页面title异常 - xpath={xpath}")
            else:
                logger.error(f"{text} - 页面跳转404 - xpath={xpath}")

        self.sleep(1)

    def is_page(self, text, xpath, flag=True):
        self.click_by_xpath(xpath)
        self.is_page_after_click(text, xpath, flag)

    def is_page_by_no_xpath(self, text):
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[1])
            self.sleep(0.5)
            url = self.driver.current_url
            result = re.search(r'\D[4][0][4]\D', url)
            if result is None:
                title = self.get_title()
                for world in text:
                    if world != " " and world in title:
                        self.close()
                        self.driver.switch_to.window(handles[0])
                        logger.info(f"{text} - 页面跳转成功")
                        break
                else:
                    self.close()
                    self.driver.switch_to.window(handles[0])
                    logger.warning(f"{text} - 元素跳转至 - {title}")
            else:
                self.close()
                self.driver.switch_to.window(handles[0])
                logger.error(f"{text} - 页面跳转404")

        elif len(handles) == 1:
            url = self.driver.current_url
            result = re.search(r'\D[4][0][4]\D', url)
            if result is None:
                title = self.get_title()
                for world in text:
                    if world != " " and world in title:
                        self.back()
                        logger.info(f"{text} - 页面跳转成功")
                        break
                else:
                    self.back()
                    logger.warning(f"{text} - 页面title异常")
            else:
                self.back()
                logger.error(f"{text} - 页面跳转404")
        self.sleep(1)

    def get_text(self, xpath):
        text = self.driver.find_element_by_xpath(xpath).text
        return text

    def to_bottom(self):
        js = "return action=document.body.scrollHeight"
        height = self.driver.execute_script(js)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        self.sleep(5)
        t1 = int(time.time())
        status = True
        num = 0
        while status:
            t2 = int(time.time())
            if t2 - t1 < 10:
                new_height = self.driver.execute_script(js)
                if new_height > height:
                    self.sleep(1)
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    height = new_height
                    t1 = int(time.time())
            elif num < 2:
                self.sleep(3)
                num = num + 1
            else:
                self.driver.execute_script('window.scrollTo(0, 0)')
                break
