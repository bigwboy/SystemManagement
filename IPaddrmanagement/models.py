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


#互联资源表
class InternetResoucesTatble(models.Model):
    CDN = models.ForeignKey('Resourcesmanagement.CDNTable')
    InternetAddsegment = models.CharField(u'互联IP段', max_length=40)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '互联资源列表'
        verbose_name_plural = '互联资源列表'
        unique_together = ['InternetAddsegment']
        ordering = ['InternetAddsegment']

    def __unicode__(self):
        return self.CDN.CDN + '\n' + self.InternetAddsegment

#华通出口表
class WatoneExportIpTable(models.Model):
    ExportAddsegment = models.CharField(u'出口地址',max_length=40)
    Province = models.CharField(u'省份', max_length=40)
    City = models.CharField(u'城市', max_length=40)
    AccessOperator = models.CharField(u'接入运营商', max_length=40)
    BackboneTransmission = models.CharField(u'骨干传输', max_length=40)
    ASNumber = models.IntegerField(u'AS号',null=True,blank=True)
    NetworkType = models.ForeignKey('NetTypeTable', verbose_name='网络类型')
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '华通出口地址列表'
        verbose_name_plural = '华通出口地址列表'
        unique_together = ['ExportAddsegment']
        ordering = ['ExportAddsegment']

    def __unicode__(self):
        return self.ExportAddsegment

#cdn管理地址表
class CDNmanagementIpTable(models.Model):
    CDN = models.ForeignKey('Resourcesmanagement.CDNTable')
    ManagementIp = models.CharField(u'CDN管理IP', max_length=40)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = 'cp管理地址表'
        verbose_name_plural = 'cp管理地址表'
        unique_together = ['ManagementIp']
        ordering = ['ManagementIp']

    def __unicode__(self):
        return   self.ManagementIp

#回源出口管理表
class BacktoSounceExportTable(models.Model):
    AddressSegment = models.CharField(u'回源地址段',max_length=40,unique=True)
    Province = models.CharField(u'省份', max_length=40)
    City = models.CharField(u'城市', max_length=40)
    BackboneTransmission = models.CharField(u'骨干传输', max_length=40,null=True,blank=True)
    ASNumber = models.IntegerField(u'AS号',null=True,blank=True)
    NetworkType = models.ForeignKey('NetTypeTable',verbose_name='网络类型')
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '回源出口表'
        verbose_name_plural = '回源出口表'
        ordering = ['AddressSegment']

    def __unicode__(self):
        return self.AddressSegment

class NetTypeTable(models.Model):
    NetType=models.CharField(u'网络类型',max_length=40)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '网络类型表'
        verbose_name_plural = '网络类型表'

    def __unicode__(self):
        return self.NetType

class ServerIPTable(models.Model):
    ServerAddress=models.CharField(u'服务ip',max_length=40)
    CDN = models.ForeignKey('Resourcesmanagement.CDNTable')
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '具体服务表'
        verbose_name_plural = '具体服务表'

    def __unicode__(self):
        return self.ServerAddress