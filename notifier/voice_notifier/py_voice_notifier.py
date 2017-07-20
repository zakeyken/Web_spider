#!usr/bin/env python
# -*- coding:utf-8
'''
Create on 2017/7/16
author:Zheng Huang
'''
import datetime, requests

from django.core.mail import send_mail

from django.conf import settings


def send_email_when_fail(subject, content, recipient_list):
    """发送失败通知邮件"""
    send_mail(
        subject=subject,
        message=content,
        from_email='wknb@sina.com',
        recipient_list=recipient_list,
        fail_silently=True
    )


class PyVoiceNotifier(object):
    """片云API"""

    @classmethod
    def send_voice_notify(self, phone_number, time, template_id):
        """发送语音通知"""

        url = 'https://voice.yunpian.com/v2/voice/tpl_notify.json'

        data = {
            'apikey': settings.PY_API_KEY,
            'mobile': phone_number,
            'tpl_id': template_id,
            'tpl_value': u'time=%s' % time,
        }

        response = requests.post(url, data)

        if response.status_code == 200:
            print (response.json())
            return True

        else:
            send_email_when_fail(u'通知失败',
                                 u'%s 语音通知失败' % time,
                                 ['125203412@qq.com', '88280578@qq.com'])
            return False


    @classmethod
    def send_voice_captcha(self, time):

        url = 'https://voice.yunpian.com/v2/voice/send.json'

        data = {
            'apikey': settings.PY_API_KEY,
            'mobile': '18982032410',
            'code': '1234',
        }

        response = requests.post(url, data)

        if response.status_code == 200:
            return True
        else:
            send_email_when_fail(u'通知失败',
                                 u'%s 语音验证码发送失败' % time
                                 ['125203412@qq.com', '88280578@qq.com'])
            return False
