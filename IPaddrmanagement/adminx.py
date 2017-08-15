# coding=utf-8
import xadmin
from .models import WatoneExportIpTable,InternetResoucesTatble,CDNmanagementIpTable,BacktoSounceExportTable,NetTypeTable

#华通出口ip管理显示
class WatoneExportIpTableXAdmin(object):
    list_display = ('ExportAddsegment', 'Province','City', 'AccessOperator','BackboneTransmission','ASNumber','NetworkType','Remarks',)
    search_fields = ('ExportAddsegment', 'ASNumber','Remarks')
    list_filter = ('BackboneTransmission','NetworkType',)
    show_bookmarks = False
xadmin.site.register(WatoneExportIpTable, WatoneExportIpTableXAdmin)

#互联资源管理显示
class InternetResoucesTatbleXAdmin(object):
    list_display = ('CDN','InternetAddsegment','Remarks',)
    search_fields = ('CDN','InternetAddsegment')
    list_filter = ('CDN','InternetAddsegment')
    # 不显示书签
    show_bookmarks = False
xadmin.site.register(InternetResoucesTatble,InternetResoucesTatbleXAdmin)

#cdn管理地址显示
class CDNmanagementIpTableXAdmin(object):
    list_display = ('CDN', 'ManagementIp', 'Remarks',)
    search_fields = ('CDN', 'ManagementIp')
    list_filter = ('CDN', 'ManagementIp')
    # 不显示书签
    show_bookmarks = False
xadmin.site.register(CDNmanagementIpTable, CDNmanagementIpTableXAdmin)

#回源地址段管理显示
class BacktoSounceExportTableXAdmin(object):
    list_display = (
    'AddressSegment', 'Province', 'City', 'BackboneTransmission', 'ASNumber', 'NetworkType',
    'Remarks',)
    search_fields = ('AddressSegment', 'ASNumber')
    show_bookmarks = False
xadmin.site.register(BacktoSounceExportTable, BacktoSounceExportTableXAdmin)

#出口类型管理显示
class NetTypeTableXAdmin(object):
    list_display = ('NetType','pub_date', 'update_time',)
    show_bookmarks = False
xadmin.site.register(NetTypeTable, NetTypeTableXAdmin)