import unittest
from BeautifulReport import BeautifulReport
import os

# 线上测试环境 online
ENVIO = 'online'
# 获取当前文件绝对路径
Dri = os.path.dirname(os.path.abspath(__file__))


def run(test_suite):
    # 定义输出的文件位置和名字
    filename = "1019Unittest/report.html"
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description='测试报告', report_dir='/')


if __name__ == '__main__':
    pattern = 'all'
    if pattern == 'all':
        suite = unittest.TestLoader().discover('', 'test_create*')
    elif pattern == 'smoking':
        suite = unittest.TestLoader().discover('./testCase', 'test_major*')
    else:
        suite = unittest.TestLoader().discover('', 'test_create*')
    run(suite)
