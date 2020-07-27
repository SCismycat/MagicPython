#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 23:36
# @Author  : Leslee

'''
并行应用需要交换对象的时候，使用队列queue和管道pipe；
'''
# 使用队列共享对象，队列线程安全，进程安全，可序列化对象都可以通过队列进行交换。

import multiprocessing
from multiprocessing import Process
import random
import time

class Producer(Process):
    # 子类重写Process方法，先重写init方法，提供额外参数
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) -> None:
        for i in range(10):
            item = random.randint(0,256)
            self.queue.put(item)
            print("Process Producer : item %d appended to queue %s" % (item, self.name))
            time.sleep(1)
            print("The size of queue is %s" % self.queue.qsize())

class Consumer(Process):

    def __init__(self,queue):
        Process.__init__(self)
        self.queue = queue

    def run(self) -> None:
        while True:
            if self.queue.empty():
                print("the queue is empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print('Process Consumer : item %d popped from by %s \n' % (item, self.name))
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()

