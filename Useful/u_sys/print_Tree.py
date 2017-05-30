#coding=utf-8
#字符输出一棵树

import math,pdb

def printT(L):
    size = len(L)
    H = int(math.log(size,2))*2+1
    L1 = 2*H

    I = 0
    level = 0
    Num = int(math.pow(2,level))
    NN = L[I:I+Num]
    SN = [L1]
    theNode = 0

    while Num <= size:
        #pdb.set_trace()
        SB,theNode = printN(NN,SN,theNode,size)
        SN = printB(SB,level,H)

        level += 1
        I += Num
        Num = int(math.pow(2,level))
        if I+Num > size:
            NN = L[I:]
        else:
            NN = L[I:I+Num]

def printN(NN,SN,theNode,size):
    SB = []
    lineStr = ''
    for i in range(len(NN)):
        if i == 0:
            lineStr += ' '*SN[i]+str(NN[i])
        else:
            lineStr += ' '*(SN[i]-SN[i-1]-1)+str(NN[i])
        theNode += 1
        if theNode < size//2 or theNode*2+1 == size:
            SB.append(SN[i]-1)
            SB.append(SN[i]+1)
        elif theNode*2 == size:
            SB.append(SN[i]-1)
        else:
            continue
    print lineStr
    return SB,theNode

def printB(SB,level,H):
    SN = []
    if level == 0:
        sb = SB[0]
        for i in range(H):
            print ' '*sb + '/' + ' '*2*(i+1) + '\\'
            sb -= 1
        SN.append(SB[0]-H)
        SN.append(SB[1]+H+1)
    else:
        lineStr1 = ''
        for i in range(len(SB)):
            if i % 2 == 0:
                if i == 0:
                    lineStr1 += ' '*SB[i]+'/'
                else:
                    lineStr1 += ' '*(SB[i]-SB[i-1]-1)+'/'
            else:
                lineStr1 += ' '*(SB[i]-SB[i-1]-1)+'\\'
        print lineStr1
        lineStr2 = ''
        for i in range(len(SB)):
            if i % 2 == 0:
                if i == 0:
                    lineStr2 += ' '*(SB[i]-1)+'/'
                else:
                    lineStr2 += ' '*(SB[i]-SB[i-1]-3)+'/'
                SN.append(SB[i]-2)
            else:
                lineStr2 += ' '*(SB[i]-SB[i-1]+1)+'\\'
                SN.append(SB[i]+2)
        print lineStr2
    return SN


#*************
#待改进：1）根据树的高度有效计算树根空格数
#       2）改进打印每一层节点和分支的接口
