#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 0:22
# @Author  : Leslee

'''
Python的多进程模块提供所在用户间管理共享信息的管理者(Manager).
Manager控制着持有Python对象的服务进程，允许其他进程操作共享对象。
1. 控制着管理共享对象的服务进程；
2. 确保当前某一进程修改了共享对象，所有的进程能拿到额外共享对象的更新。
'''

import multiprocessing

def worker(dictionary, key, item):
    dictionary[key] = item
    print("key = %d value = %d" % (key, item))

if __name__ == '__main__':
    mgr = multiprocessing.Manager()

    dictionary =mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(dictionary, i, i*2)) for i in range(10)]

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print("Result:",dictionary)
