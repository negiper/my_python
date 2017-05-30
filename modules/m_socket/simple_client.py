#coding=utf-8

#socket 网络编程——client端

import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost', 6969))
#f = open('mytest.flac', 'wb')

while True:
    req = raw_input('Input Your request: ').strip()
    if len(req) == 0:
        break
    client.send(req)
    
    while True:
        #client.setblocking(0)
        data_size = client.recv(1024)   #接收数据的大小
        print 'Data size: ', data_size
        client.send('ok, ready for receiving!')
        
        '''
        if len(data) < 4096:
            print 'receive complete!'
            f.write(data)
            break
        '''
        #接收指定大小的数据
        size = 0
        received_data = ''
        while size < int(data_size):
            data = client.recv(1024)
            received_data += data
            size += len(data)
        else:
            print received_data
            print 'receive dong!'
            break
        #f.write(data)

#f.close()
client.close()


