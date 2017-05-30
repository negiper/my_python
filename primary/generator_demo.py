#coding=utf-8
#====================
#生成器&生成器表达式
#====================
'''
生成器：
    定义：可以被挂起并在返回中间值后，仍能多次继续执行的协同程序被称为生成器。
    特点：1)不是一次性将对象全部放入内存，因此节省内存空间。
          2)惰性求值(延迟计算)。
          3)迭代结束，触发StopIteration。
    生成器适合迭代大型数据集。
生成器表达式：
    语法：( expr for iter_var in iterrable if cond_expr )
'''
#简单例子：斐波那契数列生成器
def fab(top):
    n,a,b = 0,0,1
    while n < top:
        yield b
        a,b = b,a+b
        n += 1

#读取大文件
def read_file(path):
    BLOCK_SIZE = 1024
    with open(path,'r') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield
            else:
                return

#可传参数的生成器
def counter(start=0):
    count = start
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1
           
if __name__ == '__main__':
    f = fab(5)
    for i in f:
        print i, '  ',
      
    count = counter(1)
    print count.next()
    print count.next()
    print count.next(5)
    print count.next()
    count.close()
    #count.next() 引发StopIteration

#=========================
#生成器的应用及优势对比
# 实例：查找文件中最长的行
#=========================

#得到(行号，行长)的生成器
def line_tuple(f):
    n = 0
    for line in f:
        n = n+1
        yield (n,len(line.strip()))
        

def find_longest_line(filename):
    f = open(filename,'r')
    longest = 0
    maxi = 0
    i = 0
    while True:
        line = f.readline()
        if not line:
            break
        i += 1
        linelen = len(line.strip())
        if linelen > longest:
            longest = linelen
            maxi = i
    f.close()
    return (maxi,longest)

#改进1：读取文件内容后尽早释放文件句柄    
def find_longest_line1(filename):
    f = open(filename, 'r')
    longest = 0
    maxi = 0
    lines = f.readlines()
    f.close()
    i = 0
    for line in lines:
        i += 1
        linelen = len(line.strip())
        if linelen > longest:
            longest = linelen
            maxi = i
    return maxi,longest
    
#改进2：利用列表解析表达式处理文件的行
def find_longest_line2(filename):
    f = open(filename,'r')
    longest = 0
    maxi = 0
    lines = [ x.strip() for x in f.readlines() ]
    f.close()
    i = 0
    for line in lines:
        i += 1
        linelen = len(line)
        if linelen > longest:
            longest = linelen
            maxi = i
    return maxi,longest
    
#改进3：利用文件内置迭代器读取文件的行
def find_longest_line3(filename):
    f = open(filename,'r')
    lineslen = [ len(line.strip()) for line in f ]
    f.close()
    longest = 0
    maxi = 0
    i = 0
    for length in lineslen:
        i += 1
        if length > longest:
            longest = length
            maxi = i
    return maxi,longest
    
#改进4：为了节省内存，将列表解析改为生成器表达式
def find_longest_line4(filename):
    f = open(filename,'r')
    lt  = line_tuple(f)
    maxt = max( (x for x in lt), key=lambda y: y[1] )
    f.close()
    return maxt
    
#改进5：利用上下文管理器处理文件的开闭
def find_longest_line5(filename):
    with open(filename,'r') as f:
        lt = line_tuple(f)
        return max( (x for x in lt) ,key=lambda y: y[1])

#利用collections.Counter
def find_longest_line6(filename):
    with open(filename, 'r') as f:
        import collections
        lt = line_tuple(f)
        linedict = dict(lt)
        c = collections.Counter(linedict)
    return c.most_common(1)[0]