from functools import update_wrapper, wraps

def wrap(func):
    def call_it(*args, **kwargs):
        '''wrap func: call_it'''
        print 'before call'
        return func(*args, **kwargs)
    return call_it

@wrap
def hello():
    '''say hello'''
    print 'hello python!'

def wrap2(func):
    def call_it(*args, **kwargs):
        '''wrap func: call_it2'''
        print 'before call'
        return func(*args, **kwargs)
    return update_wrapper(call_it, func)

@wrap2
def hello2():
    '''test hello'''
    print 'hello python2!'

def wrap3(func):
    @wraps(func)
    def call_it(*args, **kwargs):
        '''wrap func: call_it3'''
        print 'before call'
        return func(*args, **kwargs)
    return call_it

@wrap3
def hello3():
    '''hello again'''
    print 'hello python3!'


if __name__ == '__main__':
    hello()
    print hello.__name__
    print hello.__doc__

    print
    hello2()
    print hello2.__name__
    print hello2.__doc__

    print
    hello3()
    print hello3.__name__
    print hello3.__doc__
