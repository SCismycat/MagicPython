#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 22:25
# @Author  : Leslee


import os
import sys
program = "python"
print("process calling..")
arguments = ["called_Process.py"]

os.execvp(program,(program,) + tuple(arguments) + tuple("abc"))
print("bye~")