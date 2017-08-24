# coding=utf-8
import xlrd
import sys
from Resourcesmanagement.models import CDNTable,ApplicationDomainTable,RegionTable,ApplicationTable,restype
reload(sys)
sys.setdefaultencoding('utf-8')
from django import db
#文件读取
def ReadExeclFile(file,tablename):
    FilePath=str(file)
    row_list=[]
    NOTfind=[]
    returnData=[]
    FileData=xlrd.open_workbook(filename=FilePath)
    FileTable=FileData.sheets()[0]
    ExeclRows=FileTable.nrows
    ExeclCols=FileTable.ncols
    # 调度控制域名表
    if tablename == "ControlDomainTable":
        pass
    #cp管理地址表
    elif tablename == "cdnmanagementiptable":
        for i in range(1, ExeclRows):
            rowValues = FileTable.row_values(i)
            try:
                # 查询cdn
                cdn_id = CDNTable.objects.get(CDN=rowValues[0])
                rowValues[0] = cdn_id
                row_list.append(rowValues)
            except Exception, e:
                print e
                # 查找核对错误，[单条记录，错误信息]
                error = rowValues + e
                NOTfind.append(error)
    # 调度控制控制ip表
    elif tablename == "ControlIpTable":
        pass
    # 应用域名表
    elif tablename == 'ApplicationDomainTable':
        for i in range(1, ExeclRows):
            errormsg = []
            rowValues = FileTable.row_values(i)
            # 查询应用
            try:
                app_id = ApplicationTable.objects.get(app=rowValues[1])
            except Exception, e:
                print e
                errormsg.append(rowValues[1])
                errormsg.append('应用查找错误')
                # 查找核对错误，[单条记录，错误信息]
                NOTfind.append(errormsg)
                continue
            # 查询cdn
            try:
                cdn_id = CDNTable.objects.get(CDN=rowValues[2])
            except Exception,e:
                print e
                errormsg.append(rowValues[2])
                errormsg.append('cdn查找错误')
                # 查找核对错误，[单条记录，错误信息]
                NOTfind.append(errormsg)
                continue
            # 查询域
            try:
                region_id = RegionTable.objects.get(region=rowValues[3])
            except Exception, e:
                print e
                errormsg.append(rowValues[3])
                errormsg.append('域查找错误')
                # 查找核对错误，[单条记录，错误信息]
                NOTfind.append(errormsg)
                continue
            # 查询域名类型
            try:
                res_id = restype.objects.get(restype=rowValues[4])
            except Exception, e:
                print e
                errormsg.append(rowValues[4])
                errormsg.append('类型查找错误')
                # 查找核对错误，[单条记录，错误信息]
                NOTfind.append(errormsg)
                continue
            # 原有数据替换为数据库类型
            rowValues[1] = app_id
            rowValues[2] = cdn_id
            rowValues[3] = region_id
            rowValues[4] = res_id
            row_list.append(rowValues)
    elif tablename == 'ApplicationTable':
        for i in range(1, ExeclRows):
            rowValues = FileTable.row_values(i)
            row_list.append(rowValues)
    #返回信息 [[写入数据库数据],[查询错误数据]]
    returnData.append(row_list)
    returnData.append(NOTfind)
    return returnData

