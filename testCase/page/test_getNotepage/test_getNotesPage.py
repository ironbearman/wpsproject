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
        """1.获取首页便签的主流程"""
        userId1 = self.userId1
        startindex = 0
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

