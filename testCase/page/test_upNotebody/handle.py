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


@class_case_log
class CreateNotes(unittest.TestCase):
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    path = '/v3/notesvr/set/noteinfo'
    expr = {
        "responseTime": int,
        'contentVersion': int,
        'contentUpdateTime': int,
    }

    def setUp(self):
        print("test start")

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self):
        """缺失cookie校验"""
        url = self.host + self.path
        headers = {
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
        """过期cookie校验"""
        url = self.host + self.path
        headers = {
            'Cookie': 'wps_sid=wps_sid=V02StLCQuRENqrzRn6ACs_Rgs4J6OYs00aa002b30032f73883',
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


    def testCase_03(self):
        """非法的cookie校验"""
        host = self.host
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=Vsssssss33333ces_Rgs4J6OYs00aa002b30032f73883'

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
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())