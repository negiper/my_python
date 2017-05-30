#coding=utf-8

import sys, os
import atexit
import time
import psutil

def get_cpu_status(interval=1):
    return ('CPU: ' + str(psutil.cpu_percent(interval)) + '%')

def get_mem_status():
    mem = psutil.virtual_memory()

    line = 'Memory: %s%% %s/%s' % (
        mem.percent,
        str(int(mem.used/1024/1024)) + 'M',
        str(int(mem.total/1024/1024)) + 'M')
    return line

def simplify(n):
    '''
    简化数值大小为可读形式
    '''

    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    bases = {}
    for i, s in enumerate(symbols):
        bases[s] = 1 << (i+1)*10

    for s in reversed(symbols):
        if n >= bases[s]:
            value = float(n)/bases[s]
            return '%.2f %s' % (value, s)
    return '%.2f B' % (n)

def refresh_window(args):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(time.asctime() + '|' + args['cpu_status'] + '|' + args['mem_ststus'])

    #总的网络状态
    print('Network Status')
    print('total bytes:     send: %-10s    received: %s' %
          (simplify(args['tot_after'].bytes_sent), simplify(args['tot_after'].bytes_recv)))
    print('total packets:   send: %-10s    received: %s' %
          (simplify(args['tot_after'].packets_sent), simplify(args['tot_after'].packets_recv)))

    #每个网卡的网络状态
