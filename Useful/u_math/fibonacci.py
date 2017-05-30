#coding=utf-8
#计算斐波那契数列的三种方法

num = 10
itemList = [0]*num
#*****递归方法******
def cal_fibonacci(n):
#递归计算斐波那契数列前n项
#itemList用于将重复子问题的解记录下来，以免重复计算
    global itemList
    if n == 1 or n == 2:
        an = f1 = f2 = 1
        itemList[n-1] = an
        print an
        return an
    else:
        if itemList[n-2]:
            f1 = itemList[n-2]
        else:
            f1 = cal_fibonacci(n-1)
        
        if itemList[n-3]:
            f2 = itemList[n-3]
        else:
            f2 = cal_fibonacci(n-2)
        
        an = f1 + f2
        f1 = f2
        f2 = an
        itemList[n-1] = an
        print an
        return an

#print 'the '+str(num)+'th of Fibonacci sequence is: ',cal_fibonacci(num)
#cal_fibonacci(num)

#*****循环计算斐波那契数列前n项******
def loop_fibonacci(n):
    global itemList
    itemList[0] = itemList[1] = 1
    print itemList[0]
    print itemList[1]
    for ind in range(2,n):
        itemList[ind] = itemList[ind-1] + itemList[ind-2]
        print itemList[ind]

#loop_fibonacci(num)

#******利用公式计算斐波那契前n项*****
from math import sqrt

def formula_fibonacci(n):
    for i in range(n):
        an = int((sqrt(5)/5)*(((1+sqrt(5))/2)**(i+1)-((1-sqrt(5))/2)**(i+1)))
        print an

formula_fibonacci(num)
