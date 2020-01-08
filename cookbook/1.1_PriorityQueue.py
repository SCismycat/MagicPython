#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 8:57
# @Author  : Leslee

import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),3)
q.push(Item('spam'),5)
q.push(Item('gss'),1)
print()
print(q.pop())

# heapq.heappush和heappop分别在队列上插入和删除第一个元素。
"""
heappop()函数总是返回最小的元素，这是保证队列pop返回正确元素的关键；
队列包含一个(-priority,self._index,item)元祖，priority保证优先级；index保证按照插入顺序排序。
"""

# Todo 阅读官方heapq模块的官方文档