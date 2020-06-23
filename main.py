
from hashlib import md5

import openpyxl

from pandas import read_excel
from pandas import isnull
from pandas import ExcelWriter

from os import listdir
from os import makedirs
from os import removedirs
import os.path as osp

def mkdir(path):
    folder = osp.exists(path)
    if not folder:
        makedirs(path)
        print('--- folder mk ---')
    else:
        print('--- folder exists ---')

def getFileList(path):
    return listdir(path)

# md5转换
def getStrAsMD5(parmStr):
    if isinstance(parmStr, str):
        # 转utf-8
        parmStr = parmStr.encode("utf-8")
    m = md5()
    m.update(parmStr)
    return m.hexdigest()

# data masking
def editExl(path,topath, name):
    df = read_excel(path+ '/' + name, formatting_info=True)


    if '身份证件' in df.columns:
        # id
        id = df['身份证件']

        # 身份证号, 1/2代处理
        IdReg = '(^\d{8}(0\d|10|11|12)([0-2]\d|30|31)\d{3}$)|(^\d{6}(18|19|20)\d{2}(0[1-9]|10|11|12)([0-2]\d|30|31)\d{3}(\d|X|x)$)'
        id.replace(IdReg, id.apply(lambda x: x if isnull(x) else x[0:6] + getStrAsMD5(x)), inplace=True, regex=True)

        # passport 处理
        preg = '(^[EeKkGgDdSsPpHh]\d{8}$)|(^(([Ee][a-fA-F])|([DdSsPp][Ee])|([Kk][Jj])|([Mm][Aa])|(1[45]))\d{7}$)'
        id.replace(preg, id.apply(lambda x: x if isnull(x) else x[0:6] + getStrAsMD5(x)), inplace=True, regex=True)

        # 军官证处理
        jreg = '(^[\u4E00-\u9FA5](字第)([0-9a-zA-Z]{4,8})(号?)$)'
        id.replace(jreg, id.apply(lambda x: x if isnull(x) else x[0:2] + getStrAsMD5(x)), inplace=True, regex=True)

        # 警官证处理
        policereg = '(^[\u4E00-\u9FA5]([0-9a-zA-Z]{7})$)'
        id.replace(policereg, id.apply(lambda x: x if isnull(x) else x[0] + getStrAsMD5(x)), inplace=True, regex=True)

    print("值:\n{0}".format(id.values))

    if '户名' in df.columns:
        # name
        names = df['户名']
        # 户名处理
        names.replace('^[\u4E00-\u9FA5]{2,3}$', names.str[-1], inplace=True, regex=True)


    writer = ExcelWriter(topath + "/" + name)
    df.to_excel(writer,index=False)
    writer.save()
    writer.close()

def editAll(fromPath,toPath):
    originPath = fromPath
    fileList = getFileList(originPath)
    # print(fileList)
    for fileItem in fileList:
        editExl(originPath, toPath,fileItem)
