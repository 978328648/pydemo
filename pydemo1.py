#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# name = input('please enter your name: ')
print('hello','1024*768=',1024*768)
# name = input()
# print('Hello,', name)
# print('''line1
# line2
# line3''')
# print('''hello,\nworld''')
# print((3>5)==False)

# name = input()
# if name >= 18:
#     print('123',name)
# else:
#     print('321',name)
# print(name)

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)
# print(a)

# n = 123
# f = 1.23456
# s1 = r'hello,"bart"'
# s4 = r'''hello,
# lisa!'''
# print(10/3)
# print(10//3)
# print(10%3)

# age = input()
# print('hello,%s'%(age/2))

# print('%2d-%02d'%(3,1))
# print('32d-102d')
# print('%.2f'%3.1415926)

# int('123')
# float('12.34')
# str(123)
# bool(1) bool('')

# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

# list 数组1
# classmates = ['123','456','789']
# classmates.append('101112') 
# classmates.insert(2,'insert')
# classmates.pop()
# # !!!!!!append向数组最后  insert指定位置添加
# # !!!!!!pop 删除数组最后 也可以删除指定位置
# print(classmates)

# tuple 数组2 不可变的   但是里面可以有list list是可变的
# 不变指的是指向不变
# t = ('a','b',['A','B'])
# t[2][0] = 123
# print(t)
# tuple里只有一个元素后面要加,   
# t = (1,)
# print(t)

# age = input('your name:')
# if age==2100:
#     print('死了')
# elif age>2000:
#     print('00后')
# else:
#     print('00前')

# obj = input('zong:')
# num = 0
# for x in range(obj+1):
#     num = num + x
#     pass
# print(num)

# obj = 0
# num = 99
# while num>0:
#     if num == 95:
#         break
#     obj = obj + num
#     num-=2
# print(obj)

# print(list(range(5))) 
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

# d={'a':1,'b':2,'c':3,'d':4}
# print(d.get('e'))

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TabError('23123')
#     if x > 0:
#         return x
#     else:
#         return -x
# print(my_abs('a'))

import math
def quadratic(a,b,c):
    return (-b+(math.sqrt((b*b)-(4*a*c))))/(2*a),(-b-(math.sqrt((b*b)-(4*a*c))))/(2*a)
# print(quadratic(2,3,1))

def calc(*num):
    for target_list in num:
        print (target_list)
# print(calc(1,2,3))