#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: diange.du
@file: time_demo.py
@time: 2020/9/9 18:45
@desc: 时间 demo
'''

# 三种形式：
#
# 时间戳(timestamp)：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。
# 格式化的时间字符串(Format String)
# 结构化的时间(struct_time)：struct_time元组共有9个元素共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时)

import time

a = time.time()   #
b = time.strftime('%Y-%m-%d %X %p')
c = time.strftime('%Y-%m-%d %H:%M:%S')
d = time.localtime()   #结构化时间

print(a)
print(b)
print(c)
print('结构化时间:',d)
# print(d.tm_year)  #单独得到特定值


#datatime模块
import datetime

a = datetime.datetime.now()
print('datetime时间：', a)

# 计算三天后是什么时间
b = datetime.datetime.now() + datetime.timedelta(days=3)
print('计算三天后是什么时间', b)


#时间之间的转换
print('---------------------时间之间的转换----------------------')
#需求：当前得到一个格式化字符串的时间数据：2020-05-03 15:48:16  。在这个时间的基础加算7天后是什么时间

#第一步：
struct_time = time.strptime('2020-05-03 15:48:16', '%Y-%m-%d %H:%M:%S') #这里转成结构化时间
timestamp = time.mktime(struct_time) + 7*24*3600  #这里得到最后7点后的时间戳的时间

#第二步：转回去
res = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
print('最后得到7天后的时间是：', res)


print(datetime.datetime.now())  # 返回 2020-09-10 10:43:42.734159
print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转成日期格式 2020-09-10
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分

c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=2))  # 时间替换
