#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bill Li
list1=[1,2,4,1,5,6,8]
list1=set(list1)
print(list1)
list2=set(list([2,4,4,5,67,33,5]))
# 交集
print(list1.intersection(list2))
print(list1&list2)
# 并集
print(list1.union(list2))
print(list1|list2)
# 差集
print(list1.difference(list2))
print(list2.difference(list1))
# 子集
list3=set([1,3,7])
print(list3.issubset(list1))
print(list1.issubset(list3))

# 对称差集
print(list1.symmetric_difference(list2))
print(list1 ^ list2)

list1.add(999)
list1.update([888,777,555])
print(list1)

print(list1.pop())
print(list1.pop())
print(list1.pop())
print(list1.pop())
print(list1.remove(999))
print(  list1.discard(888)  ) # 指定一个值删除
print(list1)