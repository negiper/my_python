#*********************************
#计算阶乘结果末尾0的个数的简单方法
#*********************************

def cal_zeros(N,t):
    factors = []
    count = []

    for n in range(2,N+1):
        if n % t == 0:
            factors.append(n)
            temp = n
            n_count = 0
            while temp % t == 0:
                n_count += 1
                temp = temp/t
            count.append(n_count)
    print factors
    print count
    print sum(count)

if __name__ == '__main__':
    num = input('Please input the number: ')
    cal_zeros(num,5)
