#coding=utf-8
#将time封装为一个计时器，用于with语句
#即定义一个计时上下文管理器(必须定义__enter__和__exit__方法)

import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        print 'Starting...'
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
        print 'End.'
        if self.verbose:
            print 'elapsed time: %f ms' % self.msecs

if __name__ == '__main__':
    sum = 0
    with Timer(True) as t:
        for i in range(10000000):
            sum += i
