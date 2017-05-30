#coding=utf-8
# 列出某个路径下的所有文件
#This is a new line

import os
import os.path

def file_List(path):
    for root,dirs,files in os.walk(path,topdown=False):
	for name in files:
		print os.path.join(root,name)
	
	for name in dirs:
		print os.path.join(root,name)

if __name__ == '__main__':
	path = raw_input('Input the path: ')
	file_List(path)
