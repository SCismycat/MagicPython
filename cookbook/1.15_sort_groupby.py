#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 9:43
# @Author  : Leslee

# 根据某个特定的字段分组迭代访问
## itertools.groupby()
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter # 用于根据选择的字段排序
from itertools import groupby
# 需要先排序，再进行groupby
rows.sort(key=itemgetter('date'))
for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)

## 如果你仅仅只是想根据date 字段将数据分组到一个大的数据结构中去，可以用多值字典把groupby的结果进一步存储
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
