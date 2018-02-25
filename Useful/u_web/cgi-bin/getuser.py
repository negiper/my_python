#!/usr/bin/env python

import cgi

res = '''Content-Type: text/html\n
<html>
<head>
<title>Response Page</title>
</head>

<body>
<h3>Friends list for: <i>%s</i></h3>
Your name is: <b>%s</b>

<p>You have <b>%s</b> friends.
</body>
</html>'''

form = cgi.FieldStorage()
who = form['person'].value
fnum = form['g1'].value
print res % (who, who, fnum) 