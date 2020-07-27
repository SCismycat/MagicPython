#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 0:34
# @Author  : Leslee

import multiprocessing

'''
Pool类的方法：
1. apply():直到得到结果之前一直阻塞；
2. apply_async()：返回一个result对象，异步操作，所有子类执行前不会锁住主进程。
3. map(): 内置map()函数的并行版本，此方法将可迭代的数据每个元素作为进程池一个任务来执行
4. map_async(): 这是 map() 方法的一个变体，返回一个result对象。如果指定了回调函数，回调函数应该是callable的，并且只接受一个参数。当result准备好时会自动调用回调函数（除非调用失败）。回调函数应该立即完成，否则，持有result的进程将被阻塞。
'''
def function_square(data):
    result = data *data
    return result

if __name__ == '__main__':
    inputs = list(range(100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    print ('Pool    :', pool_outputs)



