#coding=utf-8

#socket网络编程——server端
import os
import socket

server = socket.socket()

server.bind(('localhost', 6969))
server.listen(2)

print('Waiting for client\'s connection...')
conn, addr = server.accept()
print('The connected client: ', addr)

#f = open('test.flac', 'rb')
while True:
    print 'Waiting for cmd: '
    data = conn.recv(1024)
    if not data:
        break

    print('The client request: ', data)

    #接发数据
    #conn.send(data.upper())
    
    #执行命令
    res = os.popen(data).read()
    #conn.send(res)

    #接发文件
    
    #res = f.read()
    print len(res)
    conn.send(str(len(res)))
    ack = conn.recv(1024)    #为了解决两次连续发送产生的粘包问题
    print ack
    conn.sendall(res)
    
server.close()
