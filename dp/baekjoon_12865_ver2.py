
# 33688kb, 3708ms
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
d = [0]*(k+1) 

for _ in range(n):
    w,v= map(int,input().split())
    for j in range(k,w-1,-1) :
        d[j] = max(d[j],d[j-w]+v)

print(d[k])