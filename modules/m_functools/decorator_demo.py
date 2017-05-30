#coding=utf-8
#==========================
#functools.wraps 创建装饰器
#==========================

import os
import sys
import functools
from os import getcwd

#======================
#两个简单装饰的例子
#======================
def add_hello(func):
    '''
    为用户接口添加当前工作目录的装饰器
    '''
    import getpass
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print 'Hello,',getpass.getuser(),'Your current position is:'
        return func(*args, **kwargs)
    return wrapper

getcwd = add_hello(getcwd)

#print getcwd()
#print '\n','-'*20,'\n'

def add_hello2(func):
    '''
    为用户打印功能介绍
    '''
    import getpass
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print 'Hello,',getpass.getuser(),'This functon:',getattr(func,'__doc__')
        print 'The result is:'
        return func(*args, **kwargs)
    return wrapper

@add_hello2
def JJtable():
    '''打印乘法口诀表'''
    for i in range(1,10):
        for j in range(1,i+1):
            print '%d*%d = %-4d' % (j,i,i*j),
        print

#JJtable()

#=================================
#替换装饰：将原来的函数替换成新的
#即原函数执行的是新函数的功能
#=================================
import warnings
def deprecated_method(new_name):
    def outer(fun):
        msg = '%s() is deprecated(已弃用); use %s() instead' %(fun.__name__, new_name)
        if fun.__doc__ is None:
            fun.__doc__ = msg
            
        @functools.wraps(fun)
        def inner(*args, **kwargs):
            warnings.warn(msg, category=DeprecationWarning,stacklevel=2)
            new_obj = getattr(sys.modules[__name__],new_name)
            return new_obj(*args, **kwargs)
        return inner
    return outer

def hello_new(name):
    print 'Hello,',name,'welcome to new world!'

#hello_old = deprecated_method('hello_new')(hello_old)
@deprecated_method('hello_new')
def hello_old(name):
    print 'Hello,',name


#========================================================
#缓存装饰：为函数提供备忘录功能
# 即将确定参数的返回值缓存，下次调用时直接返回该缓存值
# 适用于计算量较大，参数离散的情形
#========================================================

def memoize(fun):
    cache = {}
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        key = (args, frozenset( sorted( kwargs.items() ) ))
        print 'Current cache:'
        print cache
        if key in cache:
            print 'Got it!'
            return cache[key]
        else:
            ret = cache[key] = fun(*args, **kwargs)
            return ret
    return wrapper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

