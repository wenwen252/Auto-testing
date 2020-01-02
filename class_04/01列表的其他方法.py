""" 
============================
  -*- coding:utf-8 -*-
  Author    :稳稳的幸福  
  E_mail    :1107924184@qq.com
  Time      :2019/12/30 20:14
  File      :01列表的其他方法.py
============================
 
"""

"""
列表查找的方法：
index：根据元素查找对于的下标（如果找不到，报错）
count:查找某个元素在列表中出现的次数

列表中修改元素
通过下标指定元素赋值

列表中其他方法
sort:排序
reverse：列表反向（倒序/反转）
copy：复制列表

内置函数：id 查看数据内存地址

"""

# li = [1, 2, 3, 11, 22, 33, 44, 1]
# # 根据元素查找对于的下标
# res = li.index(11)
# print(res)
#
# # 如果有两个相同的元素，返回第一个元素所在下标
# res = li.index(1)
# print(res)
#
# # 找不到报错：ValueError: 111 is not in list
# res = li.index(14)
# print(res)

# li = [1, 2, 3, 11, 22, 33, 44, 1]
# # 查找指定元素的个数
# res2 = li.count(1)
# #查找不在列表中援助的则返回0
# res3 = li.count("a")
# print(res2)
# print(res3)

# li = [1, 2, 3, 11, 22, 33, 44, 1]
# # 通过下标获取到列表中对应的元素，进行重新赋值
# li[3] = 999
# # 下标不能超过原来的长度 ，否则报错：IndexError: list assignment index out of range
# # li[23] = 444
# print(li)

# # 列表排序
# li = [2554, 7, 58, 96, 36, 526, 4, 85]
# # 从小到大进行排序，没有返回值(列表排序时，列表中必须全部是数值型数据,否则报错！！)
# li.sort()
# print(li)
#
# # 从大到小排序
# li.sort(reverse=True)
# print(li)

# li = [2554, 7, 58, 96, 36, 526, 4, 85]
# # 列表反向
# li.reverse()
# print(li)
#
#
# copy:只是复制值，内存地址不一样
li0 = [1, 2, 3]
li1 = li0
li2 = [1, 2, 3]
li3 = li0.copy()
print(li0, id(li0))
print(li1, id(li1))
print(li2, id(li2))
print(li3, id(li3))
