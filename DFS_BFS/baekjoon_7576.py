# 토마토

import sys 
from collections import deque
from tkinter import W
input = sys.stdin.readline

m, n = map(int,input().split())
storage=[]
queue = deque()

for i in range(n) : 
    row=list(map(int,input().split()))
    storage.append(row)

    # 익은 토마토 queue에 담기
    for j, tomato in enumerate(row):
        if tomato == 1 :
            queue.append((i,j))

visited = [[0]*m for _ in range(n)]
count = 1


def bfs():
    global count
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    while queue :
        x,y = queue.popleft()
        visited[x][y]= 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx >= m or ny <0 or ny>= n :
                continue
            
            # 토마토가 없을 때 무시
            if storage[nx][ny] == -1 :
                continue

            if visited[nx][ny] != 1 and storage[nx][ny] == 0 :
                queue.append((nx,ny))
                visited[nx][ny] = 1
                storage[nx][ny] += 1
                count = max(count,storage[nx][ny])

if all(storage):
    print('0')

bfs()

if not all(storage) : 
        print('-1')
                
print(count)



