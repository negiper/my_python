#coding=utf-8

#筛选法寻找素数
#对n以内的数进行筛选，返回一个长度为n的布尔数组
def sieve(n):
    '''compute primes using sieve eratosthenes'''
    x = [1]*n
    x[1] = 0                #1既不是素数也不是合数
    for i in range(2, n/2):
        j = 2*i
        while j < n:
            x[j] = 0        #将所有i的倍数筛除
            j = j+i
    return x

#求第n个素数，只需要找到筛选好的布尔数组中找第n个标记为1的数
def n_prime(n,x):
    '''Find nth prime'''
    i = 1
    j = 1
    Mi = len(x)
    while j <= n:
        if i >= Mi:
            print '\nOut of range!'
            return 1
        if x[i] == 1:
            j = j+1
        i = i+1
    return i-1

def print_primes(x): 
    N = len(x)
    n = 1
    j = 1
    while n <= N:
        n = prime(j,x)
        if n == 1:
            break
        print n,'  ',
        j = j+1
    return

if __name__ == '__main__':
    N = 100
    pl = sieve(N)
    print pl
    primes_within_x(pl)
    n = 1
    j = 1
    while n <= N:
        n = prime(j,pl)
        if n == 1:
            break
        print u'第%s个prime: %s' % (j,n)
        j = j+1
