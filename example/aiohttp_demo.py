#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: diange.du
@file: aiohttp_demo.py
@time: 2020/9/9 17:50
@desc: aiohttp 示例
'''

import requests
from datetime import datetime

# requests 方式
def fetch(url):
    resp = requests.get(url)
    print(resp.text)


def run():
    start = datetime.now()
    for i in range(10):
        fetch('http://httpbin.org/get')
    print('requests use time:', str(datetime.now() - start))

# requests use time: 0:00:04.241664


# aiohttp 方式
import asyncio
from aiohttp import ClientSession


async def async_fetch(client):
    async with client.get('http://httpbin.org/get') as resp:
        assert resp.status == 200
        return await resp.text()


async def main():
    async with ClientSession() as client:
        tasks = []
        for i in range(10):
            tasks.append(asyncio.ensure_future(async_fetch(client)))
        await asyncio.wait(tasks)


def run2():
    loop = asyncio.get_event_loop()
    start = datetime.now()
    loop.run_until_complete(main())

    print('aiohttp use time:', str(datetime.now() - start))
    loop.close()

# aiohttp use time: 0:00:00.472710


if __name__ == '__main__':
    run2()
