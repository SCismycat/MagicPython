#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 0:11
# @Author  : Leslee

"""
自定义进程子类：
1. 定义Process的子类；
2. 覆盖 __init__(self,[args])添加额外参数
3. 覆盖 run(self,[args])方法实现Process启动的时候执行的任务
"""

import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self) -> None:
        print('called run method in process: %s' % self.name)
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()

