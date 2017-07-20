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
from voice_notifier.py_voice_notifier import PyVoiceNotifier


class Command(BaseCommand):
    """数据库扫描"""

    def handle(self, *args, **options):
        phone_list = ['18982032410', '18982032400']
        template_id = 1875398
        while True:
            data_query = NsData.objects.last()
            data_to_check = data_query.key_word
            timestamp = datetime.datetime.now().strftime('%Y年%m月%d日%H点%M分')
            if not self.check_data(data_to_check):
                for phone_number in phone_list:
		    # 语音通知
                    PyVoiceNotifier.send_voice_notify(phone_number, timestamp, template_id)
                    data_query.delete()

            if NsData.objects.all().__len__() > 1000:
                NsData.objects.all().delete()

            time.sleep(30)

    def check_data(self, data_to_check):
        if data_to_check == settings.NS_DATA:
            return True
        else:
            return False
