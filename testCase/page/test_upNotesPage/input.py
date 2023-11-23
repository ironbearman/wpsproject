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
class CreateNotes(unittest.TestCase):
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    path = '/v3/notesvr/set/noteinfo'
    expr = {
        "responseTime": int,
        'contentVersion': int,
        'contentUpdateTime': int,
    }

    def setUp(self):
        """获取infoversion的主流程"""
        host = self.host
        path = self.path
        url = host + path
        headers = {
            'Cookie': 'wps_sid=' + self.sid1,
            'X-user-key': str(self.userId1),
            'Content-Type': 'application/json',
        }
        data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': '',
            'remindType': '',
            'groupId': 0
        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.status_code)
        print(res.text)
        global version
        version = res.json()['infoVersion']
        print(version)

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self):
        """3.新增便签内容主流程 title缺失"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "summary": "testsummary",
            "body": "neirong",
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }

        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_02(self):
        """3.新增便签内容主流程 空title"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": "",
            "summary": "testsummary",
            "body": "neirong",
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_03(self):
        """3.新增便签内容主流程 错误类型title"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": 1,
            "summary": "testsummary",
            "body": "neirong",
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_04(self):
        """3.新增便签内容主流程 title过长"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": '99999999999999999999999999999999999999999999999999999999999999999',
            "summary": "testsummary",
            "body": "neirong",
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_05(self):
        """3.新增便签内容主流程 错误类型summary"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": "testtitile",
            "summary": 1,
            "body": "neirong",
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_06(self):
        """3.新增便签内容主流程 必填项summary缺失"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": "testtitile",
            "body": "neirong",
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_07(self):
        """3.新增便签内容主流程 summary空字符串"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": "testtitile",
            "summary": '',
            "body": "neirong",
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_08(self):
        """3.新增便签内容主流程 summary过长"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": "testtitile",
            "summary": '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
            "body": "neirong",
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_09(self):
        """3.新增便签内容主流程 错误类型body"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": "testtitile",
            "summary": 'test',
            "body": 1,
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_10(self):
        """3.新增便签内容主流程 必填项body缺失"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": "testtitile",
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())

    def testCase_11(self):
        """3.新增便签内容主流程 body空字符串"""
        print('用例执行：testCase01_major')
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notecontent'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        data = {
            "title": "testtitile",
            "summary": 'test',
            "body": None,
            "localContentVersion": version,
            "noteId": '58b80a76a3f29962c7fe9ac6a09ea986',
            "BodyType": 0

        }
        res = requests.post(url=url, headers=headers, json=data)
        print(res.text)
        print(res.status_code)
        OutputCheck().assert_output(self.expr, res.json())
