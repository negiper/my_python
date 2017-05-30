#coding=utf-8
#===================
#psutil 模块函数选录
#===================

def usage_percent(used,total,_round=None):
    '''
	计算资源使用百分比，分母为零时返回0.0或0
	同时保留用户要求精度
	'''
	try:
        ret = (used / total) * 100
    except ZeroDivisionError:
        ret = 0.0 if isinstance(used,float) or isinstance(total,float) else 0

    if _round is not None:
        return round(ret,_round)
    else:
        return ret

def isfile_strict(path):
	'''
	Same as os.path.isfile() but does not allow EACCES(无权限)/EPERM(操作不允许)
	'''
	try:
		st = os.stat(path)
	except OSError as err:
		if err.errno in (errno.EPERM, errno.EACCES):
			raise
		return False
	else:
		return stat.S_ISREG(st.st_mode)

#Process类的接口
def children(self,recursive=False):
    '''
    Return the children of this process as a list of Process 
    '''
    if hasattr(_psplatform, 'ppid_map'):
        '''windows only: obtain a (pid:ppid,...) dict for all running process
        '''
        ppid_map = _psplatform.ppid_map()
    else:
        ppid_map = None
    
    ret = []
    if not recursive:
        if ppid_map is None:
            #process_iter得到所有正在运行程序实例的生成器
            for p in process_iter():
                try:
                    if p.ppid() == self.pid:
                        if self.create_time() <= p.create_time():
                            ret.append(p)
                except (NoSuchProcess, ZombieProcess):
                    pass
        else:
            for pid,ppid in ppid_map.items():
                if ppid == self.pid:
                    try:
                        child = Process(pid)
                        if self.create_time() <= child.create_time():
                            ret.append(child)
                    except (NoSuchProcess, ZombieProcess):
                        pass
    else:
        table = collections.defaultdict(list)
        if ppid_map is None:
            for p in process_iter():
                try:
                    table[p.ppid()].append(p)
                except (NoSuchProcess, ZombieProcess):
                    pass
        else:
            for pid,ppid in ppid_map.items():
                try:
                    p = Process(pid)
                    table[ppid].append(p)
                except (NoSuchProcess, ZombieProcess):
                    pass
        checkpids = [self.pid]
        for pid in checkpids:
            for child in table[pid]:
                try:
                    intime = self.create_time() <= child.create_time()
                except (NoSuchProcess, ZombieProcess):
                    pass
                else:
                    if intime:
                        ret.append(child)
                        if child.pid not in checkpids:
                            checkpids.append(child.pid)
    return ret
