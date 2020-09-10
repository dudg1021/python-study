#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: diange.du
@file: async_demo.py
@time: 2020/9/9 17:06
@desc: 协程使用示例
'''

import time
import asyncio

# 同步方式调用
def hello():
    time.sleep(1)


def run():
    for i in range(5):
        hello()
        print('hello() use time:' + str(time.time()))


# 异步方式调用
loop = asyncio.get_event_loop()


async def async_hello():
    asyncio.sleep(1)
    print('hello() use time:' + str(time.time()))
    return str(time.time())


# 回调函数
def callback(future):
    print('这里是回调函数，获取返回结果是：'+future.result())


def run2():
    tasks = []
    for i in range(5):
        task = asyncio.ensure_future(async_hello())
        task.add_done_callback(callback)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == "__main__":
    run2()



