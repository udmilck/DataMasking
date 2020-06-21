import hashlib
from collections import OrderedDict
from typing import Any, Union

import pandas as pd
from pandas import DataFrame


def getStrasmd5(parmStr):
    if isinstance(parmStr, str):
        # 如果是unicode先转utf-8
        parmStr = parmStr.encode("utf-8")
    m = hashlib.md5()
    m.update(parmStr)
    return m.hexdigest()


df = pd.read_excel('test.xlsx')
ids = df['身份证件'].values
print("值:\n{0}".format(ids))
reg = "(^\d{8}(0\d|10|11|12)([0-2]\d|30|31)\d{3}$)|(^\d{6}(18|19|20)\d{2}(0[1-9]|10|11|12)([0-2]\d|30|31)\d{3}(\d|X|x)$)"
ids = df['身份证件'].replace(reg,getStrasmd5(ids), regex=True)
print("值:\n{0}".format(ids))
# names=df['户名'].values
# print("值:\n{0}".format(ids))
# ids= df['身份证件'].replace('[\u4e00-\u9fa5]{2}+$',getStrAsMD5('12345678'), regex=True)

# print("值:\n{0}".format(names))
# 户名处理
# names= df['户名'].replace('^[\u4E00-\u9FA5]{2,3}$',df['户名'].str[-1], regex=True)
# print("值:\n{0}".format(names))
