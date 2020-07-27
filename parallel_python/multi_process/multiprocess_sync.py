#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 0:00
# @Author  : Leslee

'''
进程同步原语：
1. Lock：一个锁有两种状态 locked和unlocked。一个Lock有acquire()和release()控制共享数据的读写权限；
2. Event：实现了进程间的简单通讯，一个进程发事件的信号，另一个进程等待事件的信号。
3. Condition:用来同步部分工作流程，并行进程中，有两个基本方法：wait()用于等待进程，notify_all()用于通知所有
等待此条件的进程。
4. Semaphore:用于共享资源，如支持固定数量的共享连接。
5. Rlock：递归锁对象
6. Barrier: 将程序分成几个阶段，适用于有些进程必须在某些特定进程之后执行。处于障碍（Barrier）之后的代码不能同处于障碍之前的代码并行。
'''
import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))

if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer,serializer)).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer,serializer)).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()










