import hashlib
import os
import random
import re
import clr
import pyautogui
from selenium.webdriver import ActionChains

from wyw_net.common.basepage import *
from certificateDll import *
# from wyw_net.common.certificateDll import *
my_logger = Logger(logger='3').getlog()


def wintobt(driver):
    # 滚动条到最底下
    js = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(2)


def wintotop(driver):
    # 滚动条到最上面
    js = "window.scrollTo(0,0)"
    driver.execute_script(js)
    time.sleep(2)


def wintowh(driver, x, y):
    # 滚动条横竖向任意滚动
    js = "window.scrollTo({},{})".format(x, y)
    driver.execute_script(js)
    time.sleep(2)


def close_hd_back(driver, nowwd):
    # 关闭所有标签页并切换句柄回到主页
    dr_hds = driver.window_handles
    for i in dr_hds:
        if i != nowwd:
            driver.switch_to.window(i)
            driver.close()
    driver.switch_to.window(nowwd)


def swich_handle(driver,now_hd):
    # 切换窗口句柄
    win_hds = driver.window_handles
    # print(now_hd)
    # print(win_hds)
    # for i in win_hds:
    #     if i != now_hd:
    #         driver.switch_to.window(i)
    driver.switch_to.window(win_hds[-1])


def judgestr(lintxt, tt):
    # 首页链接文字,第二页title
    res = []
    for x in lintxt:
        if x in tt:
            res.append(x)
    if len(res)/len(lintxt) >= 0.3:
        return res
    else:
        return False


def jump_tt_test_large_bt(driver, begin, end, xpath, nowhd):
    r_n = random.randint(begin, end-1)
    for i in range(begin, end):
        zxtxt = driver.find_element_by_xpath(xpath.format(i)).text
        driver.find_element_by_xpath(xpath.format(i)).click()
        swich_handle(driver, nowhd)
        BasePage(driver).wait(10)
        pg_tt = driver.title
        if pg_tt:
            my_logger.info('wyw首页"{}"跳转正常'.format(zxtxt))
        else:
            my_logger.error('wyw首页"{}"跳转异常'.format(zxtxt))
            message('wyw首页"{}"跳转异常'.format(zxtxt))
            Cappic(driver)
        wintowh(driver, 0, 4550)
        res = driver.find_elements_by_xpath('//ul[@id="pagination_item"]/li')
        random_num = random.randint(1, len(res)-1)
        time.sleep(2)
        res[random_num].click()
        time.sleep(2)
        res1 = driver.find_elements_by_xpath('//div[@class="w-tit"]/h4/a')
        random_num1 = random.randint(0, len(res1)-1)
        lintxt = res1[random_num1].text
        res1[random_num1].click()
        time.sleep(2)
        swich_handle(driver, nowhd)
        tt = driver.title
        jures = judgestr(lintxt, tt)
        if jures:
            my_logger.info("wyw下载页面{}跳转正常".format(tt))
        else:
            my_logger.info("wyw下载页面{}跳转异常".format(tt))
            message("wyw下载页面{}跳转异常".format(tt))
        try:
            driver.find_element_by_xpath('//a[@id="pc_download_link"]')
            my_logger.info("wyw下载页面{}下载按钮正常".format(tt))
            if i == r_n:
                driver.find_element_by_xpath('//a[@id="pc_download_link"]').click()
                get_msg(tt)
        except:
            my_logger.error("wyw下载页面{}下载按钮异常".format(tt))
            message("wyw下载页面{}下载按钮异常".format(tt))
        close_hd_back(driver, nowhd)
        time.sleep(2)


def get_msg(p_tt):
    wi, hei = pyautogui.size()
    pyautogui.moveTo(1900/1920*wi, 1000/1080*hei, duration=0.9)
    pyautogui.click(button='left')
    filename = ""
    for root, dirs, files in os.walk(os.path.abspath('..') + '\\downloads\\'):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files[-1])  # 当前路径下所有非目录子文件
        filename = files[-1]
    filename1 = os.path.abspath('..') + '\\downloads\\' + filename
    with open(filename1, "rb") as f:
        data = f.read()
        m = hashlib.md5()
        m.update(data)
        my_logger.info("wyw页面‘{}’下载器md5:{}".format(p_tt, m.hexdigest()))
    clr.AddReference('certificateDll')
    certificate_information = certificate.getCert(filename1)
    certificate_information = str(certificate_information)
    digital_signature = re.findall(r'CN=.+C=CN', certificate_information)
    digital_moment = digital_signature[0]
    digital_signature_data = str(digital_moment[3:-6])
    # digital_signature_data数字签名
    timestamp = re.findall(r'signDate.+', certificate_information)
    timestamp_moment = timestamp[0]
    timestamp_data = str(timestamp_moment[11:-2])
    my_logger.info("wyw页面‘{}’下载器数字签名：{}".format(p_tt, digital_signature_data))
    my_logger.info("wyw页面'{}'下载器时间戳：{}".format(p_tt, timestamp_data))
    time.sleep(5)
    
    
