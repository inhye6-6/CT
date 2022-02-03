import sys
input = sys.stdin.readline
from collections import deque

v,e = map(int,input().split())
graph = [[0]*e for _ in range(v)]
visited = [0]*v

for _ in range(v) :
    a, b ,c = map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[a-1].sort(key= lambda x :x[1])

queue=deque()
queue.append(graph[0][0])

def bfs():
    min_weight=0
    n = 0
    while queue: 
        j,w = queue.popleft()
        if n == v-1:
            return min_weight
        if visited[j] == 0:
            min_weight += w
            visited[j]=1
            queue.append(graph[j][0])

print(bfs())    