import sys
from tkinter import W
input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[]*e for _ in range(v)]
visited = [0]*v
min_weight=0
for _ in range(v) :
    a, b ,c = map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[a-1].sort(key= lambda x : x[1])


n=0
def dfs(i):
    global n
    global min_weight
    while True: 
        if n == v-1:
            return min_weight

        if graph[i] :    
            min_weight += graph[i][0][1]
            n+=1
            dfs(graph[i].pop(0)[0])

print(dfs(0))    



