#coding=utf-8
#=========================
# 上下文管理器：contextlib
# with 语句的作用类似于try...finally...，提供一种上下文机制。要使用with语句的类，其内部必须提供两个内置函数__enter__以及__exit__，前者在主体代码执行前执行，后者则在主体代码执行后执行(注：as后面的变量由__enter__函数返回)
#==========================

import contextlib

class echo(object):
    def output(self,s):
        print s
        print ':',
    
    def __enter__(self):
        print  '-'*10,'Hello,world!', '-'*10
        print ':',
        return self
       
    def __exit__(self,exc_type,exc_value,traceback):
        print '\nexit.'
        if exc_type == ValueError:
            return True
        else:
            return False

#数据库的连接、查询、关闭处理
class Database(object):
    def __init__(self):
        self.connected = False
    
    def connect(self):
        print 'Connecting the database...'
        self.connected = True
        print 'connected.'
        
    def close(self):
        self.connected = False
        print 'Connection was closed.'
        
    def query(self):
        if self.connected:
            return 'query data.'
        else:
            raise ValueError('DB not connected')
    
    #利用with语句实现数据库的连接与释放
    def __enter__(self):
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

def handle_query():
    db = Database()
    db.connect()
    print 'Query:',db.query()
    db.close()

#对上述数据库操作的改进——装饰器
def connect_db(fun):
    import functools
    
    
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        print u'利用装饰器为数据库的查询操作添加连接和关闭操作'
        db = Database()
        db.connect()
        ret = fun(db, *args, **kwargs)
        db.close()
        return ret
    return wrapper

@connect_db
def handle_query1(db=None):
    print 'handle---',db.query()

#对于实现了上下文协议(实现了__enter__,__exit__方法)的对象即可利用with语句
def handle_query2():
    print u'利用上下文管理器为数据库的查询操作提供进入的连接和退出的关闭操作——实现上下文协议'
    with Database() as db:
        print 'handle---',db.query() 

#利用contextlib将函数转换为一个上下文管理器
@contextlib.contextmanager
def database():
    db = Database()
    try:
        if not db.connected:
            db.connect()
        yield db
    except Exception as e:
        print e
    finally:
        db.close()
  
def handle_query3():
    print u'利用上下文管理器为数据库的查询操作提供进入的连接和退出的关闭操作——利用contextlib模块'
    with database() as db:
        print 'handle----',db.query()

if __name__ == '__main__':
    with echo() as e:
        e.output('Hi!')
        e.output("What's your name?")
        e.output('Nice to meet you!')

    with echo() as e:
        raise ValueError("Nothing input")

    # with echo() as e:
        # raise Exception('Unknown Error.')
    print '\n'
    print '-'*20
    print u'数据库操作的基本流程：'
    handle_query()
    print 
    handle_query1()
    print 
    handle_query2()
    print 
    handle_query3()