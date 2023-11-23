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
class DeleteNotes(unittest.TestCase):
    re = Re()
    envConfig = YamlRead().env_config()
    userId1 = envConfig['userIds']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    dataConfig = YamlRead().data_config()
    url = host + dataConfig['interface']['PostdeleteNote']['path']

    def setUp(self):
        CreateGroup.create_group_note(self.userId1, self.sid1, num=1)
        print("test start")

    def tearDown(self) -> None:
        print('tearDown')

    def testCase_01(self):
        """5.软删除便签内容的主流程 必填项缺失"""
        host = self.host
        path = self.path
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {'noteId': ""}

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)

    def testCase_02(self):
        """5.软删除便签内容的主流程 已删除便签id"""
        host = self.host
        path = self.path
        url = host + path
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(self.userId1),
            'Cookie': 'wps_sid=' + self.sid1
        }
        body = {'noteId': "5de81f1f27769b88c77c654c12fe523d"}

        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)