def ele_clicks(driver, xpaths, now_whd, is_bt, is_judge_link, is_mix, pc_bt_xpath, mo_bt_xpath, pc_or_mobile, attr, is_back, mv_xp):
    res = []
    try:
        res = driver.find_elements_by_xpath(xpaths)
    except:
        my_logger.error('xpath有误,站点结构改了？')
        message('xpath有误,站点结构改了？')
        return
    lenth = len(res)
    w = 0
    for i in res:
        w += 1
        res1 = driver.find_elements_by_xpath(xpaths)
        res2 = res1[w - 1]
        zx_txt = ''
        if attr != '':
            zx_txt = res2.get_attribute(attr)
        else:
            zx_txt = res2.text
        driver.execute_script("arguments[0].click();", res2)
        time.sleep(2)
        swich_handle(driver, now_whd)
        pg_tt = driver.title
        judge_jump(is_bt, is_judge_link, zx_txt, pg_tt, driver, is_mix, pc_bt_xpath, mo_bt_xpath, now_whd,
                        pc_or_mobile, is_back, mv_xp, lenth, w)


def judge_jump(is_bt, is_judge_link, zx_txt, pg_tt, driver, is_mix, pc_bt_xpath, mo_bt_xpath, now_hd, pc_or_mobile
               , is_back, mv_xp, lenth, w):
    # 判断页面跳转以及按钮
    if is_bt:
        if is_judge_link:
            judge = judgestr(zx_txt, pg_tt)
            if judge:
                my_logger.info('页面"{}"跳转正常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
            else:
                my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                # message('desk.zol页面"{}"跳转异常'.format(zx_txt))
                Cappic(driver)
        else:
            if pg_tt:
                code_sta = page_tt_code(pg_tt)
                if code_sta:
                    my_logger.info('页面"{}"跳转正常,该类元素共{}个，当前第{}个'.format(pg_tt, lenth, w))
                else:
                    my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(pg_tt, lenth, w))
                    # message('页面"{}"跳转异常'.format(pg_tt))
                    Cappic(driver)
            else:
                my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                # message('页面"{}"跳转异常'.format(pg_tt))
                Cappic(driver)
        if is_mix:
            try:
                driver.find_element_by_xpath(pc_bt_xpath)
                my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
            except:
                try:
                    driver.find_element_by_xpath(mo_bt_xpath)
                    my_logger.info('页面"{}"手机下载按钮正常存在'.format(pg_tt))
                except:
                    my_logger.error('页面"{}"下载按钮异常'.format(pg_tt))
                    # message('页面"{}"下载按钮异常'.format(pg_tt))
                    Cappic(driver)
        else:
            if pc_or_mobile == "pc":
                try:
                    driver.find_element_by_xpath(pc_bt_xpath)
                    my_logger.info('页面"{}"按钮正常存在'.format(pg_tt))
                except:
                    my_logger.error('页面"{}"按钮异常'.format(pg_tt))
                    # message('页面"{}"按钮异常'.format(pg_tt))
                    Cappic(driver)
            else:
                try:
                    driver.find_element_by_xpath(mo_bt_xpath)
                    my_logger.info('页面"{}"手机下载按钮正常存在'.format(pg_tt))
                except:
                    my_logger.error('页面"{}"手机下载按钮异常'.format(pg_tt))
                    # message('页面"{}"手机下载按钮异常'.format(pg_tt))
                    Cappic(driver)
    else:
        if is_judge_link:
            judge = judgestr(zx_txt, pg_tt)
            if judge:
                my_logger.info('页面"{}"跳转正常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
            else:
                my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                # message('fixdown首页"{}"跳转异常'.format(zx_txt))
                Cappic(driver)
        else:
            if pg_tt:
                code_sta = page_tt_code(pg_tt)
                if code_sta:
                    my_logger.info('页面"{}"跳转正常,该类元素共{}个，当前第{}个'.format(pg_tt, lenth, w))
                else:
                    my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(pg_tt, lenth, w))
                    # message('页面"{}"跳转异常'.format(pg_tt))
                    Cappic(driver)
            else:
                my_logger.error('页面"{}"跳转异常,该类元素共{}个，当前第{}个'.format(zx_txt, lenth, w))
                # message('页面"{}"跳转异常'.format(pg_tt))
                Cappic(driver)
    if is_back:
        BasePage(driver).back()
        time.sleep(2)
    else:
        close_hd_back(driver, now_hd)
        time.sleep(2)
    if mv_xp != '':
        move_in(driver, mv_xp)
        time.sleep(1)


def move_in(driver, xpath):
    ele = driver.find_element_by_xpath(xpath)
    ActionChains(driver).move_to_element(ele).perform()


def page_tt_code(pg_tt):
    list_worn = ['401', '402', '403', '404', '405', '406', '407', '408', '409', '501', '502', '503', '504',
                 '505', '506', '507', '508', '509']
    for u in list_worn:
        if u in pg_tt:
            return False
    return True


if __name__ == '__main__':
    get_msg("")
