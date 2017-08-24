#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from .models import UploadFileTable
from django.core.urlresolvers import reverse
from .script.ReadExecl import ReadExeclFile
from .script.WriteToDB import WriteDataToDB
class UploadFileForm(forms.Form):
    TableName = forms.CharField()
    UploadFile = forms.FileField()

#上传文件并数据记录
def UploadFile(request):
    if request.method == "POST":
        uf = UploadFileForm(request.POST,request.FILES)
        if uf.is_valid():
            #获取表单信息
            uptablename = uf.cleaned_data['TableName']
            upfilename = uf.cleaned_data['UploadFile']
            #文件写入用户上传数据库
            WriteDBCLASS = UploadFileTable()
            WriteDBCLASS.UserName = request.user.username
            WriteDBCLASS.FileName = upfilename
            WriteDBCLASS.save()
            #文件解析内容写入对应表
            print '文件上传成功'
            ReadData = ReadExeclFile(WriteDBCLASS.FileName.name,uptablename)
            WriteDBData = ReadData[0]
            ReadErrorData = ReadData[1]
            if WriteDBData:
                print '文件解析成功'
                returnWritedata=WriteDataToDB(WriteDBData,uptablename)
                return render_to_response('WriteDBover.html',{'ReadErrorData':ReadErrorData,'returnrepeatedata':returnWritedata[0],'returnWriteErrorData':returnWritedata[1]})
            else:
                print WriteDBData
                print '文件解析失败'
                return render(request,'WriteError.html')

    else:
        uf = UploadFileForm()
    return render_to_response('UploadFile.html',{'uf':uf})

