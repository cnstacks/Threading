#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Threading 
# Software: PyCharm
# Time    : 2018-09-20 09:20
# File    : 4.自定义Local对象(基于面向对象).py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from threading import get_ident
from threading import Thread


class Local(object):
    storage = {}

    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in Local.storage:
            Local.storage[ident][k] = v
        else:
            Local.storage[ident] = {k: v}

    def __getattr__(self, item):
        ident = get_ident()
        return Local.storage[ident][item]


obj = Local()


def task(arg):
    obj.val = arg
    print(obj.val)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
