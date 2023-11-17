import requests
from ymlRead import YamlRead
import time

"""批量新增便签"""


class Createnotes():
    hostenv = YamlRead().env_config()
    host = hostenv['host']

    def create_note(self, userid, sid, groupId, num):
        note_info_url = self.host + '/v3/notesvr/set/noteinfo'  # 新建便签主体便签接口
        notepage_url = self.host + '/v3/notesvr/set/notecontent'  # 便签内容接口
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(userid),
            'Cookie': f'wps_sid={sid}',
        }
        # 新增便签主体
        for i in range(num):
            noteId = str(int(time.time() * 1000)) + '_noteId'
            body = {
                'noteID': noteId,
                'groupId': groupId
            }
            res = requests.post(url=note_info_url, headers=headers, json=body)
            infoVersion = res.json()['infoVersion']
            # 新增便签内容
            body_2 = {
                'noteId': noteId,
                'title': 'test',
                'summary': 'test',
                'localContentVersion': infoVersion,
                'BodyType': 0
            }
            requests.post(url=notepage_url, headers=headers, json=body_2)
