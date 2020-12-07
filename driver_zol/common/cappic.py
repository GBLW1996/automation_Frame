# coding=utf-8
import time
import os

def Cappic(driver):
    pt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    picname = os.path.abspath('..')+'\\screenshots\\'+pt+'.png'
    driver.get_screenshot_as_file(picname)