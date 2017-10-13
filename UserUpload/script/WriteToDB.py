# coding=utf-8
import xlrd
from Resourcesmanagement.models import ApplicationDomainTable,ApplicationTable
from IPaddrmanagement.models import CDNmanagementIpTable
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def WriteDataToDB(WriteDBData,DBtable='ApplicationDomainTable' ):
    writeDB=0
    errorDB=0
    repeatData=0
    ReturnRepeatData=[]
    ReturnErrorDate=[]
    VIEWDATA=[]
    # 调度控制域名表
    if DBtable == "ControlDomainTable":
        pass
    # 调度控制ip表
    elif DBtable == "ControlIpTable":
        pass
    # 应用域名表
    elif DBtable == 'ApplicationDomainTable':
        for i in WriteDBData:
            try:
                appdomain=ApplicationDomainTable.objects.get_or_create(domain=i[0],app=i[1],region=i[3],res_type=i[4],resourcescover=i[5])
                if appdomain[1]:
                    appdomain[0].save()
                    writeDB+=1
                else:
                    repeatData+=1
                    #repeatinfo=str(i[0])+','+'重复'
                    #ReturnRepeatData.append(str(i[0]))
            except Exception,e:
                errorDB+=1
                #errrorinfo=str(i[0])+','+'写入错误'+str(e)
                errrorinfo=str(i[0])
                ReturnErrorDate.append(errrorinfo)
        VIEWDATA.append(str(repeatData))
        VIEWDATA.append(ReturnErrorDate)
        return VIEWDATA
    #cp管理地址
    elif DBtable == "cdnmanagementiptable":
        for i in WriteDBData:
            try:
                managementip=CDNmanagementIpTable.objects.get_or_create(CDN=i[0],ManagementIp=i[1],Remarks=i[2])
                if managementip[1]:
                    managementip[0].save()
                    writeDB+=1
                else:
                    repeatData+=1
                    #repeatinfo=str(i[0])+','+'重复'
                    #ReturnRepeatData.append(str(i[0]))
            except Exception,e:
                errorDB+=1
                #errrorinfo=str(i[0])+','+'写入错误'+str(e)
                errrorinfo=str(i[0])
                ReturnErrorDate.append(errrorinfo)
        VIEWDATA.append(str(repeatData))
        VIEWDATA.append(ReturnErrorDate)
        return VIEWDATA
    elif DBtable == "ApplicationTable":
        for i in WriteDBData:
            try:
                managementip=ApplicationTable.objects.get_or_create(app=i[0])
                if managementip[1]:
                    managementip[0].save()
                    writeDB+=1
                else:
                    repeatData+=1
                    #repeatinfo=str(i[0])+','+'重复'
                    #ReturnRepeatData.append(str(i[0]))
            except Exception,e:
                errorDB+=1
                #errrorinfo=str(i[0])+','+'写入错误'+str(e)
                errrorinfo=str(i[0])
                ReturnErrorDate.append(errrorinfo)
        VIEWDATA.append(str(repeatData))
        VIEWDATA.append(ReturnErrorDate)
        return VIEWDATA
    elif DBtable == "":
        pass
    elif DBtable == "":
        pass