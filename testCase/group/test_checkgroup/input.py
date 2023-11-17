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
class CheckGroupNotes(unittest.TestCase):
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    url = host + dataConfig['interface']['GetGroupNote']['path']
    optionKeys = dataConfig['interface']['GetGroupNote']['optionKeys']
    base = dataConfig['interface']['GetGroupNote']['base']
    assertBase = {
        'responseTime': int,
        'webNotes': [
            {
                'noteId': '',
                'createTime': int,
                'star': 0,
                'remindTime': 0,
                'remindType': 0,
                'infoVersion': int,
                'infoUpdateTime': int,
                'groupId': '',
                'title': 'test',
                'summary': 'test',
                'thumbnail': None,
                'contentVersion': int,
                'contentUpdateTime': int
            }
        ]
    }

    def setUp(self) -> None:
        Clearnotes().clear_note(self.userId1, self.sid1)

    def testCase01(self):
        """8查看分组下的便签的主流程"""
        step('PRE-STEP: 新增一个分组')
        groupIds = CreateGroup.creat_group(self.userId1, self.sid1, 1)
        step('PRE-STEP: 在分组下新增一个便签')
        noteIds = CreateGroup.create_group_note(self.userId1, self.sid1, groupIds[0], 1)
        step('STEP: 查看分组下便签的接口请求')
        body = self.base
        body['groupId'] = groupIds[0]

        res = self.re.post(url=self.url, body=body, userId=self.userId1, sid=self.sid1)
        print(res.text)
        self.assertEqual(200, res.status_code)
        expr = self.assertBase
        expr['webNotes'][0]['noteId'] = noteIds[0]
        expr['webNotes'][0]['groupId'] = groupIds[0]
        OutputCheck().assert_output(expr, res.json())
