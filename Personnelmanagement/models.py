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



#cp联系人管理表
class PersonnelTatble(models.Model):
    CDN = models.ForeignKey('Resourcesmanagement.CDNTable')
    Name = models.CharField(u'姓名', max_length=40,unique=True)
    Phone = models.CharField(u'电话', max_length=40,null=True,blank=True)
    QQNunmber = models.BigIntegerField(u'QQ号',null=True,unique=True,blank=True)
    Email = models.EmailField(u'邮箱',null=True,blank=True)
    Remarks = models.TextField(u'备注',null=True,blank=True)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '联系人信息'
        verbose_name_plural = '联系人信息'
        ordering = ['Name']

    def __unicode__(self):
        return self.Name
