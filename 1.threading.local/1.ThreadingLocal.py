# -*- coding:utf-8 -*-
# Project: Threading 
# Software: PyCharm
# Time    : 2018-09-19 22:40
# File    : 1.ThreadingLocal.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


""
"""
threading.local的作用：为每个线程开辟一块空间来进行数据存储；
"""
from threading import local
from threading import Thread
import time
from threading import get_ident

# 特殊的对象;
xiaozhao = local()


# xiaozhao = -1


def task(arg):
    # global xiaozhao

    xiaozhao.value = arg
    time.sleep(2)
    print(xiaozhao.value)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
