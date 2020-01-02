""" 
============================
  -*- coding:utf-8 -*-
  Author    :稳稳的幸福  
  E_mail    :1107924184@qq.com
  Time      :2019/12/27 21:28
  File      :04数据类型的转换.py
============================
 
"""

"""
整数和浮点数转换为字符串：使用str
字符串和浮点数转换为整数：使用int
整数和字符串转换为浮点数：使用float

整数和字符串和浮点数转换为布尔类型：bool

# 注意点：使用字符串转换为int和float时，字符串的内容必须是数字（不能有字母和符号）


"""

a = 19
b = 11.11

s1 = "9999"
print(s1, type(s1))
print(a, type(a))
print(b, type(b))

# 将字符串转换成整数int类型,保证字符串里面的内容是数字
print("----------转化之后——————")
s = int(s1)
print(s, type(s))

将字符串转换成整数float类型
s2 = float(s1)
print(s2, type(s2))

将字符串转换成整数float类型
a1 = str(a)
print(type(a1))

将整数转换成整数float类型
a2

# 使用input输入的数据，接受到的都是字符串类型
