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

@class_case_log
class GetNotes(unittest.TestCase):
    path = '/v3/notesvr/get/notebody'
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    expr = {
        'responseTime': int,
        'noteBodies': [{"summary": str, "noteId": str, "bodyType": int, "body": str, "contentVersion": 1,
                        "contentUpdateTime": int,"title": str, 'valid': int}]
    }

    def setUp(self):
        print("test start")

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self):
        """4.获取便签内容的主流程"""

        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {'noteIds': ['3e1f2c75d182bfee666d3046cd518a1d']}

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)

    def testCase_01(self):
        """4.获取便签内容的主流程,多便签"""

        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {'noteIds': ['3e1f2c75d182bfee666d3046cd518a1d', '23b8cd5a00494d5d78519a4407d67ea2']}
        expr = {
            'responseTime': int,
            'noteBodies': [{"summary": str, "noteId": str, "bodyType": int, "body": int, "contentVersion": 1,
                            "contentUpdateTime": int,"title": str, 'valid': int},
                           {"summary": str, "noteId": str, "bodyType": int, "body": int, "contentVersion": 1,
                            "contentUpdateTime": int,"title": str, 'valid': int}]
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(expr, res.json())

