import json
import requests
from common.ymlRead import YamlRead
import time
from buinessCommon.re import Re

"""批量新增便签"""


class Createnotes():
    re = Re()
    envConfig = YamlRead().env_config()
    host = envConfig['host']

    def create_note(self, userid, sid, num):
        note_info_url = self.host + '/v3/notesvr/set/noteinfo'  # 新建便签主体便签接口
        notepage_url = self.host + '/v3/notesvr/set/notecontent'  # 便签内容接口
        headers = {
            'Content-Type': 'application/json;charset=utf-8',
            'X-user-key': userid,
            'cookie': f'wps_sid=' + sid
        }
        # 第一步：新增便签主体
        noteid = str(int(time.time() * 1000)) + '_noteId'
        for i in range(num):
            data = {
                'noteId':noteid ,
                'star': 0,
            }
            res = requests.post(note_info_url, headers=headers, json=data)
            print(res.text)
            infoVersion = res.json()['infoVersion']
            note_content_info_list = []
            # 第二步新增便签内容

            data_2 = {
                'noteId': noteid,
                'title': 'test',
                'summary': 'test',
                'localContentVersion': infoVersion,
                'BodyType': 0,
                'body':'test'
            }
            res2 = requests.post(url=notepage_url, headers=headers, json=data_2)
            print(res2.text)
            note_content_info = {"noteId": data_2["noteId"], "title": data_2["title"], "body": data_2["BodyType"],
                                 "summary": data_2["summary"]}
            note_content_info_list.append(note_content_info)
        return note_content_info_list



if __name__ == "__main__":
    re = Re()  # 创建类的实例
    envConfig = YamlRead().env_config()
    userId = envConfig['userIds']
    sid = envConfig['sid1']
    Createnotes().create_note(userId, sid, num=1)

