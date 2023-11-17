import requests
from common.ymlRead import YamlRead


class Clearnotes:
    """
    清空用户下便签数据
    """

    envConfig = YamlRead.env_config()
    host = envConfig['host']

    def clear_note(self, userid, sid):

        get_note_url = self.host + f'/v3/notesvr/user/{userid}/home/startindex/0/rows/999/notes'  # 获取首页便签列表
        delete_note_url = self.host + '/v3/notesvr/delete'  # 软删除便签
        clear_note_url = self.host + 'v3/notesvr/cleanrecyclebin'  # 清空回收站
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(userid),
            'Cookie': f'wps_sid={sid}',
        }
        res = requests.get(get_note_url, headers=headers)
        print(res.text)

        note_ids = []
        for item in res.json()['webNotes']:
            note_ids.append(item['noteId'])

            # 删除便签
        for noteId in note_ids:
            body = {
                'noteis': noteId
            }
            res0 = requests.post(delete_note_url, headers=headers, json=body)
            #assert res0.status_code == 200

        clear_body = {
            'noteId': [-1]
        }

        res1 = requests.post(clear_note_url, headers=headers, json=clear_body)
        assert res1.status_code == 200
