#coding=utf-8
#========================
#WSGI接口
#========================

#对于网路服务我们希望有一个统一的接口为我们提供底层的请求、解析和响应，从而我们可以专注于上层代码的编写。
#这个接口就是WSGI：Web Server Gateway Interface

#WSGI接口定义非常的简单，他只需要web开发者实现一个函数，就可以响应HTTP请求。

def application(environ,start_respose):
    start_respose('200 ok', [('Content_Type', 'text/html')])
    return '<h1>Hello, web!</h1>'
    
#上面的application函数就是符合WSGI标准的一个HTTP请求处理函数
#   environ：一个包含所有HTTP请求信息的dict对象
#   start_respose：一个发送HTTP响应的函数。

#有了WSGI，我们关心的就是如何从environ这个dict对象中拿到HTTP请求信息，然后得到HTML，通过 start_respose发送响应Header，最后返回Body。

#此处定义的application必须有WSGI服务器来调用
#python内置了一个用于测试的WSGI服务器————wsgiref

from wsgiref.simple_server import make_server
httpd = make_server('', 45453, application)
print 'Serving HTTP on port 45453...'
httpd.serve_forever()

#运行该文件之后，通过浏览器访问localhost:45453
#即可得到"Hello, web!"