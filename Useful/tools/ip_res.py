#!/usr/bin/env python
#coding=utf-8

import os
import sys

IP = sys.argv[1]

get_ip_cmd = 'neutron floatingip-list | grep ' + IP
#print get_ip_id_cmd
ip_info = os.popen(get_ip_cmd).read().split('|')
ip_id = ip_info[1].strip()
fake_ip = ip_info[2].strip()

show_ip_cmd = 'neutron floatingip-show ' + ip_id + ' | grep tenant_id'
#print show_ip_cmd
tenant_id = os.popen(show_ip_cmd).read().split('|')[2].strip()
#print 'The tenant id is :', tenant_id

get_user_cmd = 'openstack user list --project ' + tenant_id + ' | grep -v "+"'
user = os.popen(get_user_cmd).readlines()[1].split('|')[2].strip()
print '用户:',user, '所属项目id:',tenant_id

router_id_cmd = 'neutron router-list --tenant-id ' + tenant_id + ' | grep ip_address'
router_id = os.popen(router_id_cmd).read().split('|')[1].strip()
print
print 'The Router id is :', router_id.strip()
l3_list_cmd = 'neutron l3-agent-list-hosting-router ' + router_id
l3_list = os.popen(l3_list_cmd).read().strip()
print l3_list

########################################
#根据tenant_id找到该项目下的所有资源
#  1.所有主机
#  2.每个主机关联ip（内网、假公网、公网）
#  3.每个主机关联的磁盘及信息
#  4.每个主机的系统信息
#######################################

#1和2: openstack server list --project <tenant_id>
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
print '-'*140
for sid in server_dict:
    netip = server_dict[sid]['Networks']
    str1 = netip.split('=')[1]
    ips = [ i.strip() for i in str1.split(',')]
    ips.append(IP) #??????
    
    fmt = sid + '\t' + server_dict[sid]['Name'] + ' '*2*(maxlen - len(server_dict[sid]['Name'].decode('utf8'))) + '\t' + server_dict[sid]['Status'] + '\t'*2 + server_dict[sid]['Host'] + '\t' + ', '.join(ips)
    if fake_ip in ips:
        #print '\033[32m'+server_dict[sid]['Name']+'\t'+server_dict[sid]['Status']+'\t'+ips+'\033[0m'
        #print '\033[32m',
        #print server_dict[sid]['Name'] + ' '*2*(maxlen - len(server_dict[sid]['Name'].decode('utf8'))),
        #print '\t',  server_dict[sid]['Status'],
        #print '\t',  ips,
        #print '\033[0m'
        print '\033[32m' + fmt + '\033[0m'
        HOST = sid
    else:
        print fmt

#3: cinder list --tenant <tenant_id>
print
print '\033[31m所有云硬盘：\033[0m'
disk_cmd = "cinder list --tenant " + tenant_id + " | grep -v '+' "  + r' | awk -F "|" "{ print \$2,\$4,\$5,\$6,\$9}"'
disk_list = [ t.strip() for t in os.popen(disk_cmd).readlines()]
#print disk_list
print ' '*15,disk_list[0]
print '-'*120
for dline in disk_list[1:]:
    if HOST in dline:
        dline = '\033[32m'+dline+'\033[0m'
        print dline
    else:
        print dline

#4: openstack server show <server_id>
