#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 9:37
# @Author  : Leslee

# 你想排序类型相同的对象，但是他们不支持原生的比较操作。
"""
内置sorted函数的关键字参数key。传入一个callable对象，可以排序。
"""
class User:
    def __init__(self,user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)
from operator import attrgetter
def sort_not_compare():
    users = [User(23),User(3),User(99)]
    print(users)
    print(sorted(users,key=lambda u:u.user_id))

# 或者
    sorted(users,key=attrgetter('user_id'))







