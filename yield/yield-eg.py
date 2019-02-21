#!/usr/bin/env python
#-*- encoding:utf-8 -*-

def do_func(i):
    print(i,'done')
    return i**2

def square():
    for i in range(100):
        # yield i**2 # 简单功能可以直接执行，复杂的可以执行函数
        yield do_func(i) # yield必须在函数内使用

''' square()执行结果是一个generator object,
    要查看结果必须一次一次的next(...)来获取下一个值,
    或者可以使用in来依次获取，
    因为in这个关键词自动在后台为我们调用生成器的next(..)函数
    https://segmentfault.com/a/1190000018208997 这篇文章讲的很清晰
'''
result = square()
print('result is a generator object',result)
print('call next get result value')
print(next(result))
print('use in get result value')
for r in result:
    print(r)
