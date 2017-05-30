#coding=utf-8
'''
简单的文件备份脚本
'''

import os
import os.path
import sys
import shutil
import time
import contextlib

TMPDIR = 'tmp_backup'
CONF = 'backup.cnf'
CWD = os.path.dirname(os.path.abspath(__file__))
__all__ = [ 'config', 'run']

def config():
    with open(CONF,'w') as f:
        path = raw_input("Please input the files or directory to backup:\n")
        while path:
            f.write(path + '\n')
            path = raw_input()
          

@contextlib.contextmanager
def tmp_dir():
    try:
        os.chdir(CWD)
        os.mkdir(TMPDIR)
        yield
    except Exception as e:
        print 'Backup failed',e
    finally:
        os.chdir(CWD)
        shutil.rmtree(TMPDIR)
        

def source_files():
    with open(CONF) as f:
        files = f.readlines()
        return [x.strip() for x in files]
        
def copy_file(source,target_dir):
    if os.name == 'nt':
        path = source.split(':\\')[1]
    else:
        path = source if source[:1] != '/' else source[1:]
    target = os.path.join(target_dir,path)
    
    if not os.path.exists(target):
        dir,filename = os.path.split(target)
        if not os.path.exists(dir):
            os.makedirs(dir)
        shutil.copy(source,target)
        print 'backup',source

    elif os.path.getmtime(source) > os.path.getmtime(target):
        shutil.copy(source,target)
        print 'backup',source

def copy_dir(top,target_dir):
    for root,dirs,files in os.walk(top):
        for f in files:
            filepath = os.path.join(root,f)
            copy_file(filepath,target_dir)

def usage():
    print 'Usage:'
    print os.path.basename(__file__),'[target_dir]'

def run():
    import zipfile
    
    if len(sys.argv) == 2:
        backup_dir = sys.argv[1]
    elif len(sys.argv) == 1:
        backup_dir = CWD
    else:
        usage()
        return
    config()
    
    sfiles = source_files()
    date = time.strftime('%y_%m_%d_%H_%M_%S')
    #FLAG = False
    if os.name == 'nt':
        #prog = '"D:\\Program Files\\7-Zip\\7z.exe"'
        #parms = ' a backup_%s.7z %s' % (date,target_dir)
        #os.system(prog + parms)
        backup_file = 'backup_%s.zip' % date
        with zipfile.ZipFile(backup_file,'w',compression=zipfile.ZIP_DEFLATED) as zf:
            for path in sfiles:
                if os.path.isdir(path):
                    for root,dirs,files in os.walk(path):
                        for dirname in sorted(dirs):
                            dirpath = os.path.join(root,dirname)
                            zf.write(dirpath,dirpath)
                        for filename in files:
                            filepath = os.path.join(root,filename)
                            zf.write(filepath,filepath)
                else:
                    zf.write(path,path)
        os.system('move backup_%s.zip %s' % (date,backup_dir))
    elif os.name == 'posix':
        with tmp_dir():
            target_dir = os.path.abspath(TMPDIR)
            for f in sfiles:
                if os.path.isdir(f):
                    copy_dir(f,target_dir)
                else:
                    copy_file(f,target_dir)
            os.chdir(target_dir)
            os.system('tar -czf backup_%s.tar.gz *' % date)
            os.system('mv backup_%s.tar.gz %s' %(date,backup_dir))

if __name__ == '__main__':
    run()