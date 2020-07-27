#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 23:50
# @Author  : Leslee

'''
Communication Channel
1. 返回一对被管道连接的连接对象
2. 对象拥有send/receive方法在进程间通信
'''

import multiprocessing

def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        output_pipe.send(item)
    output_pipe.close()

def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2

    try:
        while True:
            item = input_pipe.recv()
            output_pipe.send(item*item)
    except EOFError:
        output_pipe.close()

if __name__ == '__main__':
    # new 一个多进程的pipeline
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=create_items,args=(pipe_1,))
    process_pipe_1.start()
    # 第二个进程管道接收数字并且计算
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()
    pipe_1[0].close()
    pipe_2[0].close()
    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError:
        print("End")