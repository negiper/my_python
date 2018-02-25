#!/usr/bin/env python
#coding=utf-8

import os
import re
from pprint import pprint

#----------------------------------------#
# 系统内存使用情况
#----------------------------------------#

info = os.popen('cat /proc/meminfo').read()

total = re.search('MemTotal:\s*(.*)', info)
free = re.search('MemFree:\s*(.*)', info)
available = re.search('MemAvailable:\s*(.*)', info)
buff = re.search('Buffers:\s*(.*)', info)
cache = re.search('Cached:\s*(.*)', info)

#-----------------------------------------#

print '\033[32m系统内存使用情况\033[0m'
tmp = re.findall('((?:MemTotal|MemFree|MemAvailable|Buffers|(?<!\w)Cached):\s*.*)', info)
pprint(tmp)

#-----------------------------------------#
# 真实物理内存
#-----------------------------------------#

print '\033[32m真实物理内存\033[0m'

'''
info2 = os.popen('dmidecode -t memory | grep "Memory Device" -A11 | grep Size | grep -v "No Module Installed"').read()

size = [ t.strip() for t in info2.split('\n') if t.strip() ] 
total_size = sum([ int(t.split()[1]) for t in size ])/1024
total = 'TotalSize: ' + str(total_size) + 'GB'
size.insert(0,total)
print size
'''
info3 = os.popen('dmidecode -t memory | grep -E "(Size|Speed).*" | grep -vE "(No|Unknown|Configured)"').readlines()
lst = []
total_size = 0
if len(info3)<2:
    lst.append(info3[0].strip())
    total_size = int(info3[0].split()[1].strip())
else:
    for i in range(len(info3)/2):
        dt = {}
        dt['device'] = i
        dt['Size'] = info3[2*i].split(':')[1].strip()
        dt['Speed'] = info3[2*i+1].split(':')[1].strip()
        lst.append(dt)
        total_size = total_size + int(info3[2*i].split()[1])

lst.insert(0, 'Total_Size: %d GB' % (total_size/1024))
pprint(lst)

