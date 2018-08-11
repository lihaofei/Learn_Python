#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bill Li

#windows 默认编码是GBK
import os ,sys
import time
# f=open("yesterday",'r',encoding='utf-8') # f 是文件句柄 就是文件指定的内存对象
# data=f.read()
# f.close()
# # print(data)
# f=open('yesterday2','w',encoding='utf-8')
# f.write("我爱你祖国")
#
# f.close()
#
# f=open('yesterday2','a',encoding='utf-8') #追加模式
# f.write("我爱你祖国\n")
# f.write("我爱你祖0-0--0-0-0-\n")
# f.write("我爱你祖0-0-22222-0-\n")
# f.close()

# f=open('yesterday','r',encoding='utf-8') #追加模式
# print(f.readline())
# for lines in range(5):
#     print(f.readline())


# #此方法不适用大文件 readlines()
# for lines in f.readlines():
#     print(lines.strip())
# #较为高效的方式为
# count=0
# for line in f:
#     if count==9:
#         print('-----------')
#         count+=1
#         continue
#     print(line)
#     count+=1

# #low loop
# for index,line in enumerate(f.readlines()):
#     if index==9:
#         print("---------分割线----------")
#         continue
#     print(line.strip())
# f.close()

# seek() 设定光标位置
# encoding
# flush
# tell() 找光标位置
#
# for  i in  range(50):
#     sys.stdout.flush()
#     print("#",end='')
#     time.sleep(0.1)
# r+ 可读追加写

# f = open("yesterday2",'r+',encoding="utf-8")
# # print(f.encoding)
# f.write("----diao----")
# print(f.readline())
# print(f.tell())

#
# f.close()

# #
# # w+ 写读 先创建然后写 读
# #
#
# f2=open("yesterday2",'w+',encoding='utf-8')
# f2.write("-----diao------\n")
# f2.write("-----diao------\n")
# f2.write("-----diao------\n")
# f2.write("-----diao------\n")
# print(f2.tell())
# f2.seek(10)
# print(f2.tell())
# print(f2.readline())
# f2.write("i love python \n")
# f2.close()
# f2.flush()

# f2.close()
# #
# # a+ 追加写 不能读
# #
# f2=open("yesterday3",'a+',encoding='utf-8')
# f2.write("hello")
# print(f2.readline())
# f2.close()
#
# #
# # rb 二进制读模式 不能传encoding相关内容
# # 在网络传输时用网络传输的方式需要进行二进制模式
# #
# f=open("yesterday4",'rb')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()
# print(f.tell())
# f.close()
# # wb 二进制写模式
# # 需要进行编码encode()
# f=open("yesterday4",'wb')
# f.write('hello world'.encode())
# f.close()


# 文本修改

# f = open("yesterday2",'r',encoding='utf-8')
# f_new=open("yesterday2.bak",'w',encoding='utf-8')
# for line in f:
#     if  'diao' in line:
#         line = line.replace('diao','python')
#     f_new.write(line)
# f.close()
# f_new.close()

import sys
with open('yesterday2','r',encoding='utf-8') as f:
    for line in f:
        print(line)
