#!usr/bin/env python
# -*- coding:utf-8
'''
Create on 2017/7/15
author:Zheng Huang
'''

import time, datetime

from django.core.management import BaseCommand


from voice_notifier.models import NsData, OnData, SaData
from django.conf import settings
from voice_notifier.voice_notifier import VoiceNotifier
from voice_notifier.py_voice_notifier import PyVoiceNotifier


class Command(BaseCommand):
    """数据库扫描"""

    def handle(self, *args, **options):

        while True:
            data_to_check = NsData.objects.last().key_word

            if not self.check_data(data_to_check):
                # 语音通知
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # 语音模板审核中，通过后开启。
                # PyVoiceNotifier.send_voice_notify(timestamp)
                # PyVoiceNotifier.send_voice_captcha(timestamp)
                data_to_check.delete()

            if NsData.objects.all().__len__() > 1000:
                NsData.objects.all().delete()

            time.sleep(120)

    def check_data(self, data_to_check):
        if data_to_check == settings.NS_DATA:
            return True
        else:
            return False
