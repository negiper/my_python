#coding=utf-8
#====================
#heapq 简单运用
#====================

import heapq

#heapq 实现堆排序
def heapsort(lst):
    heapq.heapify(lst)
    tmp = []
    for i in range(len(lst)):
        tmp.append(heapq.heappop(lst))
    return tmp

#求第n大和第n小的元素
def nth_large(n,lst):
    return heapq.nlargest(n,lst)[-1]
    
def nth_small(n,lst):
    return heapq.nsmallest(n,lst)[-1]
    

#利用小根堆求(TopK)和大根堆求(BtmK)

