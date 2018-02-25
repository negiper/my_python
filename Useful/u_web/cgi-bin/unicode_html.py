#!/usr/bin/env python

CODE = 'UTF-8'
UNICODE_STR = u'''
Hello!
\u00A1Hola!
\u4F60\u597D!
\u3053\u3093\u306B\u3061\u306F!
'''

print 'Content-Type: text/html; charset=%s\r' % CODE
print '\r'
print '''
<html>
	<head>
		<title>Unicode CGI Demo</title>
	</head>
	
	<body>
	%s
	</body>
</html>
''' % (UNICODE_STR.encode(CODE))