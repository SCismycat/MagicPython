#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 9:28
# @Author  : Leslee
import heapq
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h,value)
    return [heapq.heappop(h) for i in range(len(h))]


