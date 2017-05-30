#coding=utf-8

import platform
import getpass

print 'Welcome to your system: ',getpass.getuser()
print platform.node(),'on', platform.system()
