import pdb
from my_python.Useful.u_sys.usefultools import get_screen_width
from collections import defaultdict

def splitdiff(diff):
    st1 = []
    st2 = []
    n = 0
    for dff in diff:
        #pdb.set_trace()
        if dff[0] == '?' and diff[n-1][0] == '-' or dff[0] in '- ':
            st1.append(dff)
            if n >= 1 and dff[0] == '-' and diff[n-1][0] == '-':
                st2.append('')
        if dff[0] == '?' and diff[n-1][0] == '+' or dff[0] in '+ ':
            st2.append(dff)
            if n >= 1 and dff[0] == '+' and diff[n-1][0] == '+':
                st1.append('')
        n += 1
    return st1,st2

def printdiff(st1,st2):
    Ln = 0
    middle = get_screen_width() // 2
    while st1 or st2:
        df1 = defaultdict(str)
        f1 = False
        #pdb.set_trace()
        while st1:
            if st1[0] and st1[0][0] == '-':
                if f1:
                    break
                else:
                    df1['-']=st1.pop(0)
                    f1 = True
                    Ln += 1
                    df1['ln'] = Ln
            elif st1[0] and st1[0][0] == '?':
                df1['?']=st1.pop(0).strip()
            else:
                if not st1[0] and df1:
                    break
                else:
                    if not st1[0]:
                        st1.pop(0)
                        break
                    st1.pop(0)
                    Ln += 1
        df2 = defaultdict(str)
        f2 = False
        #pdb.set_trace()
        while st2:
            if st2[0] and st2[0][0] == '+':
                if f2:
                    break
                else:
                    df2['+']=st2.pop(0)
                    f2 = True
            elif st2[0] and st2[0][0] == '?':
                df2['?']=st2.pop(0).strip()
            else:
                if not st2[0] and df2:
                    break
                else:
                    if not st2[0]:
                        st2.pop(0)
                        break
                    st2.pop(0)
                    
        #Onecmp = str(df1['ln']) + ': ' + df1['-'] + df2['+'] + '\n' + df1['?'] + df2['?']
        pre = str(Ln) + ': '
        print pre + df1['-'] + ' '*(middle - len(pre + df1['-'])) + df2['+']
        print ' '*len(pre) + df1['?'] + ' '*(middle - len(pre +df1['?'])) + df2['?']