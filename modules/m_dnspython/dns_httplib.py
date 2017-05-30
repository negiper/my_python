#!/usr/bin/env python
#coding=utf-8

import dns.resolver as rer
import os
import httplib

iplist = []
domain = 'www.baidu.com'

def get_ip_list(domain=''):
    try:
        A = rer.query(domain, 'A').response.answer
    except Exception,e:
        print 'dns resolver error: '+ str(e)
        return
    
    for i in A:
        if i.rdtype == 1:
            for j in i.items:
                iplist.append(j.address)
    return True

def check_ip(ip):
    url = ip+':80'
    content = ''
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(url)
    
    try:
        conn.request('GET', '/', headers={'Host':domain})
        res = conn.getresponse()
        content = res.read(15)
        #print content
    finally:
        if content == '<!DOCTYPE html>':
            print ip + ' [OK]'
        else:
            print ip + ' [Error]'

if __name__ == '__main__':
    if get_ip_list(domain) and len(iplist)> 0:
        #print iplist
        for ip in iplist:
            check_ip(ip)
    else:
        print 'dns resolver error.'
