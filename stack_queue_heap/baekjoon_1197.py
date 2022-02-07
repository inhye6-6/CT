# prim
## 1. 임의의 정점을 선택
## 2. 해당 정점에서 갈수 있는 간선을 minheap에 넣는다.
## 3. 최소값을 뽑아 해당 정점을 방문안했다면 선택

# ver 2 
# 61988KB, 4744ms
import heapq

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
visited = [0]*(v+1)

heap=[[0,1]] # 정점은 1부터 시작
 
for _ in range(e) :
    a, b ,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

answer = 0
cnt =0

while heap :
    if cnt == v:
        break

    w, s = heapq.heappop(heap)
    if visited[s] == 0 :
        visited[s] = 1
        answer += w
        cnt += 1
        for i in graph[s]:
            heapq.heappush(heap,i)

print(answer)

#ver 3
#61832KB, 704ms

import sys
import heapq
input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[] for _ in range(v)]
visited = [0]*(v)

for _ in range(e) :
    a, b ,c = map(int,input().split())
    graph[a-1].append([c,(b-1)])
    graph[b-1].append([c,(a-1)])

min_weight=0
n=0 #간선 수
heap=[[0,0]]    

while heap :
    if n == v :
        break
    w, s =heapq.heappop(heap)
    if visited[s] == 0:
        visited[s] = 1 
        min_weight+=w
        n+=1
        for i in graph[s]:
            heapq.heappush(heap,i)
print(answer)
    