#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 22:22
# @Author  : Leslee

import threading
import time

#### demo 1
# def func(i):
#     print("程序被 %i\n 所唤起" % i)
#     return
#
# threads = []
#
# for i in range(5):
#     t = threading.Thread(target=func, name = "thread-"+str(i),args=(i,))
#     threads.append(t)
#     t.start()
#     t.join()
# print(threads)

#### demo 2
"""
理论上说明三个线程是同时执行的。
"""
def first_function():
    print(threading.currentThread().getName() + str(' is Starting '))
    time.sleep(2)
    print (threading.currentThread().getName() + str(' is Exiting '))
    return

def second_function():
    print(threading.currentThread().getName() + str(' is Starting '))
    time.sleep(2)
    print (threading.currentThread().getName() + str(' is Exiting '))
    return

def third_function():
    print(threading.currentThread().getName() + str(' is Starting '))
    time.sleep(2)
    print(threading.currentThread().getName() + str(' is Exiting '))
    return

if __name__ == '__main__':
    t1 = threading.Thread(name='first_function', target=first_function)
    t2 = threading.Thread(name='second_function', target=second_function)
    t3 = threading.Thread(name='third_function', target=third_function)
    t1.start()
    t2.start()
    t3.start()
    # t1.join()
    # t2.join()
    # t3.join()








