import sys

# method that uses dynamic programming to
# find the maximum subsum of a set "vals"
# and the corresponding indicies
def findMaxSumDP(vals):

    # set that holds previously computed values
    B = [0 for i in range(len(vals) +1)]
    # set that sorts start indicies
    start = [0 for i in range(len(vals) +1)]
    stopval = 0

    for i in range(0,len(vals)+1):
        if (i == 0):
            B[i] = 0
        else:
            B[i] = max(B[i-1] + vals[i-1], 0)
            if (B[i] > B[stopval]):
                stopval = i
            if (B[i] == 0):
                start[i] = 0
            elif (B[i] != 0 and B[i-1] == 0):
                start[i] = i
            else:
                start[i] = start[i-1]

    return B[stopval], start[stopval], stopval
