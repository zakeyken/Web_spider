#!usr/bin/env python
# -*- coding:utf-8
'''
Create on 2017/7/15
author:Zheng Huang
'''

import datetime, base64, hashlib, requests, json

from django.core.mail import send_mail
from django.conf import settings


class VoiceNotifier(object):
    """语音通知API"""

    @classmethod
    def send_voice_message(self):

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        sig_parameter_text = '{account}{auth_token}{timestamp}'.format(
            account=settings.YZX_ID, auth_token=settings.YZX_AUTH_TOKEN, timestamp=timestamp)
        sig_parameter = hashlib.md5(sig_parameter_text).hexdigest()

        url = 'https://api.ucpaas.com/{version}/Accounts/{accountSid}/Calls/voiceNotify?sig={SigParameter}'.format(
            version=settings.YZX_VERSION, accountSid=settings.YZX_ACCOUNT_SID,
            SigParameter=sig_parameter)

        authorization = base64.b64encode(
            '{id}:{timestamp}'.format(id=settings.YZX_ID, timestamp=timestamp))
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': authorization,
        }

        data = json.dumps({
            'appId': settings.YZX_APP_ID,
            'to': '18982032410',
            'type': '2',
            'playTimes': '2',
            'templateId': '649827',
            'content': '',
        })

        response = requests.post(url, data=data, headers=headers)

        result = json.loads(response)

        if result['respCode'] == '000000':
            return True
        else:
            send_mail(
                subject=u'语音通知失败',
                message=u'语音通知失败了，请检查一下。%s' % timestamp,
                from_email='wknb@sina.com',
                recipient_list=['125203412@qq.com', '88280578@qq.com'],
                fail_silently=True
            )
            return False
