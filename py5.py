# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

l = [1,2,3,5,5,6,4,5]
# def f(x):
#     return x * x
# r = map(f,l)
# r = map(str,l)




# dig = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def intFun(s):
#     def axx(x,y):
#         return x * 10 + y
#     def char(s):
#         return dig[s]
#     return reduce(axx,map(char,s))

# print intFun('165498651')


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name
L2 = list(map(normalize, L1))
print(L2)
