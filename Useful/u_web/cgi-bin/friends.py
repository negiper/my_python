#!/usr/bin/env python

import cgi

header = 'Content-Type: text/html\n\n'

formhtml = '''
<html>
   <head>
      <title>Friends CGI Demo</title>
   </head>

   <body>
      <h3>Friends list for: <i>New User</i></h3>
      <form action="/cgi-bin/friends.py">
      <b>Enter your name:</b>
         <input type=hidden name=action value=edit>
         <input type=text name=person value="new user" size=15>
      <p><b>How manay friends do you have?</b>
         %s
      <p><input type=submit>
      </form>
   </body>
</html>'''

fradio = '<input type=radio name=r1 value="%s" %s> %s\n'

def showform():
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checked=''
        if i == 0:
            checked='checked'
        friends = friends + fradio % (str(i), checked, str(i))
    print header + formhtml % (friends)


reshtml = '''
<html>
   <head>
      <title>Response Page</title>
   </head>

   <body>
      <h3>Friends list for: <i>%s</i></h3>
      Your name is: <b>%s</b>
      <p>You have <b>%s<b> friends.
   </body>
<html>'''

def doRes(who, fnum):
    print header + reshtml % (who, who, fnum)


def process():
    form = cgi.FieldStorage()
    if form.has_key('person'):
        who = form['person'].value
    else:
        who = 'New User'
    if form.has_key('r1'):
        fnum = form['r1'].value
    else:
        fnum = 0
    if form.has_key('action'):
        doRes(who, fnum)
    else:
        showform()

if __name__ == '__main__':
    process()