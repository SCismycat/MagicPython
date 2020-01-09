#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 8:52
# @Author  : Leslee

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['a'].append(3)


# 字典排序
## 保顺序的dict
from collections import OrderedDict
d = OrderedDict()#需要精确控制字段顺序的时候，用orderDict，耗内存
d['foo'] = 1
d['bar'] = 2

## 字典运算操作

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
min_price = min(zip(prices.values(),prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))
prices_sorted = sorted(zip(prices.values(),prices.keys()))

## 在min和max函数中提供key函数参数来获取最大或最小对应键的信息。
min(prices,key=lambda k:prices[k]) # 返回最小的value对应的key
max(prices,lambda x:prices[x])

# 查找两个字典的相同点
a = {
'x' : 1,
'y' : 2,
'z' : 3
}
b = {
'w' : 10,
'x' : 11,
'y' : 2
}

a.keys() & b.keys()
a.items() & b.items() # 键值都相同

## 通过某个关键字排序一个字典列表
### 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表
rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
sort_by_fnames = sorted(rows,key=itemgetter('fname'))
sort_by_uid = sorted(rows,key=itemgetter('uid'))

sort_by_lfname = sorted(rows,key=itemgetter('lname','fname'))
