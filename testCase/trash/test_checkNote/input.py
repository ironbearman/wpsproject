import yaml
from main import ENVIO, Dri
import unittest
import requests
from common.ymlRead import YamlRead
from buinessCommon.celearNote import Clearnotes
from common.outputCheck import OutputCheck
# from parameterized import parameterized
from buinessCommon.re import Re
from common.caselog import step, class_case_log
from buinessCommon.creatGroup import CreateGroup


class CheckTrashNote(unittest.TestCase):
    path = '/v3/notesvr/cleanrecyclebin'
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
        print('tearDown')

    def testCase02_major(self):
        """11.rows为字符串"""
        userid = self.userId1
        startindex = 0
        rows = '1'
        path = f'/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase03_major(self):
        """11.rows为字符串"""
        userid = self.userId1
        startindex = 0
        rows = '1'
        path = f'/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase04_major(self):
        """11.rows为空字符串"""
        userid = self.userId1
        startindex = 0
        rows = ''
        path = f'/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase05_major(self):
        """11.rows为空"""
        userid = self.userId1
        startindex = 0
        rows = None
        path = f'/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase06_major(self):
        """11.rows为字符串"""
        userid = self.userId1
        startindex = 0
        rows = '你好abc'
        path = f'/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase07_major(self):
        """11.rows为空"""
        userid = self.userId1
        startindex = 0
        path = f'/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/notes'
        url = self.host + path
        headers = {
            'cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    def testCase08_major(self):
        """11.rows为字符串"""
        userid = self.userId1
        startindex = 0
        rows = '你好abc'
        path = f'/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path
        headers = {
            'cookie': 'wps_sid=' + self.sid1
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        self.assertEqual(400, res.status_code, msg=f'状态码异常，返回体{res.text}')
        OutputCheck().assert_output(self.expr, res.json())

    




