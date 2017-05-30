#coding=utf-8
# 列出某个路径下的所有文件

import os
import os.path

def fileList(path):
    for root,dirs,files in os.walk(path,topdown=False):
	for name in files:
		print os.path.join(root,name)
	
	for name in dirs:
		print os.path.join(root,name)


if __name__ == '__main__':
	path = raw_input('Iput the path: ')
	fileList(path)
