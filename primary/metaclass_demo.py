#coding=utf-8
#==================
#元类简单示例
#==================

def upper_attr(cls_name,bases,attrs):
    attrs = ((name,value) for name,value in attrs.items() if not name.startswith('_'))
    
    upper_attrs = dict((name.upper(),value) for name,value in attrs)
    
    return type(cls_name,bases,upper_attrs)
    
#__metaclass__ = upper_attr

class Foo(object):
    __metaclass__ = upper_attr
    bar = 'Hello'
    
print hasattr(Foo, 'bar')
print hasattr(Foo, 'BAR')
print Foo.BAR

class UpperAttrMetaClass(type):
    def __new__(cls,name,bases,dct):
        attrs = ((name,value) for name,value in dct.items() if not name.startswith('_'))
    
        upper_attrs = dict((name.upper(),value) for name,value in attrs)
        
        return type.__new__(cls,name,bases,upper_attrs)
        
class Person(object):
    __metaclass__ = UpperAttrMetaClass
    name = 'python'
    age = 26

print hasattr(Person, 'name')
print hasattr(Person, 'AGE')
print Person.NAME,Person.AGE