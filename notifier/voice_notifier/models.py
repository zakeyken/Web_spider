from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class NsData(models.Model):
    crawl_time = models.DateTimeField(blank=True, null=True)
    key_word = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ns_data'


class OnData(models.Model):
    crawl_time = models.DateTimeField(blank=True, null=True)
    key_word = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'on_data'


class SaData(models.Model):
    crawl_time = models.DateTimeField(blank=True, null=True)
    key_word = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sa_data'
