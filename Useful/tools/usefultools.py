#!/usr/bin/env python
#coding=utf-8
#===================
#自定义实用工具
#===================
'''
Custom useful tools.
''' 
__all__ = []
import os,pdb,sys

def Dir(obj=None):
    '''
    打印对象对外提供的有用接口
    '''
    if obj is None:
        #获取shell名字空间中的对象
        ret = dir(sys.modules['__main__'])
    else:
        if hasattr(obj,'__all__'):
            ret = sorted(obj.__all__)
        else:
            ret = dir(obj)
    return [attr for attr in ret if not attr.startswith('_')]

def ls(path):
    '''
    列出指定目录下的文件
    '''
    file_list = os.listdir(path)
    maxlen = max([len(x) for x in file_list])
    if os.name == 'nt':
        import ctypes
        from ctypes import windll,create_string_buffer
        h = windll.kernel32.GetStdHandle(-11)
        sbinfo = create_string_buffer(22)
        try:
            res = windll.kernel32.GetConsoleScreenBufferInfo(h,sbinfo)
        except:
            return None
        if res:
            import struct
            '''
            struct.unpack(fmt,string)
            #unpack 参数fmt：
                h: (short)              integer
                H: (unsigned short)    integer
                s: (char[])             string
                x: (pad byte)           no value
                b: (signed char)        integer
                B: (unsigned char)      integer
                i: (int)                 integer
                I: (unsigned int)       integer
                
            #len(string) == struct.calcsize(fmt)
           '''
            size_x,size_y,curse_x,curse_y,wattr,left,top,right,bottom,max_x,max_y = struct.unpack('hhhhHhhhhhh', sbinfo.raw)
            width = right - left - 2
    elif os.name == 'posix':
        width = int(os.popen('stty size').read().split()[1]) - 2
    else:
        print 'Not support!'
        return -1
    ColNum = width // maxlen
    ColPos = [i*maxlen for i in range(ColNum)]
    cn = 1
    cp = 0
    for fn in file_list:
        fill = ColPos[cn-1] - cp
        if os.path.isdir(fn):
            fn = fn + '/'
        print ' '*fill + fn,
        if cn == ColNum:
            cn = 1
            cp = 0
            print
        else:
            cn += 1
            cp += fill + len(fn)
    return

def printf(filename):
    '''
    显示文件内容
    '''
    if not os.path.exists(filename):
        print 'Error: %s not exist!' % (filename)
        return 1
    if not os.path.isfile(filename):
        print 'Error: %s is not a file!' % (filename)
        return 2
    with open(filename) as f:
        print f.read()
    return 

def dir_tree(path,indent=''):
    '''
    打印目录树
    '''
    print indent[:-2] + indent[-2:].replace(' ','-') + os.path.basename(path),':'
    file_list = os.listdir(path)
    dirs = []
    indent += '|  '
    for f in file_list:
        f_path = os.path.join(path,f)
        if os.path.isdir(f_path):
            dirs.append(f_path)
        else:
            print indent+f
    for d in dirs:
        dir_tree(d,indent)

def Help(*args,**kwargs):
    '''
    对内置功能help的改进——可以对查询内容进行增量查看。
    默认每次查看10行，可以通过关键字参数lines设定
    '''
    import sys,contextlib
    tmpfile_path = 'E:\\python\\files\\myenv\\Tmp\\tmpfile_for_help'
    num = kwargs['lines'] if 'lines' in kwargs else 10
    @contextlib.contextmanager
    def print_to_file(fd):
        stdout = sys.stdout
        try:
            sys.stdout = fd
            yield
        except Exception:
            pass
        finally:
            sys.stdout = stdout
    
    with open(tmpfile_path,'w') as f:
        with print_to_file(f) as t:
            ret = help(*args, **kwargs)
    
    with open(tmpfile_path) as f:
        lines = f.readlines()
        pos = 0
        choice = ''
        while lines[pos:pos+num] and choice == '':
            print ''.join(lines[pos:pos+num])
            choice = raw_input()
            pos += num
        else:
            return 
    return 
    
__all__.extend(['Dir', 'ls','printf' ,'dir_tree','Help'])
