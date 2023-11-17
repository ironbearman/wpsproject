import time
import requests
from common.ymlRead import YamlRead

"""批量新增分组以及分组下的便签"""


class CreateGroup:
    envConfig = YamlRead.env_config()
    host = envConfig['host']

    def creat_group(self, userid, sid, num):
        url = self.host + '/v3/notesvr/set/notegroup'  # 新建分组接口
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(userid),
            'Cookie': f'wps_sid={sid}',
        }
        group_list = []
        for i in range(num):
            groupId = str(int(time.time() * 1000)) + '_groupId'
            body = {
                'groupId': groupId,
                'groupNmae': 'tset'
            }
            requests.post(url, headers=headers, json=body)
            group_list.append(groupId)
        return group_list

    def create_group_note(self, userid, sid, groupId, num):
        """
        批量新增分组便签的方法
        :param userid:
        :param sid:
        :param groupId:
        :param num:
        :return:
        """
        note_info_url = self.host + '/v3/notesvr/set/noteinfo'  # 新建分组下便签接口
        notepage_url = self.host + '/v3/notesvr/set/notecontent'  # 便签内容接口
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(userid),
            'Cookie': f'wps_sid={sid}',
        }
        # 新增便签主体
        noteIds = []
        for i in range(num):
            noteId = str(int(time.time() * 1000)) + '_noteId'
            body = {
                'noteID': noteId,
                'groupId': groupId
            }
            res = requests.post(url=note_info_url, headers=headers, json=body)
            infoVersion = res.json()['infoVersion']

            body_2 = {
                'noteId': noteId,
                'title': 'test',
                'summary': 'test',
                'localContentVersion': infoVersion,
                'BodyType': 0
            }
            requests.post(url=notepage_url, headers=headers, json=body_2)
            assert res.status_code == 200
            noteIds.append(noteId)

        return noteIds
