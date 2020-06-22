import hashlib

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import os

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print('--- folder mk ---')
    else:
        print('--- folder exists ---')

def getFileList(path):
    return os.listdir(path)

# md5转换
def getStrAsMD5(parmStr):
    if isinstance(parmStr, str):
        # 转utf-8
        parmStr = parmStr.encode("utf-8")
    m = hashlib.md5()
    m.update(parmStr)
    return m.hexdigest()

# data masking https://segmentfault.com/a/1190000021080227?utm_source=tag-newest
def editExl(path, name):
    if os.path.exists(path):
        df = pd.read_excel(path+name+'.xlsx', formatting_info=True)
    else:
        df = pd.read_excel(name+'.xlsx',formatting_info = True)
    # id
    id = df['身份证件']
    # name
    names = df['户名']

    # 身份证号, 1/2代处理
    IdReg = '(^\d{8}(0\d|10|11|12)([0-2]\d|30|31)\d{3}$)|(^\d{6}(18|19|20)\d{2}(0[1-9]|10|11|12)([0-2]\d|30|31)\d{3}(\d|X|x)$)'
    id.replace(IdReg, id.apply(lambda x: x[0:6] + getStrAsMD5(x)), inplace=True, regex=True)

    # passport 处理
    preg = '(^[EeKkGgDdSsPpHh]\d{8}$)|(^(([Ee][a-fA-F])|([DdSsPp][Ee])|([Kk][Jj])|([Mm][Aa])|(1[45]))\d{7}$)'
    id.replace(preg, id.apply(lambda x: x[0:6] + getStrAsMD5(x)), inplace=True, regex=True)

    # 军官证处理
    jreg = '(^[\u4E00-\u9FA5](字第)([0-9a-zA-Z]{4,8})(号?)$)'
    id.replace(jreg, id.apply(lambda x: x[0:2] + getStrAsMD5(x)), inplace=True, regex=True)

    # 警官证处理
    policereg = '(^[\u4E00-\u9FA5]([0-9a-zA-Z]{7})$)'
    id.replace(policereg, id.apply(lambda x: x[0] + getStrAsMD5(x)), inplace=True, regex=True)

    print("值:\n{0}".format(id.values))
    # 户名处理
    names.replace('^[\u4E00-\u9FA5]{2,3}$', names.str[-1], inplace=True, regex=True)

    # print("值:\n{0}".format(df['户名'].values))

    writer = pd.ExcelWriter('./testresult.xlsx')
    df.to_excel(writer,index=False)
    writer.save()#文件保存
    writer.close()#文件关闭


def editAll():
    originPath = './origin'
    fileList = getFileList(originPath)
    # print(fileList)
    for fileItem in fileList:
        editExl(originPath, fileItem)
editAll()
