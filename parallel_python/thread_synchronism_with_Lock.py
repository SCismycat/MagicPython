#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 22:55
# @Author  : Leslee

import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT = 100000
shared_resource_lock = threading.Lock() # 共享资源的锁

def incre_with_lock():
    global shared_resource_with_lock # 声明为全局变量
    for i in range(COUNT):
        shared_resource_lock.acquire() # 获取锁
        shared_resource_with_lock += 1
        shared_resource_lock.release()

def decre_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()

def increment_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock += 1

def decrement_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock -= 1

if __name__ == "__main__":
    t1 = threading.Thread(target=incre_with_lock)
    t2 = threading.Thread(target=decre_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print ("the value of shared variable with lock management is %s" % shared_resource_with_lock)
    print ("the value of shared variable with race condition is %s" % shared_resource_with_no_lock)