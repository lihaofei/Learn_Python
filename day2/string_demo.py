#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bill Li
name = "my \t  name is {name} and i am {year} old"
print(name.capitalize())
print(name.count('a')) #计算a的个数
print(name.center(50,"-")) # 一共打印50个字符，不够的话则通过-补全
print(name.endswith("ld")) #判断字符以ld结尾
print(name.expandtabs(tabsize=30)) #tab按键转换成30个空格 \t
print(name.find("name")) #找出字符串的索引
print(name[name.find("name"):])
print(name.format(name='alex',year=23))
print(name.format_map(  {'name':'alex','year':12}  ))
print('ab23'.isalnum()) #包括英文字符和1234567890
print('abA'.isalpha())
print('10'.isdecimal())
print('1A'.isdigit())
print('A'.isidentifier()) #判读是不是一个合法的标识符 即就是判断是不是一个合法的变量名
print('33'.isnumeric()) #判读是不是一个数字 ==isdigit()
print(' '.isspace()) #判断是不是 一个空格
print('My Name Is'.istitle()) #判断每个首字母大写
print('My Name Is'.isprintable()) #是否能打印 字符串不考虑 一般在linux 中tty file driver file 是不能打印的
print("My Name is".join("===="))
print('+'.join(['1','2','3'])) ####很重要#####
print(name.ljust(50,"*"))
print(name.rjust(50,'-'))
print("All".lower()) #全部小写
print("AlL".upper()) #全部大写
print('\nAlex   '.lstrip())
print('    alex\n'.rstrip())
print('  alex   \n '.strip())
print('---------')
p = str.maketrans('abcdef','123456') #将字符串转成对应的值 a=1 b=2 c=3
print('alex li'.translate(p)) #1l5x li
print('alex li'.replace('l','L',2))
print('alex li1'.rfind('e')) #从左往右找到最右边值的下标
print('1+2+3+5'.split('+'))
print('1+2\n+3+4'.splitlines()) #遇到换行符分割
print('lex li'.title())
print('lex li'.zfill(50))

your_string = 'hello github'
print(your_string.capitalize())
print(your_string.count('g'))
print(your_string.endswith('hub'))
