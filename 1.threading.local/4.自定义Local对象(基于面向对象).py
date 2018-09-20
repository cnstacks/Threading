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

    def set(self, k, v):
        ident = get_ident()
        if ident in Local.storage:
            Local.storage[ident][k] = v
        else:
            Local.storage[ident] = {k: v}

    def get(self, k):
        ident = get_ident()
        return Local.storage[ident][k]

obj = Local()
def task(arg):
    obj.set('val', arg)
    v = obj.get('val')
    print(v)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
