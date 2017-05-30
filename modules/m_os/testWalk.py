import os
import os.path as path

def testwalk(top,topdown=True,onerror=None,followlinks=False):
    names = os.listdir(top)

    dirs,nondirs = [],[]
    for name in names:
        if path.isdir(path.join(top,name)):
            dirs.append(name)
        else:
            nondirs.append(name)

    if topdown:
        yield top,dirs,nondirs
    for name in dirs:
        new_path = path.join(top,name)
        if followlinks or not path.islink(new_path):
            for a,b,c in testwalk(new_path,topdown,onerror,followlinks):
               yield a,b,c
            #testwalk(new_path,topdown,onerror,followlinks)
    if not topdown:
        yield top,dirs,nondirs
        
