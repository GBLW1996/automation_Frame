# coding=utf-8
import HTMLTestRunner
import os
import sys
import unittest
import time

#添加环境变量
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.TestLoader().discover("testsuites")

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="fixdown自动化测试报告", description="用例测试情况", verbosity=2)
    # 开始执行测试套件
    runner.run(suite)
    fp.close()