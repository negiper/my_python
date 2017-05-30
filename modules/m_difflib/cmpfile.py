#!/usr/bin/env python
#coding=utf-8
#===============================
#比较文件的差异并输出为html文件
#===============================

import sys
import difflib

try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
except Exception as e:
    print 'Error:',e
    print 'Usage: cmpconf.py filename1,filename2'
    sys.exit()

def readfile(filename):
    try:
        with open(filename,'rb') as f:
            text = f.read().splitlines()
    except IOError as e:
        print 'Read file error:',e
        sys.exit()
    return text
    
text1_lines = readfile(file1)
text2_lines = readfile(file2)

hd = difflib.HtmlDiff()
outfilename = file1.rsplit('.',1)[0]+'_to_'+file2.rsplit('.',1)[0]+'.html'
with open(outfilename,'w') as f:
    f.write(hd.make_file(text1_lines,text2_lines))

