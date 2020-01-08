#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 8:38
# @Author  : Leslee
from collections import deque
# 你在学习一门课程，在学期
# 末的时候，你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数

def drop_first_last(grades):
    first,*middle,last = grades
    return (middle) # 取平均即可

# 多行做文本匹配，返回匹配所在行的最后N行
def searchN(lines,pattern,history=6):
    # deque构造函数新建一个固定大小的队列，新元素假如，旧元素移除。
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

"""
查找最大或最小的N个元素：heapq
适合N不太大又不太小的场景
"""
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheaper = heapq.nsmallest(3,portfolio,key= lambda x:x['price'])
# 转换成堆
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)
