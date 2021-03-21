#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def compute(a, r, c, m): 
    res = 0    
    # Iterate over the 2D conv mask
    for i, j in itertools.product( range(len(m)), range(len(m[0])) ):
        res += a[r+i][c+j] * m[i][j]
    return res 


def hourglassSum(arr):
    res = None
    
    # Hourglass Mask 
    m = [[1,1,1],[0,1,0],[1,1,1]]
    
    # Iterate over the input matrix with the conv 
    for r,c in itertools.product(range(len(arr)-len(m)+1), range(len(arr[0])-len(m[0])+1)):
        temp = compute(a=arr, r=r, c=c, m=m)
        # Track the max value 
        res = temp if res is None else (temp if temp > res else res)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



