""" 
============================
  -*- coding:utf-8 -*-
  Author    :稳稳的幸福  
  E_mail    :1107924184@qq.com
  Time      :2019/12/27 20:20
  File      :02字符串常用方法.py
============================
 
"""

"""
find方法：查找指定元素的下标位置
count:查找指定元素的个数
repalce:替换的方法
split:分割的方法
upper：把小写的字母串变成大写
lower：把大写的字母变成小写





"""

s = "python1234java5678php"
# # 查找指定元素的下表位置，没有找到返回-1
# res = s.find("4")
# print(res)
# # 如果查找元素有多个，则返回第一个元素的下标位置
# res = s.find('p')
# print(res)
# # 如果查找元素是一个字符串片段，则返回字符串片段的第一个元素的下标位置
# res = s.find("php")
# print(res)
#
# # 查找指定元素的个数,查找不在字符串中字符的则返回0
# s = "python1234java5678php"
# res1 = s.count("p")
# res2 = s.count("z")
# print(res1)
# print(res2)
#
# 替换
# 第一个参数;待替换的字符串片段
# 第二个参数：替换之后的字符串片段
# 第三个参数：默认替换所有的，也可以通过第三个参数来控制

# s = "python1234java5678php"
# res3 = s.replace("p", "aa")
# res4 = s.replace("p", "aa", 1)
# #如果第一个参数不存在字符串中，则返回原字符串
# res5 = s.replace("z", 'r')
# print(res3)
# print(res4)
# print(res5)

# # 字符串分割,返回是列表
# # 第一个参数：分割点
# # 第二个参数：默认找到所有分割点进行分割，也可以通过第二个参数来控制
# s2 = "123aa456aa789aa888aa99"
# res4 = s2.split("aa")
# # a和a之间没有内容就是空字符
# res5 = s2.split("a")
# # 不存在就返回全部
# res6 = s2.split("php")
# print(res4)
# print(res5)
# print(res6)

# # 把小写的字母串变成大写
# s3 = "abc1234"
# res5 = s3.upper()
# print(res5)

# # 把大写的字母变成小写
# s4 = "ASDFee56WXVR"
# res6 = s4.lower()
# print(res6)


# s4 = "ggASDFee56WXVR"
# res7 = s4.title()
# res8 = s4.capitalize()
# print(res7)
# print(res8)
