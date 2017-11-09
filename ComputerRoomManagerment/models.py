
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
    ComputerRoomName = models.CharField(u'机房名称', max_length=40)
    ComputerRoomAddress = models.CharField(u'机房位置', max_length=200)
    ComputerRoomPhone = models.CharField(u'联系电话', max_length=40)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '机房信息'
        verbose_name_plural = '机房信息'
        #ordering = ['']

    def __unicode__(self):
        return self.ComputerRoomName

#服务器信息表
class ServerMachineTable(models.Model):
    #机器名称
    ManufacturersName=models.ForeignKey('EquipmentManufacturersTable')
    ManufacturersType=models.CharField(u'机器型号', max_length=100)
    SNNumber= models.CharField(u'SN号', max_length=100)
    DiskType = models.CharField(u'硬盘类型', max_length=20)
    DiskSize= models.CharField(u'硬盘大小', max_length=20)
    #端口数
    #内存
    CDN = models.ForeignKey('Resourcesmanagement.CDNTable')
    #网络端口
    #链接的网络设备
    #所在机柜
    #备注
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
    CabinetName = models.ForeignKey('CabinetTable')
    #设备型号
    #端口数
    Remarks = models.TextField(u'备注', null=True, blank=True)
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
    CabinetName = models.CharField(u'机柜名称', max_length=40)
    ComputerRoomName = models.ForeignKey('ComputerRoomTable')
    CabinetSize = models.CharField(u'机柜高度', max_length=40)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '机柜信息'
        verbose_name_plural = '机柜信息'
        #ordering = ['']

    def __unicode__(self):
        return self.CabinetName
#设备厂商表
class EquipmentManufacturersTable(models.Model):
    ManufacturersName= models.CharField(u'厂商名称', max_length=40)
    Remarks = models.TextField(u'备注', null=True, blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '设备厂商'
        verbose_name_plural = '设备厂商'
        # ordering = ['']

    def __unicode__(self):
        return self.ManufacturersName