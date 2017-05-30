import difflib

f1 = open('httpd2.2.3.conf', 'rb')
f2 = open('httpd2.2.15.conf', 'rb')
f1_lines = f1.read().splitlines()
f2_lines = f2.read().splitlines()
d = difflib.HtmlDiff()
print d.make_file(f1_lines, f2_lines)
