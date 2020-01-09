#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 9:10
# @Author  : Leslee

# 怎样在一个序列上面保持元素顺序的同时消除重复的值？

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe_for_dict(items, key=None):
    seen_for_dict = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen_for_dict:
            yield item
            seen_for_dict.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

mm = list(dedupe_for_dict(a, key= lambda d:(d['x'],d['y'])))
print(mm)

# mm = list(dedupe_for_dict(a,key=None))
# print(mm)

mm = list(dedupe_for_dict(a,key=lambda x:x['x']))
print(mm)


# 命名切片
## 内置slice()函数，创建了一个切片对象。
items = [1,2,3,4,5]
a = slice(2,4)
a.start
a.step
a.stop

# 序列中出现最多的元素
from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

word_count = Counter(words)
top_three = word_count.most_common(3)
"""
Counter对象可以接受任意的可哈希元素构成的序列
"""
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_count[word] += 1
## 或者
word_count.update(morewords)
