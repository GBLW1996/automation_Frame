# coding = utf - 8
import unittest
from selenium import webdriver
from jiegengnavigate.common.log import Logger
from jiegengnavigate.framework.jiegeng import JieGengNavigate

jg = JieGengNavigate(webdriver.Chrome())
logger = Logger(logger="test_jiegeng").getlog()


class JieGengAuto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        jg.to_page()
        logger.info("桔梗网-jiegeng.com-自动化测试开始")

    @classmethod
    def tearDownClass(cls):
        jg.quit_browser()
        jg.log_to_wx()
        logger.info("桔梗网-jiegeng.com-自动化测试结束")

    @staticmethod
    def test_01_web_top():
        jg.web_top()

    @staticmethod
    def test_02_box_of_search():
        jg.box_of_search()

    @staticmethod
    def test_03_navigate():
        jg.navigate()

    @staticmethod
    def test_04_left_box():
        jg.left_box()

    @staticmethod
    def test_05_right_box():
        jg.right_box()

    @staticmethod
    def test_06_left_box_2():
        jg.left_box_2()

    @staticmethod
    def test_07_mid_bar():
        jg.mid_bar()

    @staticmethod
    def test_08_today_hot():
        jg.today_hot()

    @staticmethod
    def test_09_left_box_3():
        jg.left_box_3()

    @staticmethod
    def test_10_left_box_4():
        jg.left_box_4()

    @staticmethod
    def test_11_left_box_5():
        jg.left_box_5()

    @staticmethod
    def test_12_left_box_6():
        jg.left_box_6()

    @staticmethod
    def test_13_mid_bar_2():
        jg.mid_bar_2()

    @staticmethod
    def test_14_mid_bar_3():
        jg.mid_bar_3()

    @staticmethod
    def test_15_play_game():
        jg.play_game()

    @staticmethod
    def test_16_web_popular():
        jg.web_popular()

    @staticmethod
    def test_17_financial():
        jg.financial()

    @staticmethod
    def test_18_life_thing():
        jg.life_thing()

    @staticmethod
    def test_19_minutes_of_relaxation():
        jg.minutes_of_relaxation()

    @staticmethod
    def test_20_bottom_flow():
        jg.bottom_flow()


if __name__ == '__main__':
    unittest.main(verbosity=2)
