#coding=utf-8
#牛顿法求解数的平方根
#Newton's method to calculate square root

import math

# get three inputs from the user
num_str = raw_input("Find the square root of integer: ")
while not num_str.isdigit():
	print 'Input Error!'
	num_str = raw_input('Find the square root of integer: ')
number_int  = int(num_str)

guess_str = raw_input('Initial guess: ')
while not guess_str.isdigit():
	print('Input Error!')
	guess_str = raw_input('Initial guess: ')
guess_float = float(guess_str)

originalGuess = guess_float
count_int = 0

tolerance_float = float(raw_input('What tolerance: '))

# do the algorithm steps as described above

previous_float = 0.0
count_int = 0
while math.fabs(previous_float - guess_float) > tolerance_float:
	previous_float = guess_float
	quotient = number_int/guess_float
	guess_float = (quotient + guess_float)/2
	count_int = count_int +1

# output the three original values, the num_int of iterations and the square root

print 'Square root of ',number_int,' is: ',guess_float
print 'Took',count_int,' steps to get it to tolerance: ',tolerance_float
print 'Starting from a guess of: ',originalGuess

