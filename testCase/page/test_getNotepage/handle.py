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
# wps_id校验
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

    def testCase01_major(self):
        """校验过期cookie"""
        userId1 = self.userId1
        startindex = 0
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=V02StLCQuRENqrzRn6ACs_Rgs4J6OYs00aa002b30032f73883'
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase02_major(self):
        """校验非法cookie"""
        userId1 = self.userId1
        startindex = 0
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=特殊J6OYs00aa002b30032f73883'
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase03_major(self):
        """校验没有cookie"""
        userId1 = self.userId1
        startindex = 0
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': ''
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase04_major(self):
        """校验使用其他用户cookie"""
        userId1 = self.userId1
        startindex = 0
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': ''
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())
