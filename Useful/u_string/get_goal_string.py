#coding=utf-8
# 过滤所给字符串得到目标字符串
# 2016年 02月 17日 星期三 16:39:15 CST

origin = raw_input('Enter the raw string: ')
target = raw_input('Enter the target string: ')
midRes = origin

#用于记录每个字符出现的位置
IndexList = []

#c2和c1表示当前正在匹配的字符和前一个字符
c1 = ''
c2 = target[0]
tlen = len(target)
for item in range(0,tlen):
    print c1,'\t',c2,'\t',midRes
    slen = len(midRes)
    if c1 == '':
        for ind in range(0,slen):
            if midRes[ind] == c2:
                break
        midRes = midRes[ind:]
        IndexList.append(ind)
        print ind
        print midRes
    else:
        ind1 = midRes.find(c1)
        for ind2 in range(ind1+1,slen):
            if midRes[ind2] == c2:
                break
        print ind1,ind2
        IndexList.append(ind2)
        midRes = midRes[0:ind1+1] + midRes[ind2:]
        if ind1+1 == (tlen-1):
            midRes = midRes[0:ind1+2]
        print midRes
    c1 = c2
    if item+1 < tlen:
        c2 = target[item+1]

print IndexList
Indexs = [IndexList[0]]
for i in range(1,len(IndexList)):
    Indexs.append(IndexList[i] + IndexList[i-1])

print '原字符串:',origin,'最终字符串:',midRes
print '出现在原字符串的如下位置：',Indexs
