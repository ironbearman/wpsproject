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
        """2.跟新便签内容的主体主流程 remindType0"""
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
        """2.跟新便签内容的主体主流程remindType1"""
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
            'remindType': '1',
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
        """2.跟新便签内容的主体主流程remindType2"""
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
            'remindType': '2',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        version = res.json()['infoVersion']
        print(version)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_04(self):
        """2.跟新便签内容的主体主流程remindType空"""
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
        version = res.json()['infoVersion']
        print(version)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())
