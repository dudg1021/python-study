#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: diange.du
@file: tuple-demo.py
@time: 2020/9/9 16:08
@desc: 元组操作
'''

# 元组 不可变
# 元组定义
tuple1 = (1, 2, 3, 4, 5)
tuple2 = 1, 2
tuple3 = ()


print(tuple1*3)
print(tuple1 + tuple2)
print(type(tuple3))

# 根据下标取值
print(tuple1[3:])

# tuple.index(obj)：从元组中找出某个值第一个匹配项的索引值
print(tuple1.index(3))

# tuple.count(obj)： 统计某个元素在元组中出现的次数
print(tuple1.count(2))

# len(tup): 返回元组中元素的个数
print(len(tuple1))
# max(tup): 返回元组中元素最大的值
print(max(tuple1))
# min(tup): 返回元组中元素最小的值
print(min(tuple1))
# tuple(seq): 将列表转化为元组
list1 = [1, 2, 3, 4, 5, 6]
list_to_tuple = tuple(list1)
print(type(list_to_tuple))
print(list1)
print(list_to_tuple)
