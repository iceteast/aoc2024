#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Author by Alex
from cfg import *

def distance(x, y):
    if len(x) != len(y):
        raise ValueError("different lengths: ", x, " vs ", y)
    x.sort()
    y.sort()
    ans = 0
    for i in range(len(x)):
        ans += abs(x[i] - y[i])
    return ans
def similarity(x, y):
    if (len(x) != len(y)):
        raise ValueError("different lengths: ", x, " vs ", y)
    ans = 0
    for i in x:
        for j in y:
            if i == j:
                ans += i
    return ans

if __name__ == "__main__":
    with open(getFILENAME()) as f:
        left = []
        right = []
        for line in f:
            a, b = line.strip().split()
            left.append(int(a))
            right.append(int(b))
        print(distance(left, right))
        print(similarity(left, right))
