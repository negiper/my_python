#coding=utf-8
#----------------
# os 模块源码解析
#----------------

#windows 平台
from nt import *
import ntpath as path

#------------os.renames ---------
def renames(old,new):
    #若新路径不存在，则利用makedirs创建
    head,tail = path.split(new)
    if head and tail and not path.exists(head):
        makedirs(head)

    #rename 更改最后一级的文件或目录名
    rename(old,new)

    #尽量删除原路径中的空目录
    head,tail = path.split(old)
    if head and tail:
        try:
            removedirs(head)
        except error:
            pass


#-----------os.walk ------------
def walk(top,topdown=True,onerror=None,followlinks=False):
    try:
        names = listdir(top)
    except error,err:
        if onerror is not None:
            onerror(err)
        return
    dirs,nondirs = [],[]
    for name in names:
        if isdir(join(top,name)):
            dirs.append(name)
        else:
            nondirs.append(name)
    #topdown为True 相当于广度优先遍历
    if topdown:
        yield top,dirs,nondirs
    for name in dirs:
        new_path = join(top,name)
        if followlinks or not islink(new_path):
            #需要在高层函数中定义用于接收深层调用的返回值并返回，否则递归结束后深层
            #调用的结果将会丢失
            for x in walk(new_path,topdown,onerror,followlinks):
                yield x
    #topdown为False 相当于深度优先遍历
    if not topdown:
        yield top,dirs,nondirs

