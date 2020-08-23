#!/bin/python3

import math
import os
import random
import re
import sys


def compute(a, r, c, m): 
    s = len(m)
    res = 0
    for i in range(s):
        for j in range(s):
            res += a[r+i][c+j] * m[i][j]
    return res 


def hourglassSum(arr):
    res = None
    m = [[1,1,1],[0,1,0],[1,1,1]]
    for r in range(len(arr)-len(m)+1):
        for c in range(len(arr[0])-len(m[0])+1):
            temp = compute(a=arr, r=r, c=c, m=m)
            if res is None: res = temp
            else:
                if temp > res: res=temp
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



