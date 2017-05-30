#coding=utf-8

import socket, sys
import hashlib

client = socket.socket()

client.connect(('localhost', 9999))

while True:
    cmd = raw_input('>>: ').strip()

    if len(cmd) == 0:
        continue
    if cmd.startswith('get'):
        client.send(cmd)
        file_size = client.recv(1024)
        print 'file_size: ', file_size

        client.send('ready for seceive file.')
        file_size = int(file_size)
        recv_size = 0
        filename = cmd.split()[1]
        f = open(filename + '.new' ,'wb')
        m = hashlib.md5()
        
        while recv_size < file_size:
            rest_size = file_size - recv_size
            if rest_size < 1024:
                data = client.recv(rest_size)
            else:
                data = client.recv(1024)
            recv_size += len(data)
            m.update(data)
            f.write(data)
            sys.stdout.write('\r')
            sys.stdout.write('%d%%' % (int(recv_size)*100/file_size))
            sys.stdout.flush()
        else:
            client_md5 = m.hexdigest()
            print '\nfile receive dong!'
            f.close()
        server_md5 = client.recv(1024)
        print server_md5, client_md5

client.close()
        
