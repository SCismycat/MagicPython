#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 23:46
# @Author  : Leslee

'''
事件是线程间用于通讯的对象，有些线程等待信号，有些发出信号，基本上事件对象维护一个内部变量，
可通过set()设置为True，也可以通过clear()设置为false，wait会阻塞线程，直到内部为True。
'''

import time
from threading import Thread, Event
import random
items = []
event = Event()

class consumer(Thread):

    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self) -> None:
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print('Consumer notify : %d popped from list by %s' % (item, self.name))

class producer(Thread):

    def __init__(self,items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self) -> None:
        global item
        for i in range(100):
            time.sleep(2)
            item = random.randint(0,256)
            self.items.append(item)
            print('Producer notify : item N° %d appended to list by %s' % (item, self.name))
            print('Producer notify : event set by %s' % self.name)
            self.event.set()
            print('Produce notify : event cleared by %s '% self.name)
            self.event.clear()

if __name__ == '__main__':
    t1 = producer(items, event)
    t2 = consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()