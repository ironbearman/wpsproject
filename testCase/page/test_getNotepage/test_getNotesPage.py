import unittest
import requests
import time
from common.ymlRead import YamlRead
from buinessCommon.celearNote import Clearnotes
from common.outputCheck import OutputCheck
from buinessCommon.re import Re
from common.caselog import step, class_case_log
from common.addNotes import Createnotes
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
        Clearnotes().clear_note(self.userId1,self.sid1)
        print('前置删除完成')

    def tearDown(self) -> None:
        print('测试结束')

    def testCase01_major(self):
        """1.获取首页便签的主流程"""
        userId1 = self.userId1
        sid1 = self.sid1
        startindex = 0
        rows = 1
        path = f'/v3/notesvr/user/{userId1}/home/startindex/{startindex}/rows/{rows}/notes'
        cre = Createnotes().create_note(userId1, sid1, num=1)      #创一条便签
        url = self.host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        expr_1 = {
            'responseTime': 0,
            'webNotes': [{"noteId": cre[0],
                          "createTime": int,
                          "star": int,
                          "remindTime": int,
                          "remindType": int,
                          "infoVersion": 1,
                          "infoUpdateTime": int,
                          "groupId": None,
                          "title": str,
                          "summary": str,
                          "thumbnail": None,
                          "contentVersion": int,
                          "contentUpdateTime": int}]
        }
        self.assertEqual(200, res.status_code)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
        self.assertEqual(expr_1["webNotes"][0], res.json()["webNotes"][0],msg='noteID不一致')
        OutputCheck().assert_output(self.expr, res.json())

