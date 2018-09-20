#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Threading 
# Software: PyCharm
# Time    : 2018-09-20 09:20
# File    : 5.自定义Local对象(基于面向对象优化版 ).py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from threading import get_ident
from threading import Thread


class Local(object):

    def __setattr__(self, k, v):
        # self.storage = {}
        object.__setattr__(self, 'storage', {})
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][k] = v
        else:
            self.storage[ident] = {k: v}


def __getattr__(self, item):
    ident = get_ident()
    return self.storage[ident][item]


obj = Local()
obj1 = Local()


def task(arg):
    obj.val = arg
    obj1.val = arg
    print(obj.val)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
