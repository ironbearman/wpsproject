import unittest
import requests
from common.ymlRead import YamlRead
from buinessCommon.celearNote import Clearnotes
from common.outputCheck import OutputCheck
# from parameterized import parameterized
from buinessCommon.re import Re
from common.caselog import step, class_case_log
from buinessCommon.creatGroup import CreateGroup


@class_case_log
class GetNotePage(unittest.TestCase):
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    expr = {
        'responseTime': 0,
        'webNotes': [{"noteId": str, "createTime": int, "star": int, "remindTime": int,
                      "remindType": int, "infoVersion": 1, "infoUpdateTime": int, "groupId": None,
                      "title": str, "summary": str, "thumbnail": None,
                      "contentVersion": int, "contentUpdateTime": int}]
    }

    def setUp(self):
        print('setUp')

    def tearDown(self) -> None:
        print('测试结束')

    def testCase02_major(self):
        """startindex为字符串校验"""
        userId1 = self.userId1
        startindex = '你好'
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')

        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(expr, res.json())

    def testCase03_major(self):
        """startindex空校验"""
        userId1 = self.userId1
        startindex = None
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(expr, res.json())

    def testCase04_major(self):
        """startindex为空字符串类型校验"""
        userId1 = self.userId1
        startindex = ''
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        # 没有对齐接口返回
        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(404, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(expr, res.json())

    def testCase06_major(self):
        """startindex为过长校验"""
        userId1 = self.userId1
        startindex = 99999999999999999999999999999999
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(404, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(expr, res.json())

    def testCase07_major(self):
        """startindex为！@#￥校验"""
        userId1 = self.userId1
        startindex = '！@#￥5'
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(404, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(expr, res.json())

    def testCase08_major(self):
        """startindex为！@#￥校验"""
        userId1 = self.userId1
        startindex = '！@#￥5'
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(404, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase09_major(self):
        """startindex为！@#￥校验"""
        userId1 = self.userId1
        startindex = '！@#￥5'
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(expr, res.json())

    def testCase10_major(self):
        """rows为字符串校验"""
        userId1 = self.userId1
        startindex = 99
        rows = '你好'
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')

        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(expr, res.json())

    def testCase11_major(self):
        """rows空校验"""
        userId1 = self.userId1
        startindex = 99
        rows = None
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase12_major(self):
        """rows为空字符串类型校验"""
        userId1 = self.userId1
        startindex = 1
        rows = ""
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase13_major(self):
        """rows过长校验"""
        userId1 = self.userId1
        startindex = 1
        rows = 199999999999999999999999999999999
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase14_major(self):
        """rows为！@#￥校验"""
        userId1 = self.userId1
        startindex = 99
        rows = '！@#￥5'
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(404, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(expr, res.json())

    def testCase15_major(self):
        """userids为字符串校验"""
        userId1 = '你好'
        startindex = 1
        rows = 0
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')

        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(expr, res.json())

    def testCase16_major(self):
        """userids为空校验"""
        userId1 = None
        startindex = 1
        rows = 0
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase17_major(self):
        """userids为空字符串类型校验"""
        userId1 = ''
        startindex = 1
        rows = 0
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase18_major(self):
        """userids为！@#4校验"""
        userId1 = '!@##$'
        startindex = 1
        rows = 0
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)

        expr = {"errorCode": -7, "errorMsg": '参数类型错误！'}
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')
        print(res.status_code)
        print(res.text)
        OutputCheck().assert_output(self.expr, res.json())


