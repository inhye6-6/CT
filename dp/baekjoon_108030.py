# 행렬 제곱
import sys

input = sys.stdin.readline


def mul(a,b):
    n = len(a)
    c = [[0]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]
    
    for i in range(n) :
        for j in range(n):
            c[i][j] %= 1000
    
    return c
    
