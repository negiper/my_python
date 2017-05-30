#!/usr/bin/env python
#coding=utf-8
#2016年 08月 17日 星期三 08:42:47 CST
#==================================
# 约瑟夫环算法 之 猴子选王 问题
#===================================
def king(m, n):
    dd = {}
    i = 1
    #生成字典
    while i <= m:
        dd[i] = i
        i += 1

    j = 1
    #重复筛选
    while len(dd) > 1:
        for k,v in dd.items():
            if j == n:
                del dd[k]
                j = 1
            else:
                j += 1
    return dd.items()[0][0]

#递推公式
#=================================
# f(m): 表示m个人环，胜出者的编号
# f(1)=0, f(m)=(f(m-1)+n)%m,(m>1)
#================================= 
def king2(m,n):
    K = 0
    for i in range(2,m+1):
        K = (K+n)%i
    return K+1
    
if __name__ == '__main__':
    print u'约瑟夫环(100, 5)，胜出者：',king2(100,5)
    print u'约瑟夫环(100, 4)，胜出者：',king2(100,4)
    print u'约瑟夫环(100, 3)，胜出者：',king2(100,3)
    print u'约瑟夫环(100, 2)，胜出者：',king2(100,2)
    '''隔位消灭的约瑟夫问题可以利用如下公式求解：
        若 m = 2^i + k
        则最终胜出者 K = 2*k + 1
    '''