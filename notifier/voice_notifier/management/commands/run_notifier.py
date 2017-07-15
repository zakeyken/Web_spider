#!usr/bin/env python
# -*- coding:utf-8
'''
Create on 2017/7/15
author:Zheng Huang
'''

import time

from django.core.management import BaseCommand


from voice_notifier.models import NsData, OnData, SaData
from notifier.settings import NS_DATA


class Command(BaseCommand):
    """数据库扫描"""

    def handle(self, *args, **options):
        count = 0

        while True:
            time.sleep(120)
            count += 1
            data_to_check = NsData.objects.last()

            if self.check_data(data_to_check):
                pass
            else:
                # 语音通知
                pass

            if count == 1000:
                NsData.objects.all().delete()
                count = 0

    def check_data(self, data_to_check):
        if data_to_check == NS_DATA:
            return True
        else:
            return False
