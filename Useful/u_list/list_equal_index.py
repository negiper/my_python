#******************************
#查找升序列表中值等于下标的元素
#采用的是二分查找法，找到值等于下标的边界
#*****************************

def binarySearch(lt):
    L = 0
    R = len(lt)

    while(L <= R):
        mid = L + (R-L)/2
        if (mid == 0 and lt[mid] == mid):
            return 0
        if (lt[mid]-mid < 0 and lt[mid+1]-(mid+1) == 0):
            return mid+1

        if lt[mid]-mid >= 0:
            R = mid-1
        else:
            L = mid+1
    return -1

def equal_items(lt):
    idx = binarySearch(lt)
    if idx != -1:
        while lt[idx] == idx:
            print idx,
            idx +=1
    else:
        print 'Not found!'

if __name__ == '__main__':
    lt = [-9,-8,-4,-2,4,5,9]
    #lt = [-3,-1,0,4,7]
    print lt,'中，值等于下标的元素为：'
    equal_items(lt)
