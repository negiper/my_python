import os
import string
import time

if os.name in ('nt','dos'):
    exefile = '.exe'
else:
    exefile = ''


def spawn(program,*args):
#    try:
#        return os.spawnvp(os.P_NOWAIT, program, (program,)+args)
#    except AttributeError:
#        pass
#
#    try:
#        spawnv = os.spawnv
#    except AttributeError:
        # assume it's unix
        pid = os.fork()
        if not pid:
            print '    ', os.getpid()
            os.execvp(program, (program,)+args)
        return os.wait()[0]
#    else:
#        for path in string.split(os.environ['PATH'],os.pathsep):
#            file = os.path.join(path,program) + exefile
#            try:
#                return spawnv(os.P_NOWAIT, file, (file,)+args)
#            except os.error:
#                pass
#        raise IOError, 'Cannot find executable'

print os.getpid(),':'
spawn('python', 'hello.py')
#time.sleep(1)
print 'goodbye!'

