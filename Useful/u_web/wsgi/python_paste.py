import sys
import os
import webob
from webob import Request
from webob import Response

from paste.deploy import loadapp
from wsgiref.simple_server import make_server
from pprint import pprint


class AuthFilter(object):
    '''filter1:authentication'''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print 'This is Auth filter: filter1'
        return self.app(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print '#'*10,'filter1','#'*10
        print 'global_conf type:', type(global_conf)
        print '[DEFAULT]', global_conf
        print 'kwargs type:', type(kwargs)
        print 'Auth info:', kwargs
        return AuthFilter

class LogFilter(object):
    '''filter2:Logger'''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print 'This is Log filter: filter2'
        return self.app(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print '#'*10, 'filter2', '#'*10
        print '[DEFAULT]', global_conf
        print 'Log info', kwargs
        return LogFilter

class ShowInfo(object):
    '''App: ShowInfo'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, environ, start_response):
        print 'This is app: ShowInfo'
        start_response("200 OK", [("Content-Type", "text/plain")])
        content = []
        content.append("name:%s\nage:%s\n" % (self.name, self.age))
        content.append('*'*10 + 'WSGI INFO' + '*'*10 + '\n')
        for k,v in environ.iteritems():
            content.append('%s:%s\n' % (k,v))
        return [''.join(content)]

    @classmethod
    def factory(cls, global_conf, **kwargs):
        return ShowInfo(kwargs['name'], kwargs['age'])

class ShowVersion(object):
    '''App: ShowVersion'''
    def __init__(self, version):
        self.version = version

    def __call__(self, environ, start_response):
        print 'This is app: ShowVersion'
        req = Request(environ)
        res = Response()
        res.status = '200 OK'
        res.content_type = "text/plain"
        content = []
        content.append("%s\n" % self.version)
        content.append('*'*10 + 'WSGI INFO' + '*'*10)
        for k,v in environ.iteritems():
            content.append('%s:%s\n' % (k,v))
        res.body = '\n'.join(content)
        return res(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        return ShowVersion(kwargs['version'])

if __name__ == '__main__':
    config = 'python_paste.ini'
    appname = 'pasteAPP'
    wsgi_app = loadapp('config:%s' % os.path.abspath(config), appname)
    server = make_server('172.16.2.78', 7070, wsgi_app)
    #server.serve_forever()
    server.handle_request()

