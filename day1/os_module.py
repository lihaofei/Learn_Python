#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bill Li
import os
# cmd_res=os.system("dir") #打印当前路径
# os.system 只执行命令 不能保存路径结果
# 则使用 os.popen()
# cmd_res=os.popen("dir")
# print(cmd_res)

cmd_res=os.popen("dir").read()
print(cmd_res)

os.mkdir("new_dir") #创建文件