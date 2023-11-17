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
class DeleteTrash(unittest.TestCase):
    path = '/v3/notesvr/cleanrecyclebin'
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    expr = {
        'responseTime': int
    }

    def setup(self0):
        print()

    def teardown(self):
        print()

    def Case_01(self):
        """校验noteid的值"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            {'noteIds': ['3e1f2c75d182bfee666d3046cd518a1d']}
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.text)
        print(res.status_code)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def Case_02(self):
        """校验noteid的值"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            {'3e1f2c75d182bfee666d3046cd518a1d'}
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.text)
        print(res.status_code)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def Case_03(self):
        """当id为-2时"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            {'noteIds': ['-2']}
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.text)
        print(res.status_code)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())
