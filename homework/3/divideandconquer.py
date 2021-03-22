import sys
		
# method that finds the max sum of the
# middle of the set as well as the
# corresponding indices
def crossMax(vals, start,stop,mid):
    cleft = 0
    cright = 0
    s = 0
    if (mid == start):
        left_s = vals[start]
        cleft = stop
    else:
        left_s = (-sys.maxint - 1)
    for i in range(mid,start - 1,-1):
        s = s + vals[i]
        if (s > left_s):
            cleft = i
            left_s = s
    
    s = 0
    if (mid+1 == stop):
        right_s = vals[stop]
        cright = stop
    else:
        right_s = (-sys.maxint - 1)
    for i in range(mid + 1,stop+1):
        s = s + vals[i]
        if (s > right_s):
            cright = i
            right_s = s
            
    return ((left_s + right_s), cleft,cright)
		
# method that uses divide and conquer to find
# the maximum subsum of a set "vals"
def findMaxSumDC(vals, start, stop):
    if (start == stop):
        return (vals[start], start,stop)
    mid = (start + stop) / 2
    left,lstart,lstop = findMaxSumDC(vals,start,mid)
    right,rstart,rstop = findMaxSumDC(vals,mid+1,stop)
    cross,cstart,cstop = crossMax(vals,start,stop,mid)
    if (left >= right and left >= cross):
        return (left,lstart,lstop)
    elif (right >= left and right >= cross):
        return (right,rstart,rstop)
    else:
        return (cross,cstart,cstop)
