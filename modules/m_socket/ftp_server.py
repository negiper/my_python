#coding=utf-8

import socket, os, time
import hashlib

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(2)

while True:
    conn, addr = server.accept()
    print 'new connection: ', addr

    while True:
        print 'Waiting for command...'
        data = conn.recv(1024)
        if not data:
            print 'client disconnect!'
            break

        cmd, filename = data.split()
        if os.path.isfile(filename):
            f =  open(filename, 'rb')
            m = hashlib.md5()
            
            file_size = os.stat(filename).st_size
            conn.send(str(file_size))
            conn.recv(1024)

            for line in f:
                m.update(line)
                conn.send(line)

            server_md5 = m.hexdigest()
            #print 'file md5: ', m.hexdigest()
            f.close()
            conn.send(server_md5)

        print 'send done!'

server.close()
                
