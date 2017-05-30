#coding=utf-8
#python自带计时器的使用方法

import timeit

def func1():
    labels = ''
    for i in range(10000):
        labels += str(i)

def func2():
    labels = []
    for i in range(10000):
        labels.append(str(i))
    res = ''.join(labels)

def func3():
    labels = [str(i) for i in range(10000)]
    res = ''.join(labels)

print timeit.timeit('func1()','from __main__ import func1',number=100)
print timeit.timeit('func2()','from __main__ import func2',number=100)
print timeit.timeit('func3()','from __main__ import func3',number=100)
