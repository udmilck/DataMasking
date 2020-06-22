import hashlib

import  pandas  as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# md5转换
def getStrAsMD5(parmStr):
    if isinstance(parmStr,str):
        # 转utf-8
        parmStr=parmStr.encode("utf-8")
    m = hashlib.md5()
    m.update(parmStr)
    return m.hexdigest()

df=pd.read_excel('test.xlsx')
ids=df['身份证件'].values
names=df['户名'].values

# 身份证号, 1/2代处理
IdReg='(^\d{8}(0\d|10|11|12)([0-2]\d|30|31)\d{3}$)|(^\d{6}(18|19|20)\d{2}(0[1-9]|10|11|12)([0-2]\d|30|31)\d{3}(\d|X|x)$)'
ids= df['身份证件'].replace(IdReg,df['身份证件'].apply(lambda x:x[0:6]+getStrAsMD5(x)), regex=True)
print("值:\n{0}".format(ids))

#passport 处理
preg='(^[EeKkGgDdSsPpHh]\d{8}$)|(^(([Ee][a-fA-F])|([DdSsPp][Ee])|([Kk][Jj])|([Mm][Aa])|(1[45]))\d{7}$)'
ids= df['身份证件'].replace(preg,df['身份证件'].apply(lambda x:x[0:6]+getStrAsMD5(x)), regex=True)
print("值:\n{0}".format(ids))

# 军官证处理
jreg = '(^[\u4E00-\u9FA5](字第)([0-9a-zA-Z]{4,8})(号?)$)'
ids= df['身份证件'].replace(jreg,df['身份证件'].apply(lambda x:x[0:2]+getStrAsMD5(x)), regex=True)
print("值:\n{0}".format(ids))

#警官证处理
policereg = '(^[\u4E00-\u9FA5]([0-9a-zA-Z]{7})$)'
ids= df['身份证件'].replace(policereg,df['身份证件'].apply(lambda x:x[0]+getStrAsMD5(x)), regex=True)
print("值:\n{0}".format(ids))

#户名处理
names= df['户名'].replace('^[\u4E00-\u9FA5]{2,3}$',df['户名'].str[-1], regex=True)
print("值:\n{0}".format(names))
