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
        'webNotes': [{ "noteId": str,"createTime": str, "star": int, "remindTime": str, "remindType": 1,
                        "infoVersion": int,"infoUpdateTime": str, 'groupId': int,'title': str,'summary':str,
                       'thumbnail':str,'contentVersion':int,'contentUpdateTime':int}]
    }

    def setUp(self):
        print("test start")

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self):
        """10查看日历下的便签的主流程"""
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {
            'remindStartTime': '1696089600000',
            'remindEndTime': '1698768000000',
            'startIndex': 0,
            'rows': 300
        }

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())