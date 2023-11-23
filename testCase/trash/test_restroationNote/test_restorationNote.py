import unittest
import requests
# from parameterized import parameterized
# from common.outputCheck import OutputCheck
from common.ymlRead import YamlRead


class RestorationTrashNote(unittest.TestCase):
    def setUp(self):
        print('setUp')


    def tearDown(self) -> None:
        print('tearDown')

    def testCase01_major(self, yamlres=None):
        """12.恢复回收站下所有便签的主流程"""
        hostenv = YamlRead().env_config()
        host = hostenv['host']
        userid = hostenv['userIds']
        path = f'/v3/notesvr/user/{userid}/notes'
        url = host + path
        headers = {
            'cookie': 'wps_sid=V02S0ZZmInKKXYn-P8XbuKFB1DYECw400ac5dbb80032f73883'
        }
        body = {'noteIds': ["5de81f1f27769b88c77c654c12fe523d"],
                'userIds': userid
                }

        res = requests.patch(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
