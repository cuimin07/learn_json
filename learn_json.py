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

# 写入JSON数据
with open('data.json', 'w') as f:
    json.dump(data, f)


# 读取json数据
with open('data.json', 'r') as f:
    data2 = json.load(f)

print('json数据为：', data2)


















