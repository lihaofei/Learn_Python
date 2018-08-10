#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bill Li

import copy

names = ["Jack Chen","Jack Ma",'Bill Gates','Rose','Jack']
# print(names[0:3]) # 顾头不顾尾
# print(names[0:-1:2]) # 从0切到最后一位，以2的距离跳
# print(names[-1])
# print(names[-3:-1]) # 不能-1 到 -3 只能-3 ，-1只能从左向右进行
# names.pop()
# names.insert(1,'cheng')
# names.append('lei feng')
# print(names.index("Jack Chen"))
# print(names[0:-2:5])
# print(names[0:1:2])
# print(names.count('Bill Gates'))
# print(names.clear())
# names.reverse()
# names.sort()
# print(names)
# print(names)
# names2=copy.deepcopy(names)
# print(names2)
# print(names)
# names3=['li','wang','sun']
# del names3
# names.extend(names3)
# print(names)
# names.remove('li')
# print(names)

# 浅copy
person=['name',['a',100,26]]
# # method1
# p1=copy.copy(person)
# # method2
# p2=person[:]
# # method3
# p3=list(person)
# print(p1)
# print(p2)
# print(p3)


# 浅copy一般用于联合账号的创建
p3=person[:]
p4=person[:]
p3[0]='li'
p4[0]='liuyifei'
# print(p3)
# print(p4)

p3[1][1]=60
p3[1][2]=27
p3[1][0]='b'
print(p3)
print(p4)