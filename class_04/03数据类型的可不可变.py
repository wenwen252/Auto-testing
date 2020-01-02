""" 
============================
  -*- coding:utf-8 -*-
  Author    :稳稳的幸福  
  E_mail    :1107924184@qq.com
  Time      :2019/12/30 20:55
  File      :03数据类型的可不可变.py
============================
 
"""
# -----------------不可变的数据类型----------------
# 数值
a = 10
print(id(a))
a = a + 1
print(a, id(a))

# 字符串
s = "123abc"
print(id(s))
s = s.replace('1', '9')
print(s, id(s))

# 元组
tu = (1, 2, 3)
print(id(tu))
tu = (11, 22, 33) + tu
print(tu, id(tu))

# ------------------可变的数据类型------------------

# 列表
li = [11, 2, 3]
print(id(li))
li.append(44)
print(li, id(li))

# 字典
dic = {"a": 11, "b": 22}
print(id(dic))
dic["c"] = 33
print(dic, id(dic))

# 集合
