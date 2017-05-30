#/usr/bin/env python
#coding=utf-8
#filecmp 模块的简单练习

import filecmp

basedir = '/home/wx/python/test/'
dir1 = basedir + 'a'
dir2 = basedir + 'b'
print '----cmpfiles in %s and %s----' % (dir1,dir2)

#需要对比的文件列表，必须参数
print filecmp.cmpfiles(dir1, dir2, ['f1', 'f2', 'f3', 'f4', 'f5'])

print '-'*20
obj = filecmp.dircmp(dir1, dir2)
obj.report()
print '-'*20
obj.report_partial_closure()
print '-'*20
obj.report_full_closure()
