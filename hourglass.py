#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def cal(arr):
    b = 0
    for i in arr:
        b =b+ sum(i)
    b = b - arr[1][0] - arr[1][2]
    return b
    

def hourglassSum(arr):
    final = []
    for j in range(0,4):
        for k in range(0,4):
            lst = []
            for i in range(0,3):
                lst.append(arr[i+k][0+j:3+j])
            value = cal(lst)
            final.append(value)

                

    return max(final)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
