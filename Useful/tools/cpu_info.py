#!/usr/bin/env python

from collections import OrderedDict
from pprint import pprint

def CPUinfo():
    cpuinfo = []
    procinfo = OrderedDict()

    np = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                cpuinfo.append(procinfo)
                np = np + 1
                procinfo = OrderedDict()

            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
    return cpuinfo

if __name__ == "__main__":
    info = CPUinfo()
    for p in info:
        print 'processor\t:', p['processor']
        print 'vendor_id\t:', p['vendor_id']
        print 'model name\t:', p['model name']
        print 'cpu MHz\t\t:', p['cpu MHz']
        print '-'*30
