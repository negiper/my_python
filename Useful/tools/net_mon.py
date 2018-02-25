#!/usr/bin/env Python
#coding=utf-8
import time
import sys

if len(sys.argv) > 1:
    INTERFACE = sys.argv[1]
else:
    INTERFACE = 'eth0'

print 'Interface: ', INTERFACE

def Stat():
    info = open('/proc/net/dev').readlines()
    for line in info:
        if INTERFACE in line:
            rev = float(line.split()[1])
            send = float(line.split()[9])
    return [rev, send]
    
print '\t', '  In   ', '\t', '  Out'
stat = Stat()

while True:
    time.sleep(1)
    old = stat
    new = Stat()
    RX_rate = round((float(new[0])-float(old[0]))/1024/1024, 3)
    TX_rate = round((float(new[1])-float(old[1]))/1024/1024, 3)
    stat = new
    print '\t', RX_rate, 'MB    ','\t', TX_rate, 'MB'


