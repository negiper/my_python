#coding=utf-8
# <type 'str'> find方法的实现

# ============================
# 找到字串第一次出现的位置
# ============================
def dfind(string,sub,start,end):
    I = start
    J = 0
    L1 = end
    L2 = len(sub)-1

    while I <= L1 and J <= L2:
        if string[I] == sub[J]:
            I += 1
            J += 1
#            dfind(string,sub[J:],I,L1)
        else:
            I += 1
            J = 0
#            dfind(string,sub,I,L1)
    if J > L2:
        return I-len(sub)
    else:
        return -1

# ================================
# 找到子串出现的所有位置
# 如存在则：返回由逗号分割的下标字符串
# 否则：返回空字符串
# （该函数可用在if语句中）
# ================================
def multiFind(string,sub,start,end):
    I = start
    J = 0
    L1 = end
    L2 = len(sub)-1
    Indexs = ''

    while I <= L1:
        if string[I] == sub[J]:
            I += 1
            J += 1
        else:
            I += 1
            J = 0

        if J > L2:
            Indexs = Indexs + ','+ str(I-len(sub))
            J = 0

    return Indexs[1:]

s1,s2 = raw_input('Input origin string and substring: ').split(',')
# print dfind(s1,s2,0,len(s1)-1)
result = multiFind(s1,s2,0,len(s1)-1)
if result:
    print '找到子串,出现的位置：',result
else:
    print '未找到子串'

