# 토마토

import sys 
from collections import deque
from tkinter import W
input = sys.stdin.readline

m, n = map(int,input().split())
storage=[]
queue = deque()
count = 0

for i in range(n) : 
    row=list(map(int,input().split()))
    storage.append(row)

    # 익은 토마토 queue에 담기
    for j, tomato in enumerate(row):
        if tomato == 1 :
            queue.append((i,j))
            continue
        if tomato == 0 :
            count += 1

visited = [[0]*m for _ in range(n)]


def bfs():
    global count
    day = 0
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    while queue :
        x,y = queue.popleft()

        visited[x][y]= 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx >= n or ny <0 or ny>= m :
                continue

            if visited[nx][ny] != 1 and storage[nx][ny] == 0 :
                queue.append((nx,ny))
                visited[nx][ny] = 1
                storage[nx][ny] = storage[x][y] + 1
                day = max(day,storage[nx][ny])
                count -= 1
    
    return day


if count == 0:
    print('0')
else :
    day = bfs()
    if count > 0 : 
        print('-1')
                
    else : print(day)
