
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CompressedTextField(models.TextField):
    """
    model Fields for storing text in a compressed format (bz2 by default)
    """

    def from_db_value(self, value, expression, connection, context):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def to_python(self, value):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value
    def get_prep_value(self, value):
        if not value:
            return value
        try:
            value.decode('base64')
            return value
        except Exception:
            try:
                return value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value



#机房管理表
class ComputerRoomTable(models.Model):

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '机房信息'
        verbose_name_plural = '机房信息'
        #ordering = ['']

    def __unicode__(self):
        return self.pub_date

#服务器信息表
class ServerMachineTable(models.Model):

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '服务器信息'
        verbose_name_plural = '服务器信息'
        #ordering = ['']

    def __unicode__(self):
        return self.pub_date


#网络设备信息表
class NetworkMachineTable(models.Model):

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '网络设备信息'
        verbose_name_plural = '网络设备信息'
        #ordering = ['']

    def __unicode__(self):
        return self.pub_date

#机柜信息表
class CabinetTable(models.Model):

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '机柜信息'
        verbose_name_plural = '机柜信息'
        #ordering = ['']

    def __unicode__(self):
        return self.pub_date