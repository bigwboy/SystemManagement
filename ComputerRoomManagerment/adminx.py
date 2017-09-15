# -*- coding: utf8 -*-
#time:2017/9/15 下午2:42
#VERSION:1.0
#__OUTHOR__:guangguang


import xadmin
from .models import CabinetTable,ComputerRoomTable,NetworkMachineTable,ServerMachineTable


#机房管理显示
class ComputerRoomTableXAdmin(object):
    list_display = ()
    search_fields = ()
    list_filter = ()
    # 不显示书签
    show_bookmarks = False
xadmin.site.register(ComputerRoomTable,ComputerRoomTableXAdmin)

#机柜管理显示
class CabinetTableXAdmin(object):
    list_display = ()
    search_fields = ()
    list_filter = ()
    # 不显示书签
    show_bookmarks = False
xadmin.site.register(CabinetTable,CabinetTableXAdmin)

#网络设备管理显示
class NetworkMachineTableXAdmin(object):
    list_display = ()
    search_fields = ()
    list_filter = ()
    # 不显示书签
    show_bookmarks = False
xadmin.site.register(NetworkMachineTable,NetworkMachineTableXAdmin)

#服务器管理显示
class ServerMachineTableXAdmin(object):
    list_display = ()
    search_fields = ()
    list_filter = ()
    # 不显示书签
    show_bookmarks = False
xadmin.site.register(ServerMachineTable,ServerMachineTableXAdmin)


#debug
if __name__ == "__main__":
    pass