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
                        "contentUpdateTime": int, "title": str, 'valid': int}]
    }

    def setUp(self):
        print("test start")

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self):
        """4.获取便签内容的主流程"""
