#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: diange.du
@file: log_util.py
@time: 2020/9/2 18:19
@desc:
'''

import os
import logging
from logging import handlers
import datetime


class LogUtil:
    logger = None

    def __init__(self, name, filename="tb_crawler" + datetime.datetime.now().strftime('%Y-%m-%d') + ".log"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        format = '[%(asctime)s] [%(levelname)s] [%(filename)s] [line:%(lineno)d] %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        log_path = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_filepath = os.path.join(log_path, filename)
        th = handlers.TimedRotatingFileHandler(filename=log_filepath, when='midnight', encoding='utf-8')
        # th.suffix='%Y-%m-%d_%H-%M-%S.log'
        th.setFormatter(logging.Formatter(format, datefmt))
        self.logger.addHandler(th)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(logging.Formatter(format, datefmt))
        self.logger.addHandler(console)


def getLogger(name):
    log = LogUtil(name)
    return log.logger


log = getLogger(__name__)

# if __name__ == '__main__':
#     log.info('hello world logging...')
