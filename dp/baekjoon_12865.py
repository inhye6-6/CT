
# 28104KB, 7608ms
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
wt = []
vt=[]
for _ in range(n):
    w,v = map(int,input().split())
    wt.append(w)
    vt.append(v)

d = [[0]*(k+1) for _ in range(n+1)]



for i in range(1,n+1):
    for j in range(1,k+1) :
        if wt[i-1] <= j :
            d[i][j]= max(vt[i-1]+d[i-1][j-wt[i-1]],d[i-1][j])
        else :
            d[i][j] = d[i-1][j]

print(d[n][k])