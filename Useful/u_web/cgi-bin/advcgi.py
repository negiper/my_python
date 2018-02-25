#!/usr/bin/env python

from cgi import FieldStorage
from os import environ
from cStringIO import StringIO
from urllib import quote, unquote
from string import capwords, strip, split, join

class AdvCGI(object):
	header = 'Content-Type: text/html\n\n'
	url = 'cgi-bin/advcgi.py'
	langset = ('Python', 'Perl', 'Java', 'C++', 'Php', 'C', 'JavaScript')
	langItem = '<input type=checkbox name=lang value="%s" %s> %s\n'
	
	formhtml = '''
	<html>
		<head>
			<title>Advanced CGI Demo</title>
		</head>
		
		<body>
			<h2>Advanced CGI Demo Form</h2>
			<form method=post action="%s" enctype="multipart/form-data">
				<h3>My Cookie Setting</h3>
				<li><code><b>CPPuser = %s</b></code>
				<h3>Enter cookie value</h3><br>
				<input name=cookie value="%s"> (<i>optional</i>)
				<h3>Enter your name</h3><br>
				<input name=person value="%s"> (<i>required</i>)
				<h3>What language can you program in? (<i>at least one required</i>)</h3>
				%s
				<h3>Enter file to upload</h3>
				<input type=file name=upfile value="%s" size=45>
				<p><input type=submit>
			</form>
		</body>
	</html>
	'''
	errhtml = '''
	<html>
		<head>
			<title>Advanced CGI Demo</title>
		</head>
		
		<body>
			<h3>ERROR</h3>
			<b>%s</b>
			<p><form><input type=button value=back onclick="window.history.back()"></form>
		</body>
	</html>
	'''
	reshtml = '''
	<html>
		<head>
			<title>Advanced CGI Demo</title>
		</head>
		
		<body>
			<h2>Your Uploaded Data</h2>
			<h3>Your cookie value is: <b>%s</b></h3>
			<h3>Your name is: <b>%s</b></h3>
			<h3>You can program in the following languages: </h3>
			<ul>%s</ul>
			<h3>Your uploaded file...</h3><br>
			<h3>Name: <i>%s</i><br>
			<h3>Contents: </h3><br>
			<pre>%s</pre>
			Click<a href="%s"> <b>here</b> </a> to return form.
		</body>
	</html>
	'''
	
	def get_CPPCookie(self):
		if environ.has_key('HTTP_COOKIE'):
			for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
				if len(cookie) > 6 and cookie[:3] == 'CPP':
					tag = cookie[3:7]
					try:
						self.cookies[tag] = eval(unquote(cookie[8:]))
					except (NameError, SyntaxError):
						self.cookies[tag] = unquote(cookie[8:])
		else:
			self.cookies['info'] = self.cookies['user'] = ''
		
		if self.cookies['info'] != '':
			self.who, langStr, self.fn = split(self.cookie['info'], ':')
			self.langs = split(langStr, ',')
		else:
			self.who = self.fn = ''
			self.langs = ['python']
			
	def show_form(self):
		self.get_CPPCookie()
		langStr = ''
		for lang in AdvCGI.langset:
			if lang in self.langs:
				langStr += AdvCGI.langItem % (lang, 'checked', lang)
			else:
				langStr += AdvCGI.langItem % (lang, '', lang)
				
		if not self.cookies.has_key('user') or self.cookies['user'] == '':
			cookStatus = '<i>(cookie has not been set yet)</i>'
			userCook = ''
		else:
			userCook = cookStatus = self.cookies['user']
			
		print AdvCGI.beader + AdvCGI.formhtml % (AdvCGI.url, cookStatus, userCook, self.who, langStr, self.fn)
		
	def show_err(self):
		print AdvCGI.header + AdvCGI.errhtml % (self.error)
		
	def set_CPPCookies(self):
		for cookie in self.cookies.keys():
			print 'Set-Cookie: CPP%s=%s; path=/' % (cookie, quote(self.cookies[cookie]))
	
	def show_resultes(self):
		MAXBYTES = 1024
		langlist = ''
		for lang in self.langs:
			langlist = langlist + '<li>%s<br>' % lang
		
		filedata = ''
		while len(filedata) < MAXBYTES:
			data = self.fp.readline()
			if data == '':
				break
			filedata += data
		else:
			filedata += '...<B><i>(file truncated duo to size)</i></b>'
		self.fp.close()
		if filedata == '':
			filedata = '<b><i>(file upload error or file not given)</i></b>'
		
		filename = self.fn
		if not self.cookies.has_key('user') or self.cookies['user'] == '':
			cookStatus = '<i>(cookie has not been set yet)</i>'
			userCook = ''
		else:
			userCook = cookStatus = self.cookies['user']
		self.cookies['info'] = join([self.who, join(self.langs, ','), filename], ':')
		self.set_CPPCookies()
		print AdvCGI.header + AdvCGI.reshtml % (cookStatus, self.who, langlist, filename, filedata, AdvCGI.url)
	
	def go(self):
		self.cookies = {}
		self.error = ''
		form = FieldStorage()
		if form.keys() == []:
			self.show_form()
			return
		if form.has_key('person'):
			self.who = capwords(strip(form['person'].value))
			if self.who == '':
				self.error = 'Your name is required. (blank)'
		else:
			self.error = 'Your name is required. (missing)'
			
		if form.has_key('cookie'):
			self.cookies['user'] = unquote(strip(form['cookie'].value))
		else:
			self.cookies['user'] = ''
			
		self.langs = []
		if form.has_key('lang'):
			langdata = form['lang']
			if type(langdata) == type([]):
				for lang in langdata:
					self.langs.append(lang.value)
			else:
				self.langs.append(langdata.value)
		else:
			self.error = 'At least one language required.'
		
		if form.has_key('upfile'):
			upfile = form['upfile']
			self.fn = upfile.filename or ''
			if upfile.file:
				self.fp = upfile.file
			else:
				self.fp = StringIO('(no data)')
		else:
			self.fp = StringIO('(no file)')
			self.fn = ''
		if not sellf.error:
			self.show_resultes()
		else:
			self.show_err()
			
if __name__ == '__main__':
	page = AdvCGI()
	page.go()