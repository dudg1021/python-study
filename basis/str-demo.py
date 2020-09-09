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

#9. 字符串方法
# upper ———— 转换为大写
# lower ———— 转换为小写
# title ———— 转换为标题（每个单词首字母大写）
# capitalize ———— 首字母大写
# swapcase ———— 大写变小写，小写变大写

print("how are you".capitalize())

# 字符串反转
print("hello"[::-1])   #  olleh

# 字符串连接
print('-'.join(['hello', 'world']))   # hello-world

# str.replace(old,new[,max]) #old为旧串，new为新串，max可选，为替换次数
print("today is a fine day".replace('fine', 'rainy'))


# isdigit ———— 检测字符串时候只由数字组成
# isalnum ———— 检测字符串是否只由数字和字母组成
# isalpha ———— 检测字符串是否只由字母组成
# islower ———— 检测字符串是否只含有小写字母
# isupper ———— 检测字符串是否只含有大写字母
# isspace ———— 检测字符串是否只含有空格
# istitle ———— 检测字符串是否是标题（每个单词首字母大写）

print("how are you".isdigit())

# 求字符串中最大、最小字符(字母顺序)
print(max('hello'))  # o
print(min('hello'))  # e


# 索引与切片
# 1.索引:得到单个字符:a[0] a[-1] a[len(a)-1]
# 2.切片:取很多字符串:

#1.  a[1:10]

#2. 正步长,负步长:a[1:10:2] a[10:1:-2]

#3. 缺省的时候:

  # a.起始位置缺省:正步长时,默认起始位置为0,
  # 负步长时,默认起始位置为-1:a[:10:2] a[10:1:-2]

# b.结束位置缺省:正步长时,默认结束位置为-1
# 负步长时,默认起始位置为0: a[5::2] 和 a[5::-2]

# 3.字符串运算符: + *

#abcdefg
# 字符串	a	b	c	d	e	f	g
# 正索引	0	1	2	3	4	5	6 (从左到右，第一个元素下标为0，依次往右递增。)
# 逆索引	-7	-6	-5	-4	-3	-2	-1 (从右到左，最后一个元素下标为-1，依次往左递减。)
str = '0123456789'  #str[start:stop:step]   遵循【左闭右开】规则

print(str[0:3])     #截取第一位到第三位之前的字符                 　　　　　　　　　　#012
print(str[1:5])     #截取第二位到第六位之前的字符              　　　　　　　　　　#1234
print(str[:])       #截取字符串的全部字符                     　　　　　　　　   #0123456789
print(str[6:])      #截取第七个字符到结尾                     　　　　　　　   　#6789
print(str[:-3])     #截取从头开始到倒数第三个字符之前           　　　　　　　   　#0123456
print(str[2])       #截取第三个字符                           　　　　　　      #2
print(str[-1])      #截取倒数第一个字符                    　　　　　　　　      #9
print(str[::-1])    #创造一个与原字符串顺序相反的字符串        　　　　　　　  　  #9876543210
print(str[-3:-1])   #截取倒数第三位与倒数第一位之前的字符       　　　　　　　 　  #78
print(str[-3:])     #截取倒数第三位到结尾                    　　　　　　　   　 #789
print(str[:-5:-3])  #逆序截取，步长为3                     　　　　　　　　　　  #96
print(str[9:0:-1])  #逆序截取，起始值为列表的第10为数，到列表第1位数之前的数结束，　　#987654321
print(str[0:12])    #截取全部元素
