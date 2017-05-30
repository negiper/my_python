#coding=utf-8
'''
This module gives some effective methods for list.
'''
#===========================================================
# 为了有效提高list的查找效率，我们可以减少对list的扫描次数
#===========================================================
def find_two_smallest(L):
    '''Return a tuple of the indeces of the two smallest values in list L.'''
    if L[0] < L[1]:
       min1, min2 = 0, 1
    else:
       min1, min2 = 1, 0

    for i in range(2,len(L)):
        if L[i] < L[min1]:
            min2 = min1
            min1 = i
        elif L[i] < L[min2]:
            min2 = i

    return (min1,min2)

