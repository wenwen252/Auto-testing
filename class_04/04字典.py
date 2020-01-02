""" 
============================
  -*- coding:utf-8 -*-
  Author    :稳稳的幸福  
  E_mail    :1107924184@qq.com
  Time      :2019/12/30 21:13
  File      :04字典.py
============================
 
"""

"""
字典：每一个元素都是由一个键值对(key:value)组成
字典的定义：使用花括号来表示

字典中的数据规范：
key:不能重复，只能是不可以变类型的数据（数值，字符串，元组），建议key使用字符串
value:可以是任意类型的数据


字典定义的两种方式：
第一种：
user_info = {"name": "稳稳的幸福", "age": 14, "sex": "女"}

第二种：
user_info = dict(name="稳稳的幸福",age=14,sex="女")


第三种：
data=[("name","稳稳的幸福"),("age",18),("sex","女")]
user_info=dict(data)


li1=[('aa', 11), ('cc', 11), ('bb', 22)]
dict1=dict(li1)
"""

user_info = {"name": "稳稳的幸福", "age": 14, "sex": "女"}

name = user_info["name"]
print(age)
#
# # key重复的话，则取最后一个键值对
# dic = {"a": 11, "a": 111, "a": 1111}
# print(dic)


