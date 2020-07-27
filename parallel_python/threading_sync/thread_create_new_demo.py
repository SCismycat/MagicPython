#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 22:35
# @Author  : Leslee

"""
1. 定义一个Thread的子类；
2. 重写 __init__(self,[,args])方法，使其可以增加额外参数
3. 重写run(self,[,args])方法，实现线程启动后要做的方法；
"""
import threading
import time
import _thread

exitFlag = 0
class myThread(threading.Thread):

    def __init__(self,ThreadID, name,counter):
        threading.Thread.__init__(self) # 继承Thread的基本方法
        self.threadID = ThreadID
        self.name = name
        self.counter = counter

    def run(self) -> None:
        print("Starting:" + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            _thread.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建一个新线程
t1 = myThread(1,"No.1", 1)
t2 = myThread(2, "No.2", 2)

# 开始新线程
t1.start()
t2.start()

t1.join()
t2.join()
print("Exiting Main Thread")