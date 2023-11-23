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
    expr={
        'responseTime':int
    }
    def setup(self0):
        print()

    def teardown(self):
        print()

    def major(self):
        "清空回收站"
        url = self.host +self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            {'noteIds': ['3e1f2c75d182bfee666d3046cd518a1d', '23b8cd5a00494d5d78519a4407d67ea2']}
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.text)
        print(res.status_code)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def major_02(self):
        url = self.host +self.path
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
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def major_03(self):
        """当id为-1时，清空"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            {'noteIds': ['-1']}
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.text)
        print(res.status_code)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())




