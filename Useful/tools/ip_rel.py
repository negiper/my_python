#!/usr/bin/env python
#coding=utf-8
#author:negiper, lvlei@tzyun.com
#date:	Thu Dec 21 22:30:54 CST 2017

##################################################################
#根据公网ip找到和该ip关联的所有资源
# 1.该ip所属用户  
# 2.该ip绑定的路由信息
# 3.用户拥有的所有主机
# 4.每个主机的信息及关联ip（内网、假公网、公网），
# 5.所有磁盘及信息
#################################################################
import os
import sys
import subprocess
from pprint import pprint
from subprocess import Popen

### 1、2
################
IP = sys.argv[1]
print '正在查询',IP,'关联信息....\n'
get_ip_cmd = 'neutron floatingip-list | grep ' + IP
ip_info = Popen(get_ip_cmd,shell=True,stdout=subprocess.PIPE)
IPS = ip_info.communicate()[0].split('|')
ip_id = IPS[1].strip()
FAKE_IP = IPS[2].strip()

show_ip_cmd = 'neutron floatingip-show ' + ip_id + ' | grep tenant_id'
tenant_info = Popen(show_ip_cmd,shell=True,stdout=subprocess.PIPE)
tenant_id = tenant_info.communicate()[0].split('|')[2].strip()

get_user_cmd = 'openstack user list --project ' + tenant_id + ' | grep -v "+"'
router_id_cmd = 'neutron router-list --tenant-id ' + tenant_id + ' | grep ip_address'
user_info = Popen(get_user_cmd,shell=True,stdout=subprocess.PIPE)
router_info = Popen(router_id_cmd,shell=True,stdout=subprocess.PIPE)
user = user_info.communicate()[0].splitlines()[1].split('|')[2].strip()
router_id = router_info.communicate()[0].split('|')[1].strip()

l3_list_cmd = 'neutron l3-agent-list-hosting-router ' + router_id
l3_info = Popen(l3_list_cmd,shell=True,stdout=subprocess.PIPE)
l3_list = l3_info.communicate()[0].strip()


print '用户:',user, '所属项目id:',tenant_id
print
print 'The Router id is :', router_id.strip()
print l3_list


### 3、4
#############
print
server_cmd = 'openstack server list --long --project ' + tenant_id + ' | grep -v "+"'
server_list = os.popen(server_cmd).readlines()
server_dict = {}
items = [ item.strip() for item in server_list[0].split('|') if item.strip() ]
flags = [1,1,1,0,0,1,0,1,0]
for j in range(1,len(server_list)):
    sj = [ s.strip() for s in server_list[j].split('|')[1:-1] ]
    dj = {}
    for i in range(1,len(items)):
        if flags[i]:
            dj[items[i]]=sj[i]
    server_dict[sj[0]]=dj

print '\033[31m用户',user,'下的所有主机：\033[0m'
maxlen = max(map(len, [ server_dict[s]['Name'].decode('utf8') for s in server_dict.keys() ]))
HOST = ''

print ' '*17 + 'ID' + ' '*17 + '\t' + ' '*((maxlen*2-4)/2) + 'Name' + ' '*((maxlen*2-4)/2) + '\t' + 'Status' + '\t'*2 + '  Host   ' + '\t' + ' '*17 + 'Networks'
print '-'*150
#pprint(server_dict)

Li = []
Lp = []
Ln = []
Servers = server_dict.keys()
for sid in Servers:
    netip = server_dict[sid]['Networks']
    if netip:
        str1 = netip.split('=')[1]
        pp = [ i.strip() for i in str1.split(',')]
        Li.append(pp)
        if len(pp) > 1:
            fake_ip = pp[1]
            fake_ip_cmd = 'neutron floatingip-list | grep ' + fake_ip +' | awk -F "|" "{print \$4}"'
            Lp.append(Popen(fake_ip_cmd,shell=True,stdout=subprocess.PIPE))
        else:
            Lp.append(0)
    else:
        Li.append(0)
        Lp.append(0)
    instance_cmd = 'nova show ' + sid + ' | grep instance_name | awk -F "|" "{print \$3}"'
    Ln.append(Popen(instance_cmd,shell=True,stdout=subprocess.PIPE))

I = 0
for sid in Servers:
    ips = []
    if Li[I]:
        inner_ip = Li[I][0]
        ips.append(inner_ip)
        if len(Li[I]) > 1 and Lp != 0:
            fake_ip = Li[I][1]
            ips.append(fake_ip)
            public_ips = Lp[I].communicate()[0].splitlines()
            public_ip = [ ip.strip() for ip in public_ips if fake_ip not in ip ]
            if public_ip:
                ips.append(public_ip[0])
    
    instance_name = Ln[I].communicate()[0].strip()
    
    namelen = len(server_dict[sid]['Name'].decode('utf8'))
    fmt = sid + '\t' + server_dict[sid]['Name'] + ' '*(maxlen - namelen) + '\t' + server_dict[sid]['Status'] + '\t'*2 + server_dict[sid]['Host'] + '(' + instance_name + ')' + '\t' + ', '.join(ips)
    if FAKE_IP in ips:
        print '\033[33m' + fmt + '\033[0m'
        HOST = sid
    else:
        print fmt

    I = I + 1


### 5
####################
print
print '\033[31m所有云硬盘：\033[0m'
disk_cmd = "cinder list --tenant " + tenant_id + " | grep -v '+' "  + r' | awk -F "|" "{ print \$2,\$4,\$5,\$6,\$9}"'
disk_list = [ t.strip() for t in os.popen(disk_cmd).readlines()]
#print disk_list
print ' '*15,disk_list[0]
print '-'*110
for dline in disk_list[1:]:
    if HOST in dline:
        dline = '\033[33m'+dline+'\033[0m'
        print dline
    else:
        print dline

