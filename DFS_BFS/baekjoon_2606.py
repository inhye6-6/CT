import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
graph=[[0]*n for _ in range(n)]

def dfs(x,y) :
    if x<0 or x>=n-1 or y>0 or y>=n-1: 
       return False
    if graph[i][j]==1:
        graph[i][j]=0
        dfs(j,i)
        return True
    return False  
    
for _ in range(m) :
    x,y=map(int,input().split())
    graph[x-1][y-1]=1


count=1

for i in range(n):
    for j in range(n):
        if dfs(i,j):
            count+=1

print(count)
