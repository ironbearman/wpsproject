import unittest
import requests
import time
from common.ymlRead import YamlRead
from buinessCommon.celearNote import Clearnotes
from common.outputCheck import OutputCheck
# from parameterized import parameterized
from buinessCommon.re import Re
from common.caselog import step, class_case_log
from buinessCommon.creatGroup import CreateGroup


# from parameterized import parameterized
# from common.outputCheck import OutputCheck


class UpNotesbody(unittest.TestCase):
    path = '/v3/notesvr/set/noteinfo'
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    expr = {
        'responseTime': int,
        'infoVersion': int,
        'infoUpdateTime': int,
    }

    def setUp(self):
        print("test start")

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self):
        """校验star0"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': '',
            'remindType': '0',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        version = res.json()['infoVersion']
        print(version)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())


    def testCase_02(self):
        """校验star1"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 1,
            'remindTime': '',
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        version = res.json()['infoVersion']
        print(version)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())


    def testCase_03(self):
        """校验star2"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 2,
            'remindTime': '',
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        version = res.json()['infoVersion']
        print(version)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_04(self):
        """校验star空"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': '',
            'remindTime': '',
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        version = res.json()['infoVersion']
        print(version)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_05(self):
        """校验star-1"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': -1,
            'remindTime': '',
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        version = res.json()['infoVersion']
        print(version)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_06(self):
        """校验star3"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 3,
            'remindTime': '',
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        version = res.json()['infoVersion']
        print(version)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_07(self):
        """校验star字符串"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': '你好',
            'remindTime': '',
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_08(self):
        """校验remindtime字符串"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': '1还是',
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())


    def testCase_09(self):
        """校验remindtype"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 1,
            'remindTime': '',
            'remindType': '1',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())


    def testCase_10(self):
        """校验remindtime最小时间戳"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 2,
            'remindTime': 1699282,
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_11(self):
        """校验remindtime"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': '',
            'remindTime': 32503564882,
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_12(self):
        """校验remindtime"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime':  158909988058787854,
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_13(self):
        """校验remindtime范围外的值"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': -1589099880,
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_14(self):
        """校验remindtime范围外的值"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': -1589099880,
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_15(self):
        """校验groupid的值"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': '',
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_16(self):
        """校验groupid范围外的值"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': '',
            'remindType': '0',
            'groupId': 1
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())


    def testCase_17(self):
        """校验groupid范围外的值"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': '',
            'remindType': '0',
            'groupId': '20000000000'
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_18(self):
        """校验groupid范围外的值"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': self.userId1,
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': '',
            'remindType': '0',
            'groupId': '牛逼'
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

