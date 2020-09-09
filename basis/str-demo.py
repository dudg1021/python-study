#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: diange.du
@file: str-demo.py
@time: 2020/8/26 17:02
@desc:
'''


#1. title 首字母转大写
print("(hello world)".title())

#2. 原始字符串 前缀+r
print(r'c:\now')

#3. 百分比%表示字符串 %s :格式化字符串  %d：格式化整数 %f:格式化浮点数字，可指定小数点后的精度
print('Hello,%s' % 'world')
print('%d %f %.2f' % (2019, 2.010, 2011))

#4. 模板化字符串
from string import Template

tmpl = Template("Hello, $who? $year")
print(tmpl.substitute(who="world", year=2020))

#5. 变量与替换字段同名
h = "hello"
m = "world"
print(f'{h},{m}')

#6. format,替换字符串用{}
print('{},{}'.format('hello', 'world'))
print('{1}, {0}, {1}'.format('a', 'b'))
print('{w}, {h}, {w}'.format(h='a', w='b'))

#7. #符号 对于二进制、八进制、十六进制将加上前缀,对于是兼职，加上小数点
print('{0:b}, {0:o}, {0:x}, {0:d}'.format(10))
print('{0:#b}, {0:#o}, {0:#x}, {0:#d}'.format(10))

#8. 千分比分隔符 用逗号分隔
print('{:,}'.format(123123123123))
