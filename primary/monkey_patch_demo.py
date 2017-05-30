#coding=utf-8
#======================
#Monkey patch 简单示例
#======================

#patch 类方法，对所有示例都有影响
class MyClass(object):
    def add(self,x,y):
        return x + y

#利用新方法patch原方法        
def new_add(self,x,y):
    return len(str(x)) + len(str(y))
    
obj = MyClass()
#print obj.add(32,13)
# MyClass.add = new_add
# print obj.add(32,13)

# inst = MyClass()
# print inst.add(345,21)

old_add = MyClass.add
#扩充原方法的功能
def extend_add(self,x,y):
    return old_add(self,x,y) + 1
    
print obj.add(3,3)
MyClass.add = extend_add
print obj.add(3,3)

#-------------------------
#patch 类方法，仅对某个实例有用
import types
class MyClass2(object):
    def add(self,x,y):
        return x + y
    
    def become_more_powerful(self):
        old_add = self.add
        def more_powerful_add(self,x,y):
            return old_add(x,y) + 1
        self.add = types.MethodType(more_powerful_add,self)
    
obj1 = MyClass2()
print obj1.add(3,3)
obj1.become_more_powerful()
print obj1.add(3,3)
obj1.become_more_powerful()
obj1.become_more_powerful()
obj1.become_more_powerful()
print obj1.add(3,3)

obj2 = MyClass2()
print obj2.add(3,3)