import unittest
import requests
from common.ymlRead import YamlRead
from buinessCommon.celearNote import Clearnotes
from common.outputCheck import OutputCheck
# from parameterized import parameterized
from buinessCommon.re import Re
from common.caselog import step, class_case_log
from buinessCommon.creatGroup import CreateGroup


# from parameterized import parameterized
# from common.outputCheck import OutputCheck

class CheckremindNotes(unittest.TestCase):
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    path = '/v3/notesvr/web/getnotes/remind'
    expr = {
        'responseTime': int,
        'webNotes': [{"noteId": str, "createTime": str, "star": int, "remindTime": str, "remindType": 1,
                      "infoVersion": int, "infoUpdateTime": str, 'groupId': int, 'title': str, 'summary': str,
                      'thumbnail': str, 'contentVersion': int, 'contentUpdateTime': int}]
    }

    def setUp(self):
        print("test start")

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self):
        """10查看日历下的便签的主流程 结束时间小于开始时间"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            'remindStartTime': '1698768000000',
            'remindEndTime': '1696089600000',
            'startIndex': 0,
            'rows': 300
        }

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_02(self):
        """10查看日历下的便签的主流程 校验remindtime范围外的值"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            'remindStartTime': '  1589099880',
            'remindEndTime': '1696089600000',
            'startIndex': 0,
            'rows': 300
        }

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_03(self):
        """10查看日历下的便签的主流程 remindStartTime校验负数"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            'remindStartTime': '-1',
            'remindEndTime': '1696089600000',
            'startIndex': 0,
            'rows': 300
        }

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_04(self):
        """10查看日历下的便签的主流程 remindEndTime校验负数"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            'remindStartTime': '1698768000000',
            'remindEndTime': '-1696089600000',
            'startIndex': 0,
            'rows': 300
        }

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_05(self):
        """10查看日历下的便签的主流程 remindEndTime校验范围外的值"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            'remindStartTime': '1698768000000',
            'remindEndTime': ' 1589099880',
            'startIndex': 0,
            'rows': 300
        }

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())


