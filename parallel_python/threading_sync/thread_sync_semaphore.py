#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 22:06
# @Author  : Leslee

# 使用信号量同步线程
import threading
import time
import random

# 信号量维护一个初始的值，默认是1，当小于0的时候，会抛出异常
# 信号量初始化为0，这样的话该信号量可以同步多个线程，也就是多个线程是并行运行的。
# 因为线程并行，所以consumer和producer都运行，consumer挂起，producer会产生随机数字，然后release()会另信号量增加到1.此时
# 消费者通过 acquire() 拿到这个信号量，然后执行。然后再次挂起。再次等待信号量。
#### 应用
# 互斥量，初始化信号量为1，能实现数据、资源的互斥访问；

####问题
# 死锁；t1和t2交叉等待两个信号量，会死锁。非原子性操作会导致线程都在等待。

semaphore = threading.Semaphore(0)

def consumer():
    print("consumer is waiting..")
    # 申请一个信号量
    semaphore.acquire()
    # 消费者拿到一个共享资源
    print("Consumer notify : consumed item number %s " % item)


def producer():
    global item
    time.sleep(10)
    # 创建一个随机数字item
    item = random.randint(0,1000)
    print("producer notify : produced item number %s" % item)
    # 释放一个信号量，将内部的信号量从0增加到1，当调用时信号量是0且另一个线程在等待它再次大于0的时候，唤醒该线程。
    semaphore.release()

if __name__ == '__main__':
    for i in range(0,5):
        #
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print("program terminated!")


