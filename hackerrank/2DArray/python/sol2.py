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

def filter_max(a,b):
    if a is None: return b
    else:
        return max(a,b)

def select_c(a,m,r,res=None):
    c=0
    while (c+len(m[0])-1) < len(a[0]):
        res = filter_max(res, compute(a,r,c,m))
        c += 1
    return res

def select_row(a, m, res=None):
    r=0
    while (r+len(m)-1) < len(a):
        res = filter_max(res, select_c(a,m,r,res))
        r += 1
    return res

# Complete the hourglassSum function below.
def hourglassSum(arr):
    m = [[1,1,1],[0,1,0],[1,1,1]]
    return select_row(arr,m)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



