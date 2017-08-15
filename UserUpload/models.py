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


#用户上传信息保存
class UploadFileTable(models.Model):
    UserName = models.CharField(u'姓名', max_length=40)
    FileName = models.FileField(u'文件名',upload_to='./useruploadfile/')
    TableName = models.CharField(u'操作对象',max_length=30)
    pub_date = models.DateTimeField(u'上传时间', auto_now_add=True, editable=True)

    class Meta:
        verbose_name = '用户上传文件'
        verbose_name_plural = '用户上传文件'
        ordering = ['UserName']

    def __unicode__(self):
        return self.UserName


