#!/usr/bin/env python

import os
from pprint import pprint

def load_stat():
    loadavg = {}
    f = open('/proc/loadavg')
    load = f.read().split()
    f.close()
    loadavg['avg_1'] = load[0]
    loadavg['avg_5'] = load[1]
    loadavg['avg_15'] = load[2]
    loadavg['current/total'] = load[3]
    loadavg['last_pid'] = load[4]
    return loadavg

pprint(load_stat())
