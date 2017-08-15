# coding=utf-8
import xadmin
from .models import PersonnelTatble


#联系人管理
class PersonnelTatbleXAdmin(object):
    list_display = ('CDN','Name','Phone','QQNunmber','Email','Remarks',)
    search_fields = ('Name','CDN__CDN')
    list_filter = ('CDN',)
    # 不显示书签
    show_bookmarks = False
xadmin.site.register(PersonnelTatble,PersonnelTatbleXAdmin)
