#coding=utf-8
#求两个数的最大公约数和最小公倍数
#2016年 03月 10日 星期四 00:08:00 CST

def cal_GCD(a,b):
    if a < b:
        a,b = b,a

    r = a%b
    while r:
        a = b
        b = r
        r = a%b

    return b

def cal_LCM(a,b):
    gcd = cal_GCD(a,b)

    fa = a/gcd
    fb = b/gcd

    return gcd*fa*fb

def get_allLCM(a,b,bound):
    lcm = cal_LCM(a,b)
    k = 2
    lcm_list =[]
    item = lcm
    while  item < bound:
        lcm_list.append(item)
        item = lcm*k
        k += 1

    return lcm_list

inta,intb = raw_input('Input two number: ').split(',')
inta = int(inta)
intb = int(intb)
bound = int(raw_input('Input the bound: '))
print 'GCD of',inta,'and',intb,'is: ',cal_GCD(inta,intb)
print 'LCM of',inta,'and',intb,'is: ',cal_LCM(inta,intb)
print 'All common multiples within',bound,'are: ',get_allLCM(inta,intb,bound)

