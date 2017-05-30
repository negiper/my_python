import difflib

s1 = '''text1:
Thismodule provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
'''
s2 = '''text2:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5
'''

s1_lines = s1.splitlines()
s2_lines = s2.splitlines()
d = difflib.HtmlDiff()
print d.make_file(s1_lines, s2_lines)
