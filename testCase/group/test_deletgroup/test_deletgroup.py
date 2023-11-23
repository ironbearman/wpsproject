import unittest
import requests
import time


# from parameterized import parameterized
# from common.outputCheck import OutputCheck

class DeleteGroup(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self):
        """9.删除分组的主流程"""
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/delete/notegroup'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': '855062659',
            'cookie': 'wps_sid=V02S0ZZmInKKXYn-P8XbuKFB1DYECw400ac5dbb80032f73883'
        }
        body = {
                'groupId':'f349164c304fbbe3f4f2a7340cb34ea0'
                }

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)