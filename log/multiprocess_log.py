#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging
from logging import INFO, DEBUG
from cloghandler import ConcurrentRotatingFileHandler
import socket

class CustomFormatter(logging.Formatter):
    """ 自定义日志格式
    """
    def __init__(self, fmt):
        logging.Formatter.__init__(self, fmt=fmt)

    def format(self, record):
        setattr(record, 'hostname', socket.gethostname())
        return logging.Formatter.format(self, record)

def init_logger(background=False):
    """ 初始化日志 """
    log_format = [
        '%(asctime)s',
        '%(levelname)s',
        'pid:%(process)d',
        '%(filename)s:%(lineno)d',
        '%(message)s'
    ]

    formatter = logging.Formatter('\t'.join(log_format))

    if background:
        # 多进程下日志切割出现问题, 替换成多进程日志模块,写日志会加锁,pip install ConcurrentLogHandler
        handler = ConcurrentRotatingFileHandler(
            filename='./mytestlog.log',
            maxBytes=10000000,
            backupCount=30
        )
    else:
        handler = logging.StreamHandler()
    # handler.setFormatter(CustomFormatter(fmt='\t'.join(log_format)))
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

class Log():
    def __init__(self, background=False):
        init_logger(background)

    def log(self, msg, level=INFO):
        hostname = socket.gethostname()
        msg = '\t'.join([hostname, msg])
        logging.log(level, msg)

log = Log(False)
log.log('test')
