# 바이러스
# 30860KB, 68ms
	
import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
graph=[[]*n for _ in range(n)]
visited=[0]*n

for _ in range(m) :
    x,y=map(int,input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)
    
count=0

def dfs(i):
    global count
    visited[i]=1
    for node in graph[i] :
        if visited[node]== 0:
            dfs(node)
            count+=1
    
dfs(0)    
print(count)