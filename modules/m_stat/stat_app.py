#!/usr/bin/env python
#coding=utf-8
#==================
#stat 模块应用实例
#==================

from __future__ import division

def fileType(mode):
    '''
    通过文件的mode信息返回文件的具体类型
    '''
    import stat
    FMT = [ t for t in dir(stat) if t.startswith('S_IF') and t != 'S_IFMT' ]
    smode = stat.S_IFMT(mode)
    for file_type in FMT:
        if getattr(stat,file_type) == smode:
            return file_type


def abs_info(fileName):
    '''
    返回文件的概要信息：
    文件类型(Type)
    文件所有者(UserName)
    文件大小(Size)
    文件最后修改时间(Mtime)
    文件的绝对路径(FilePath)
    '''
    import os,stat,time
    from collections import namedtuple
    AbsInfo = namedtuple('abs_info',['Type', 'UserName', 'Size', 'Mtime', 'FilePath' ])
    st = os.stat(fileName)
    info_type = fileType(st.st_mode)
    
    if os.name == 'nt':
        import getpass
        info_user = getpass.getuser()
    elif os.name == 'posix':
        import pwd
        info_user = pwd.getpwuid(st.st_uid).pw_name
    else:
        info_user = '-'
    
    info_size = st.st_size
    suffix = ''
    sl = [ 'K', 'M', 'G', 'T' ]
    while eval(str(info_size) + '/ 1024') >= 1.0:
        info_size = eval(str(info_size) + '/ 1024')
        suffix = sl.pop(0)
    info_size = str(info_size) + suffix
    
    info_mtime = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(st.st_mtime))
    
    info_path = os.path.abspath(fileName)
    
    info = AbsInfo(info_type,info_user,info_size,info_mtime,info_path)
    return info

