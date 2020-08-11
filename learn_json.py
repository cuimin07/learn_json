# -*- coding: utf-8 -*-
# @File    : learn_json.py
# @Date    : 2020-08-06
# @Author  : CuiMin
import json

# Python 字典数据转为json对象
data = {
    'no': 1,
    'name': 'zhangwei',
    'url':'www.zhangweishihundan.com'
}
json_str = json.dumps(data)
print("python原始数据：", repr(data))
print("json对象：", json_str)





















