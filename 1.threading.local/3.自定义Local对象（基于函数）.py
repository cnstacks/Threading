#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Threading 
# Software: PyCharm
# Time    : 2018-09-20 09:11
# File    : 3.自定义Local对象（基于函数）.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from threading import get_ident, Thread
import time

storage = {}


def set(k, v):
    ident = get_ident()
    if ident in storage:
        storage[ident][k] = v
    storage[ident] = {k: v}


def get(k):
    ident = get_ident()
    return storage[ident][k]


def task(arg):
    set('val', arg)
    print(storage)
    time.sleep(2)
    v = get('val')
    print(v)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
