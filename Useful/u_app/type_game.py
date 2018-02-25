#coding=utf-8

import sys
import time
import random
import msvcrt
from threading import Thread

if len(sys.argv[:]) < 2:
	print "Usage: python type_game.py NUM"
	print u"NUM: 游戏次数"
	sys.exit()

class MyThread(Thread):
	def __init__(self, func, args=()):
		super(MyThread, self).__init__()
		self.func = func
		self.args = args
		
	def run(self):
		self.result = self.func(*self.args)
		
	def get_result(self):
		try:
			return self.result
		except Exception:
			return None
		
T = int(sys.argv[1])
t = 0  
while True:
	t += 1
	letterNum=random.randint(5,20)  
	letters=[]  
	letterStr=""  
	for x in xrange(letterNum):  
		num=random.randint(65,122)  
		while num>=91 and num<=96:  #屏蔽非字母  
			num=random.randint(65,122)  
		letters.append(chr(num))  
	letterStr="".join(letters)    #列表转换为字符串  
	
	print u"请在20秒内输入",letterNum,u"位的字符串:",letterStr
	#print "Please input the characters",letterStr
	#user_input=raw_input("Input:")
	N = 0
	user_input = []
	t1 = time.clock()
	flag = False
	while True:
		thread = MyThread(msvcrt.getch)
		thread.start()
		
		ch = thread.get_result()
		while ch is None:
			ch = thread.get_result()
			t2 = time.clock()
			delta = t2-t1
			#print delta
			if delta >= 20:
				flag = True
				break
		else:
			if ch == '\x08':
				continue
			else:
				print ch,
				N += 1
				user_input.append(ch)
		if flag or N >= letterNum:
			break

	print
	user_input = ''.join(user_input)
	rightNum=0  
	for z in xrange(len(user_input)):  
		if user_input[z]==letterStr[z]:  
			rightNum+=1  
	if rightNum==letterNum:  
		print "completely correct"  
	else:  
		print "correct rate:%.2f%%"%((rightNum*1.0)/letterNum*100)
	
	print 
	if t >= T:
		print 'Game Over!'
		break