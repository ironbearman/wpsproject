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

url = 'http://note-api.wps.cn/v3/notesvr/set/noteinfo'
headers = {
            'Cookie': 'wps_sid=' + 'V02SNyLn6uPRvyw766S0PAgfuldi4yc00aa4b43c0032f73883',
            'X-user-key':  '855062659',
            'Content-Type': 'application/json',
        }
data = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'star': 0,
            'remindTime': '',
            'remindType': '0',
            'groupId': 0
        }
res = requests.post(url=url, headers=headers, json=data)
print(res.status_code)
print(res.text)
version = res.json()['infoVersion']
print(version)