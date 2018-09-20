# -*- coding:utf-8 -*-
# Project: Threading 
# Software: PyCharm
# Time    : 2018-09-19 22:50
# File    : 2.threadingLocal的思路.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from threading import Thread
from threading import get_ident


def task(arg):
    print(get_ident())


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
