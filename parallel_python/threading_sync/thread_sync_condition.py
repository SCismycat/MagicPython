#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 22:48
# @Author  : Leslee

#  使用条件进行线程同步

##
from threading import Thread, Condition
import time

items = []
condition = Condition()

class consumer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items
        condition.acquire()  # 消费者会拿到锁，修改共享资源item

        if len(items) == 0:
            # 当缓冲区是空的时候，condition就等待。
            condition.wait() # wait中有一个释放锁重新获得锁的过程
            print("Consumer notify : no item to consume")

        items.pop()# 否则的话，就通过pop消费一个item
        print("Consumer notify : consumed 1 item")
        print("Consumer notify : items to consume are " + str(len(items)))
        # 消费以后，condition会通过以下两行代码，通过notify，消费者的状态通知给生产者，并且释放共享资源。
        condition.notify() ## notify方法不会直接立刻释放锁，而是等到执行notify()方法的线程把程序执行完，当前线程会释放锁。
        condition.release()
    def run(self) -> None:
        for i in range(0,20):
            time.sleep(2)
            self.consume()

class producer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items
        # 然后生产者申请拿到共享资源，确认缓冲队列是否已经满了，如果满了，生产者也等待。
        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print("Producer notify : items producted are " + str(len(items)))
            print("Producer notify : stop the production!!")
        # 如果没满，就生产一个item。
        items.append(1)
        print("Producer notify : total items producted " + str(len(items)))
        # 然后队列没满，生产一个item，通知个消费者，并且释放资源。消费者拿到就消费一波。
        condition.notify()
        condition.release()

    def run(self) -> None:
        for i in range(0, 20):
            time.sleep(1)
            self.produce()

if __name__ == '__main__':
    producer = producer()
    consumer = consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()


