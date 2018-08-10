#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bill Li
#字符无序性 无下标 通过key 进行查询 key_value
info = {
    '1101':'wu teng',
    '1102':'xiao ze',
    '1103':'cang jing kong',
}
b= {'1101':'longze ',2:3,5:'li'}
info.update(b) #合并字典
info["1105"]="ni hao"
print(info)
# del
del info['1105']
# info.pop("1105")
# print(info.items())
# print(info['1101'])
# print(info.get('1103'))

# for k , v in info.items():
#     print(k," ",v)

for i in info:
    print(info[i])

# 增加
info['1121']="苍井空"
# 修改
info['1121']="泷泽萝拉"
# 删除
info.pop('1121')
print(info)
del info['1101']
print(info)
info.popitem()#随机删除
print(info)

# 查找
print(info['1102']) #此方法你必须确认存在字典
print(info.get('1101')) #安全获取
print('1102'in info)

#多级字典嵌套
av_catalog={
    "欧美":
        {"www.oumei.com":['you ','love','it?'],
         "www.sohu.com":['ss','hu'],
         "www.google.com":['1','2']

    },
    "日韩":{
        'tokey_hot':[1,1,2]


    },
    "大陆":
        {
            'caoliu':[3,3,3,3]

        }

}


# av_catalog.keys()
# av_catalog.values()
av_catalog["大陆"]['caoliu'][2]='your love'
av_catalog.setdefault('大陆',{'vv':[2]})
print(av_catalog)
