#coding=utf-8
#模拟监控某一日志文件并提取特定的日志信息

import time

def pytail(f):
    '''
    python 版的tail命令
    '''
    
    f.seek(0,2)
    #将光标移动到文件的末尾
    #seek(offset, whence)
    #   offset: 以字节为单位的偏移量
    #   whence: 偏移量的计算模式：0(从文件都开始)；1(从当前位置开始)；2(从文件末尾开始)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line


def pygrep(lines, text):
    '''
    python 版的grep命令
    '''
    for line in lines:
        if text in line:
            yield line

if __name__ == '__main__':
    filename = 'test.txt'
    log = pytail(open(filename))
    pylog = pygrep(log, 'python')
    for line in pylog:
        print line
