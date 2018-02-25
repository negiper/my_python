import os
from pprint import pprint

IP = '182.242.138.15'
fake_ip = '192.192.3.125'

server_list = os.popen('cat test | grep -v "+"').readlines()
server_dict = {}
items = [ item.strip() for item in server_list[0].split('|') if item.strip() ]
for j in range(1,len(server_list)):
    sj = [ s.strip() for s in server_list[j].split('|')[1:-1] ]
    dj = {}
    for i in range(1,len(items)):
        dj[items[i]]=sj[i]
    server_dict[sj[0]]=dj
print len(server_dict)
#pprint(server_dict)

for sid in server_dict:
    netip = server_dict[sid]['Networks']
    str1 = netip.split('=')[1]
    ips = [ i.strip() for i in str1.split(',')]
    ips.append(IP)
    if fake_ip in ips:
        print '\033[32m',server_dict[sid]['Name'],'\t',server_dict[sid]['Status'],'\t',ips,'\033[0m'
    else:
        print server_dict[sid]['Name'],'\t',server_dict[sid]['Status'],'\t',ips


