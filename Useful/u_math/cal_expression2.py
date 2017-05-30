#coding=utf-8

import sys
import re
import pdb

def welcome_func():
	'''
	输入判断
	'''
	welcome_str = 'Super calculator!'
	print '-'*10, welcome_str, '-'*10
	while True:
		iput = raw_input('Input your expression:(q to exit.) ')
		if iput == 'q':
			sys.exit(0)
		elif len(iput) == 0:
			continue
		else:
			iput = re.sub('\s*', '', iput)
			return iput

def mul_div(exp):
	'''
	乘除运算
	'''
	data = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', exp)
	if not data:
		return exp

	data = data.group()
	if len(data.split('*')) > 1:
		d1 , d2 = data.split('*')
		value = float(d1) * float(d2)
	else:
		d1 , d2 = data.split('/')
		if float(d2) == 0.0:
			sys.exit('Dividend is zero!')
		value = float(d1) / float(d2)

	s1 , s2 = exp.split(data)
	new_exp = '%s%s%s' % (s1, value, s2)
	return mul_div(new_exp)

def add_sub(exp):
	'''
	加减运算
	'''
	exp = exp.replace('+-', '-')
	exp = exp.replace('--', '+')
	exp = exp.replace('-+', '-')
	exp = exp.replace('++', '+')

	data = re.search('[\+\-]?\d+\.*\d*[\+\-]{1}\d+\.*\d*', exp)
	if not data:
		return exp

	data = data.group()
	if len(data.split('+')) > 1:
		d1, d2 = data.split('+')
		value = float(d1) + float(d2)
	elif data.startswith('-'):
		d1, d2, d3 = data.split('-')
		value = -float(d2) - float(d3)
	else:
		d1, d2 = data.split('-')
		value = float(d1) - float(d2)

	s1, s2 = exp.split(data)
	new_exp = '%s%s%s' % (s1, value, s2)
	return add_sub(new_exp)

def del_bracket(exp):
	'''
	小括号去除运算
	'''
	#pdb.set_trace()
	if not re.search(r'\(([^()]+)\)', exp):
		ret1 = mul_div(exp)
		ret2 = add_sub(ret1)
		return ret2

	data = re.search(r'\(([^()]+)\)', exp).group()
	simple = data.strip('[\(\)]')
	ret1 = mul_div(simple)
	ret2 = add_sub(ret1)
	s1, s2 = exp.split(data)
	new_exp = '%s%s%s' % (s1, ret2, s2)
	return del_bracket(new_exp)

if __name__ == '__main__':
	expression = welcome_func()

	ret = del_bracket(expression)
	print expression, '=', ret
