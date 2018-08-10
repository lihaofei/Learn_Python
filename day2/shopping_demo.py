#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bill Li
goods_list=[('IPhone',5800),
            ('Mac Pro',12000),
            ('Coffee',33),
            ('Book',20),
            ('Bike',800)]
# print('\nNow have some goods',
#       '\n1 IPhone 5800',
#       '\n2 Mac Pro 12000 ',
#       '\n3 Coffee 33 ',
#       '\n4 Book 20',
#       '\n5 Bike 800')
for index,item in enumerate(goods_list):
    print(index+1,item)
get_goods=[]
own_money=0
while True:
    sarary=int(input('请输入您的钱数'))
    while True:
        goods_num = input("请输入您要购买的商品编号")
        if goods_num != 'q':
            last_money=sarary-goods_list[int(goods_num)-1][1]
            if last_money<0:
                print('您的余额不足')
                break
            else:
                print('已将',goods_list[int(goods_num)-1][0],'加入到您的购物车中')
                sarary=last_money
                get_goods.append(goods_list[int(goods_num)-1][0])
                own_money=sarary



        else:
            print('你购买的东西有')
            for i in get_goods:
                print('\n',i)
            print('您的余额为',sarary)
            exit()