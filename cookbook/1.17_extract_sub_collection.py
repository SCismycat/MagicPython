#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 10:00
# @Author  : Leslee
# 构建一个字典的子集
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}#

p1 = {key:value for key,value in prices.items() if value>200}

