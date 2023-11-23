import requests
import json
from common.caselog import info, error

"""封装了一个请求方法"""


class Re:
    @staticmethod
    def post(url, body, sid, userId, headers=None):
        if headers is None:
            headers = {
                'Content-Type': 'application/json',
                'Cookie': f'wps_sid={sid}',
                'X-user-key': str(userId)
            }
        info(f're url: {url}')
        info(f're headers: {json.dumps(headers)}')
        info(f're body: {json.dumps(body)}')
        try:
            res = requests.post(url=url, headers=headers, json=body, timeout=3)
        except TimeoutError:
            error(f'{url} api requests timeout!')
            return 'timeout'

        info(f'res code: {res.status_code}')
        info(f'res body: {res.text}')
        return res

    def get(self):
        pass
