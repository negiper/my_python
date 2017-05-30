#coding=utf-8

year = int(raw_input('year: '))
month = int(raw_input('month: '))
day = int(raw_input('day: '))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

if 0 < month <=12:
    sum = months[month-1]
else:
    print 'data error!'

sum += day
leap = 0
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    leap = 1
if leap and month > 2:
    sum += 1

print "It's the %dth day." % sum
