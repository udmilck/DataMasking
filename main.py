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


# print("值:\n{0}".format(getStrAsMD5('参字第1234567号')))
df=pd.read_excel('test.xlsx')
ids=df['身份证件'].values
names=df['户名'].values
print(df['身份证件'].str)
# 身份证号, 1/2代处理
RegExp='(^\d{8}(0\d|10|11|12)([0-2]\d|30|31)\d{3}$)|(^\d{6}(18|19|20)\d{2}(0[1-9]|10|11|12)([0-2]\d|30|31)\d{3}(\d|X|x)$)'
ids= df['身份证件'].replace(RegExp,df['身份证件'], regex=True)
# 警官证处理
# ids= df['身份证件'].replace('^[\u4E00-\u9FA5]{2}$','test', regex=True)
print("值:\n{0}".format(ids))
# print("值:\n{0}".format(names))
#户名处理
# names= df['户名'].replace('^[\u4E00-\u9FA5]{2,3}$',df['户名'].str[-1], regex=True)
# print("值:\n{0}".format(names))
