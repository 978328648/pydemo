#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pydemo1 import quadratic
# print(quadratic(2,3,1))

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
# print(L[-1:-2])
# J = range(100)
# print(J[0:10:2])

# >>> from collections import Iterable
# >>> isinstance('abc', Iterable) # str是否可迭代
# True
# >>> isinstance([1,2,3], Iterable) # list是否可迭代
# True
# >>> isinstance(123, Iterable) # 整数是否可迭代
# False


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
# def trim(s):
#     if len(s)==0:
#         return s
#     else:
#         while s[0]==' ':
#             s=s[1:]
#             if len(s)==0:
#                 return s
#         while s[-1]==' ':
#             s=s[:-1]
#             if len(s)==0:
#                 return s
#     return s
# # 测试:
# if trim('hello  ') != 'hello':
#     print('1!')
# elif trim('  hello') != 'hello':
#     print('2!')
# elif trim('  hello  ') != 'hello':
#     print('3!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('4!')
# elif trim('') != '':
#     print('5!')
# elif trim('    ') != '':
#     print('6!')
# else:
#     print('7!')


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
# def findMinAndMax(L):
#     if len(L) != 0:
#         (min,max) = (L[0],L[0])
#         for target_list in L:
#             if target_list > max:
#                 max = target_list
#             if target_list < min:
#                 min = target_list
#         return(min,max)
#     else:
#         return (None, None)

# if findMinAndMax([]) != (None, None):
#     print(2)
# elif findMinAndMax([7]) != (7, 7):
#     print(3)
# elif findMinAndMax([7, 1]) != (1, 7):
#     print(4)
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print(5)
# else:
#     print(1)

# print([ x*x for x in range(1,11) if x%2==0])
# print(len([ a+b+c+d+e for a in '12345' for b in '12345' for c in '12345' for d in '12345' for e in '12345']) )

# import os 
# print(os.listdir('.'))

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
# L = ['Hello', 'World', 18, 'Apple', None]
# print( [x.lower() for x in L if isinstance(x,str)] )
