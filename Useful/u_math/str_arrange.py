#!/usr/bin/env python
#coding=utf-8
#求字符串的所有全排列

#==================================
#全排列的递归实现
#==================================
def rec_all_arranges(st,begin,end):
    global arr
    if len(st) <= 0:
        return

    if begin == end-1:
#        print ''.join(st)
        arr.append(''.join(st))
    else:
        for i in range(begin,end):
            st[begin],st[i] = st[i],st[begin]
            rec_all_arranges(st,begin+1,end)
            st[begin],st[i] = st[i],st[begin]

#==================================
#有重复的字符串全排列
#==================================
def is_swap(st,begin,pos):
    p = begin
    while p < pos:
        if st[p] == st[pos]:
            return False
        p += 1
    return True

def rec_all_arranges2(st,begin,end):
    global arr
    if len(st) <= 0:
        return

    if begin == end-1:
        arr.append(''.join(st))
    else:
        for i in range(begin,end):
            if is_swap(st,begin,i):
                st[begin],st[i] = st[i],st[begin]
                rec_all_arranges2(st,begin+1,end)
                st[begin],st[i] = st[i],st[begin]


#====================================
#全排列的非递归实现(Even全排列生成算法)
#Even_Arrange类实现了该算法：
#   1）求出最大活动整数m
#   2）交换m和其箭头所指向的相邻整数
#   3）交换所有满足p>m的整数p的方向
#该类包含4个属性：
#self.arr       ：字符列表
#     L         ：字符个数
#     direction ：每个字符的方向属性列表
#     active    ：每个字符的活动属性列表
#====================================
class Even_Arrange(object):
    def __init__(self,lstring):
        self.arr = lstring
        self.L = len(lstring)
        self.direction = [0]*self.L
        self.active = [0]+[1]*(self.L-1)

    def max_active(self):
        Index = 0
        maxch = min(self.arr)
        for i in range(self.L):
            if self.active[i] and self.arr[i]>maxch:
                maxch = self.arr[i]
                Index = i

        return Index

    def swap(self):
        I = self.max_active()
        maxch = self.arr[I]
        D = self.direction[I]

        #**************************************************
        #注意交换两个字符的时候，不要忘了交换他们的方向属性
        #**************************************************
        if D == 0:
            self.arr[I],self.arr[I-1] = self.arr[I-1],self.arr[I]
            self.direction[I],self.direction[I-1] = self.direction[I-1],self.direction[I]
        else:
            self.arr[I],self.arr[I+1] = self.arr[I+1],self.arr[I]
            self.direction[I],self.direction[I+1] = self.direction[I+1],self.direction[I]
        
        for i in range(self.L):
            if self.arr[i] > maxch:
                if self.direction[i] == 0:
                    self.direction[i] = 1
                else:
                    self.direction[i] = 0
    
    def set_active(self):
        for i in range(self.L):
            D = self.direction[i]
            if D == 0:
                if i == 0:
                    self.active[i] = 0
                elif self.arr[i-1] < self.arr[i]:
                    self.active[i] = 1
                else:
                    self.active[i] = 0
            else:
                if i == self.L-1:
                    self.active[i] = 0
                elif self.arr[i+1] < self.arr[i]:
                    self.active[i] = 1
                else:
                    self.active[i] = 0

    def all_permutaion(self):
        print ''.join(self.arr)
        while any(self.active):
            self.swap()
            print ''.join(self.arr)
            self.set_active()
#            raw_input()

st = raw_input('Input a string: ')
#arr = []
#rec_all_arranges(list(st),0,len(st))
#rec_all_arranges2(list(st),0,len(st))
ob = Even_Arrange(list(st))
ob.all_permutaion()
