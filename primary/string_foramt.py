#coding=utf-8
#字符串拼接的几种方式

name = 'Jenny'
age = 18
job = 'Taobaomeimei'
salary = 5000

info = '''
----------info of %s----------
name: %s
age: %s
job: %s
salary: %s
'''%(name,name,age,job,salary)

info2 = '''
----------info of {_name}----------
name: {_name}
age: {_age}
job: {_job}
salary: {_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)

info3 = '''
----------info of {0}----------
name: {0}
age: {1}
job: {2}
salary: {3}
'''.format(name,age,job,salary)

print info
print info2
print info3
