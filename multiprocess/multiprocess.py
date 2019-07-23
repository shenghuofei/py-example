#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import random
import time
from multiprocessing import Pool
from pebble import ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
from concurrent.futures import TimeoutError


############## 使用threading ##################
def do_task(name, res):
    time.sleep(random.randint(1, 2))
    if name == 'c':
        try:
            assert 1 == 2
        except Exception:
            raise RuntimeError('request api for detail fail')
    res.append(name)


# 某个线程抛出异常，主进程仍继续执行
def test_thread():
    name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    res = []
    threads = []
    for p in name_list:
        thread = threading.Thread(target=do_task, args=(p, res))
        thread.start()
        threads.append(thread)
    for th in threads:
        th.join()
    print("treading", res)


test_thread()


############### 使用pebble.ProcessPool(线程池支持超时时间等) ######
#### pip install pebble  https://pypi.org/project/Pebble/ ####
def do_task_pebble(name):
    time.sleep(random.randint(1, 2))
    if name == 'c':
        try:
            assert 1 == 2
        except Exception:
            raise RuntimeError('request api for detail fail')
    return name


# 某个线程抛出异常，主进程程也会抛出异常
def test_pebble_pool():
    name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    util_datas = []
    with ProcessPool(max_workers=4, max_tasks=8) as pool:
        future = pool.map(do_task_pebble, name_list, timeout=600)
        try:
            for n in future.result():
                if n:
                    util_datas.append(n)
        except TimeoutError:
            print("TimeoutError: aborting remaining computations")
            future.cancel()
    print("pebble", util_datas)


# test_pebble_pool()


################ 使用multiprocessing.Pool(进程池) ##########
def do_taks_process(name):
    time.sleep(random.randint(1, 2))
    # if name == 'c':
    #     try:
    #         assert 1 == 2
    #     except Exception:
    #         raise RuntimeError('request plus for detail fail')
    return name


# 某个进程抛出异常，主进程也会抛出异常
def test_pool():
    print 'concurrent:'  # 创建多个进程，并行执行
    pool = Pool(5)  # 创建拥有5个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    rl = pool.map(do_taks_process, name_list)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    print("process", rl)


# test_pool()


############### 使用multiprocessing.dummy.pool(线程池) #######
# https://www.programcreek.com/python/example/100817/multiprocessing.dummy.Pool
def do_taks_dummy(name):
    time.sleep(random.randint(1, 2))
    # if name == 'c':
    #     try:
    #         assert 1 == 2
    #     except Exception:
    #         raise RuntimeError('request api for detail fail')
    return name


# 某个线程抛出异常，主进程程也会抛出异常
def test_dummy():
    name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    pool = ThreadPool(4)
    res = pool.map(do_taks_dummy, name_list)
    pool.close()
    pool.join()
    print("dummy", res)


# test_dummy()
