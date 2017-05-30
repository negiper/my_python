#coding=utf-8
#calculate the value of expersion

import sys
import re
import pdb

OPER = '(+-*/'
CHR_NUM = '0123456789.'

def welcome_func():
    '''
    输出欢迎信息，读取算术表达式，并做简单处理
    '''
    welcome_str = 'Useful calculator!'
    print '-'*10, welcome_str, '-'*10
	
    while True:
        exp = raw_input('Input the expression:(enter q to exit) ').strip()
        if exp == 'q':
            sys.exit(0)
        elif len(exp) == 0:
            continue
        else:
            #对表达式进行规范化处理
            if not exp.startswith('(') or not exp.endswith(')'):
                exp = '(' + exp + ')'
            exp = re.sub('\s*', '',exp)
            
            #解析表达式中每一个独立元素，并将其放入一个列表中
            i = 0
            exp_list = []
            while i < len(exp):
                item = exp[i]
                j = i+1
                if item in CHR_NUM:
                    while j < len(exp) and exp[j] in CHR_NUM:
                        item += exp[j]
                        j += 1

                #special!! 处理负数
                elif item == '-' and exp[i-1] in OPER:
                    while j < len(exp) and exp[j] in CHR_NUM:
                        item += exp[j]
                        j += 1
                exp_list.append(item)
                i = j
            
            #将exp_list传给cal_exp函数进行求值计算
            #pdb.set_trace()
            print exp, '=', cal_exp(exp_list)
					
def cal_exp(s):
    '''
    利用栈的方式对表达式进行单元计算，每一个对小括号看作一个计算单元
    :param s: 表达式列表
    :return: 返回表达式的值
    '''
    Sd = []    #存放操作数的栈
    So = []    #存放操作符的栈
    L = len(s)
    
    for i in range(L):
        #计算最里层小括号中简单表达式的值并将其放入操作数栈Sd中
        if s[i] == ')':
            r = []
            r.insert(0, Sd.pop())
            t = So.pop()
            
            while t != '(':
                r.insert(0, t)
                r.insert(0, Sd.pop())
                t = So.pop()
            #计算简单表达式
            res = cal_simple(r)
            
            Sd.append(res)
        #将操作符放入So中
        elif s[i] in OPER:
            So.append(s[i])
        #将操作数放入Sd中
        else:
            Sd.append(s[i])
    return float(Sd[0])

def cal_simple(r):
    '''
    对简单表达式求值
    两层计算：先计算乘除后计算加减
    :param r: 简单表达式列表
    :return: 返回简单表示的值
    '''
    while '*' in r or '/' in r:
        R = r
        for k in range(len(r)-1):
            if r[k] in '*/':
                break
            else:
                continue

        R = [r[i] for i in range(len(r)) if i not in [k-1, k, k+1]]
        if r[k] == '*':
            R.insert(k-1, str(float(r[k-1]) * float(r[k+1])))
        if r[k] == '/':
            R.insert(k-1, str(float(r[k-1]) / float(r[k+1])))
        r = R

    while '+' in r or '-' in r:
        R = r
        for k in range(len(r)-1):
            if r[k] in '+-':
                break
            else:
                continue

        R = [r[i] for i in range(len(r)) if i not in [k-1, k, k+1]]
        if r[k] == '+':
            R.insert(k-1, str(float(r[k-1]) + float(r[k+1])))
        if r[k] == '-':
            R.insert(k-1, str(float(r[k-1]) - float(r[k+1])))
        r = R
    return str(r[0])

if __name__ == '__main__':
    welcome_func()
