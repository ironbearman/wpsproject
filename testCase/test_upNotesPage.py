import unittest
import requests
import time
from parameterized import parameterized
from common.outputCheck import OutputCheck


class CreateNotes(unittest.TestCase):
    def setUp(self):
        """获取首页便签的主流程，获取noteid"""
        noteId = "cdad69529683a47cd746e0324614d01b"
        host = 'http://note-api.wps.cn'
        userid = "855062659"
        startindex = 0
        rows = 1
        path = f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = host + path

        headers = {
            'Cookie': 'wps_sid=V02StLCQuRENqrzRn6ACs_Rgs4J6OYs00aa002b30032f73883'
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        version = res.json()
        return version

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self,version):
        """新增便签内容主流程"""
        note_info = setUp()
        note_id = note_info['noteId']
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-User-Key': '855062659',
            'Cookie': 'wps_sid=V02StLCQuRENqrzRn6ACs_Rgs4J6OYs00aa002b30032f73883'
        }
        body = {
            "title": "test_title",
            "summary": "test_summary",
            "body": "测试内容",
            "localContentVersion": version,
            "noteId": "cdad69529683a47cd746e0324614d01b",
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.text)
        print(res.status_code)
