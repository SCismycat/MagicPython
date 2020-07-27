#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 22:46
# @Author  : Leslee

from threading import Thread
from time import sleep
# 继承Thread，来让这个类可以通过多线程工作
class Cookbook(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.message = "Hi, Python Thread!\n"

    def print_message(self):
        print(self.message)

    def run(self) -> None:
        print("Thread Starting\n")
        x = 0
        while (x<10):
            self.print_message()
            sleep(2)
            x += 1
        print("Thread ending\n")


# start the main process
print("开始")

# create an instance of the HelloWorld class
hello_Python = Cookbook()

# print the message...starting the thread
hello_Python.start()

# end the main process
print("结束了")

