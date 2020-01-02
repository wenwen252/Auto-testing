""" 
============================
  -*- coding:utf-8 -*-
  Author    :稳稳的幸福  
  E_mail    :1107924184@qq.com
  Time      :2019/12/27 19:58
  File      :01字符串转义.py
============================
 
"""
"""
\n:换行符-->换行
\t:制表符--->空格（TAB键）
\\:------->\
r：防止转义




"""

s = "python\npython\t1234"
print(s)

# 第一种方式：使用\
s1 = "python\\npython\\t1234"
print(s1)

# 第二种方法：在字符串前面使用r,防止字符串转义（输入的时候是什么样的，打印出来就是什么样的）
s2 = r"python\npython\t1234"
print(s2)

# 使用r防止转义，用于表示路径
file_path = r"c:\apache-jmeter-5.2\backups"
print(file_path)
