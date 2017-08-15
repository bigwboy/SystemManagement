# coding=utf-8
import xadmin
from .models import UploadFileTable
from .script.UploadFile import ImportData
#华通出口ip管理显示
class UploadFileTableXAdmin(object):
    list_display = ('UserName','FileName','TableName','pub_date',)
    search_fields = ('UserName', 'FileName','TableName',)
    list_filter = ('UserName','FileName','TableName',)
    show_bookmarks = False
xadmin.site.register(UploadFileTable, UploadFileTableXAdmin)