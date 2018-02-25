#!/usr/bin/env python

import cgi
from urllib import quote_plus
from string import capwords

header = 'Content-Type: text/html\n\n'
url = '/cgi-bin/friends3.py'

errhtml = '''
<html>
   <head>
      <title>Friends CGI Demo</title>
   </head>

   <body>
      <h3>ERROR</h3>
      <b>%s</b>
      <p><form><input type=button value=Back onclick="window.history.back()"></form>
   </body>
</html>'''

def showerror(err_str):
    print header + errhtml % (err_str)


formhtml = '''
<html>
   <head>
      <title>Friends CGI Demo</title>
   </head>

   <body>
      <h3>Friends list for: <i>%s</i></h3>
      <form action="%s">
      <b>Enter your name:</b>
         <input type=hidden name=action value=edit>
         <input type=text name=person value="%s" size=15>
      <p><b>How manay friends do you have?</b>
         %s
      <p><input type=submit>
      </form>
   </body>
</html>'''

fradio = '<input type=radio name=r2 value="%s" %s> %s\n'

def showform(who, fnum):
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checked=''
        if str(i) == fnum:
            checked='checked'
        friends = friends + fradio % (str(i), checked, str(i))
    print header + formhtml % (who, url, who, friends)

reshtml = '''
<html>
   <head>
      <title>Response Page</title>
   </head>

   <body>
      <h3>Friends list for: <i>%s</i></h3>
      Your name is: <b>%s</b>
      <p>You have <b>%s<b> friends.
      <p>Click<a href="%s">here</a> to edit your data again.
   </body>
<html>'''

def doRes(who, fnum):
    newurl = url + '?action=reedit&person=%s&r2=%s' % (quote_plus(who), fnum)
    print header + reshtml % (who, who, fnum, newurl)

def process():
    error = ''
    form  = cgi.FieldStorage()
    
    if form.has_key('person'):
        who  = capwords(form['person'].value)
    else:
        who = 'New User'

    if form.has_key('r2'):
        fnum = form['r2'].value
    else:
        if form.has_key('action') and form['action'].value == 'edit':
            error = 'Please select number of friends'
        else:
            fnum = 0


    if not error:
        if form.has_key('action') and form['action'].value != 'reedit':
            doRes(who, fnum)
        else:
            showform(who, fnum)
    else:
        showerror(error)

if __name__ == '__main__':
    process()
