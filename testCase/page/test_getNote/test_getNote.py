import unittest
import requests
from common.ymlRead import YamlRead
from common.outputCheck import OutputCheck
from buinessCommon.re import Re
from common.caselog import step, class_case_log
from common.addNotes import Createnotes


@class_case_log
class GetNotes(unittest.TestCase):
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    path = '/v3/notesvr/get/notebody'
    expr = {
        'responseTime': int,
        'noteBodies': [{"summary": str,
                        "noteId": str,
                        "bodyType": int,
                        "body": str,
                        "contentVersion": 1,
                        "contentUpdateTime": int,
                        "title": str,
                        'valid': int}]
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

    def testCase_02(self):
        """4.获取便签内容的主流程,多便签"""
        step("STEP: 上传更新便签主体、内容")
        url = self.host + self.path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {'noteIds': ['3e1f2c75d182bfee666d3046cd518a1d', '23b8cd5a00494d5d78519a4407d67ea2']}
        expr = {
            'responseTime': int,
            'noteBodies': [{"summary": str,
                            "noteId": str,
                            "bodyType": int,
                            "body": int,
                            "contentVersion": 1,
                            "contentUpdateTime": int,
                            "title": str,
                            'valid': int},]
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        note_content_info_list = Createnotes.create_note(userid=self.userId1, sid=self.sid1,num=1)
        for i in note_content_info_list:
            noteId = i["noteId"]
            body = {
                "noteIds": [noteId],
            }
            res = self.re.post(self.url, body, self.sid1, self.userId1)
            self.assertEqual(200, res.status_code)
            expr = self.expr
            expr["noteBodies"][0]["summary"] = i["summary"]
            expr["noteBodies"][0]["noteId"] = noteId
            expr["noteBodies"][0]["infoNoteId"] = noteId
            expr["noteBodies"][0]["body"] = i["body"]
            expr["noteBodies"][0]["title"] = i["title"]
            self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')
            OutputCheck().assert_output(expr, res.json())
