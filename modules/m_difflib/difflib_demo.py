#coding=utf-8
#=================
#difflib 应用示例
#=================
import difflib
from collections import defaultdict
from my_python.Useful.u_sys.usefultools import get_screen_width
import pdb
__all__ = []
def normalize_line(t1,t2,width,len_pre):
    n_t1 = []
    n_t2 = []
    for i in range(len(t1)):
        line_t1 = list(t1[i])
        line_t2 = list(t2[i])
        
        while True:
            trun_line_t1 = []
            trun_line_t2 = []
            for l in range(width-len_pre):
                if line_t1:
                    trun_line_t1.append(line_t1.pop(0))
                if line_t2:
                    trun_line_t2.append(line_t2.pop(0))
            if trun_line_t1 or trun_line_t2:
                n_t1.append(''.join(trun_line_t1))
                n_t2.append(''.join(trun_line_t2))
            else:
                break
    return n_t1,n_t2

def splitdiff(diff):
    st1 = []
    st2 = []
    n = 0
    n1 = 0
    n2 = 0
    for dff in diff:
        #pdb.set_trace()
        if dff[0] in '- ':
            while n1 > n2:
                st2.append('')
                n2 += 1
            st1.append(dff)
            n1 += 1
        if dff[0] in '+ ':
            while n2 > n1:
                st1.append('')
                n1 += 1
            st2.append(dff)
            n2 += 1
        if dff[0] == '?':
            if diff[n-1][0] == '-':
                st1.append(dff)
            elif diff[n-1][0] == '+':
                st2.append(dff)
        n += 1
    return st1,st2

#简化版的HtmlDiff
def showdiff(diff):
    st1,st2 = splitdiff(list(diff))
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
                if not st1[0]:
                    if not df1:
                        st1.pop(0)
                    break
                else:
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
                if not st2[0]:
                    if not df2:
                        st2.pop(0)
                    break
                else:
                    st2.pop(0)
                        
        pre = str(df1['ln']) + ': '
        print pre + df1['-'] + ' '*(middle - len(pre + df1['-'])) + df2['+']
        if df1['?'] or df2['?']:
            print ' '*len(pre) + df1['?'] + ' '*(middle - len(pre +df1['?'])) + df2['?'] + '\n'
        else:
            print

__all__.append('showdiff')        