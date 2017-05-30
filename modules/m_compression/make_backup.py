#coding=utf-8
#=====================
#全量和增量备份脚本
#=====================

import time
import os
import zipfile
import tarfile
import cPickle as p
import hashlib

def cal_md5(fname):
    m = hashlib.md5()
    with open(fname) as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            m.update(data)
    return m.hexdigest()
    
def full_backup(src_dir,dst_dir,md5file):
    par_dir,base_dir = os.path.split(src_dir.rstrip('/'))
    back_name = '%s_full_%s' % (base_dir,time.strftime('%y-%m-%d'))
    full_name = os.path.join(dst_dir,back_name)
    md5dict = {}
    if os.name == 'nt':
        full_name += '.zip'
        with zipfile.ZipFile(full_name,'w',compression=zipfile.ZIP_DEFLATED) as zf:
            for root,dirs,files in os.walk(src_dir):
                for fname in files:
                    path = os.path.join(root,fname)
                    zf.write(path)
                    md5dict[path] = cal_md5(path)
        with open(md5file,'w') as f:
            p.dump(md5dict,f)
    elif os.name == 'posix':
        full_name += '.tar.gz'
        for root,dirs,files in os.walk(src_dir):
            for fname in files:
                path = os.path.join(root,fname)
                md5dict[path] = cal_md5(path)
        with open(md5file,'w') as f:
            p.dump(md5dict,f)
        #linux:
        tar = tarfile.open(full_name,'w:gz')
        tar.add(src_dir)
        tar.close()
        
def incr_backup(src_dir,dst_dir,md5file):
    par_dir,base_dir = os.path.split(src_dir.rstrip('/'))
    back_name = '%s_incr_%s' % (base_dir,time.strftime('%y-%m-%d_%H_%M'))
    full_name = os.path.join(dst_dir,back_name)
    md5new = {}
    
    with open(md5file) as f:
        md5old = p.load(f)
        
    for root,dirs,files in os.walk(src_dir):
        for fname in files:
            path = os.path.join(root,fname)
            md5new[path] = cal_md5(path)
    with open(md5file, 'w') as f:
        p.dump(md5new,f)
        
    if os.name == 'posix':
        full_name += '.tar.gz'
        t_z = tarfile.open(full_name,'w:gz')
        fun = t_z.add
    elif os.name == 'nt':
        full_name += '.zip'
        t_z = zipfile.ZipFile(full_name,'w',compression=zipfile.ZIP_DEFLATED)
        fun = t_z.write
    else:
        fun = ''
    if fun:
        for key in md5new:
            if md5old.get(key) != md5new[key]:
                fun(key)
    t_z.close()
    

if __name__ == '__main__':
    src_dir = raw_input('src_dir:')
    dst_dir = raw_input('dst_dir:')
    md5file = raw_input('md5file:')
    
    if time.strftime('%a') == 'Mon':
        full_backup(src_dir,dst_dir,md5file)
    else:
        incr_backup(src_dir,dst_dir,md5file)
    