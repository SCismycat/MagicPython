#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 9:50
# @Author  : Leslee

# 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
## 1. 列表表达式

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
res = [n for n in mylist if n>0]

## 内存敏感用生成器表达式
pos = (n for n in mylist if n>0)

## 使用filter()
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int,values))

## 更多用法
import math
clip_neg = [math.sqrt(n) if n > 0 else 0 for n in mylist]
clip_neg1 = [n if n > 0 else 0 for n in mylist]

## itertools.compress(),用一个iterable对象和boolean序列作为输入参数，返回为True的iterable对象
addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK',
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n>5 for n in counts]

list(compress(addresses,more5))
