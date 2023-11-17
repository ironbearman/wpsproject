import unittest
import requests
import time
from common.ymlRead import YamlRead
from buinessCommon.celearNote import Clearnotes
from common.outputCheck import OutputCheck
from parameterized import parameterized
from buinessCommon.re import Re
from common.caselog import step, class_case_log
from buinessCommon.creatGroup import CreateGroup


# import BeautifulReport


@class_case_log
class CreateNotesGroup(unittest.TestCase):
    group_id_empty = [[{"groupId": "", "code": 500}], [{"groupId": None, "code": 403}]]
    must_key = ['groupId', 'groupName']
    envConfig = YamlRead().env_config()

    def setUp(self):
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def testCase01_major(self, yamlres=None):
        """新增分组的主流程"""
        print('用例执行：testCase01_major')
        host = yamlres['host']
        path = '/v3/notesvr/set/notegroup'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': '922061821',
            'Cookie': 'wps_sid=V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd'
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            'groupId': group_id,
            'groupName': 'groupName',
            'order': 1
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg=f'状态码异常，返回体{res.text}')

    @parameterized.expand(group_id_empty)  # 传递参数化的对象，list or tuple
    def testCase02(self, dic):
        """新增分组的groupId枚举值校验"""
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notegroup'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': '922061821',
            'Cookie': 'wps_sid=V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd'
        }
        body = {
            'groupId': dic['groupId'],
            'groupName': 'groupName',
            'order': 1
        }
        print(body)
        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(dic['code'], res.status_code, msg=f'状态码异常，返回体{res.text}')

    @parameterized.expand(must_key)
    def testCase03_input(self, key):
        """必填项字段缺失校验"""
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/set/notegroup'
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': '922061821',
            'Cookie': 'wps_sid=V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd'
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            'groupId': group_id,
            'groupName': 'groupName',
            'order': 1
        }
        body.pop(key)
        print(body)
        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(500, res.status_code, msg=f'状态码异常，返回体{res.text}')
