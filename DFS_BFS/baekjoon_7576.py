# 토마토
# 105868KB,	2580ms

import sys 
from collections import deque
input = sys.stdin.readline

m, n = map(int,input().split())
storage=[]
visited = [[0]*m for _ in range(n)] 
queue = deque()
count = 0   # 안익은 토마토 수 count

for i in range(n) : 
    row=list(map(int,input().split()))
    storage.append(row)

    for j, tomato in enumerate(row):
        # 익은 토마토 좌표 queue에 담기
        if tomato == 1 :
            queue.append((i,j))
            continue
        # 안익은 토마토수 count
        if tomato == 0 :
            count += 1


def bfs():
    global count
    day = 0     # 지난 시간 count 
    
    # 상하좌우
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    while queue :
        x,y = queue.popleft()
        visited[x][y]= 1 

        #현재 위치에서 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 창고를 벗어난 경우 무시
            if nx<0 or nx >= n or ny <0 or ny>= m :
                continue

            # 해당 위치에 안익은 토마토가 있고 
            # 처음 방문하는 경우에만 시간 기록
            if visited[nx][ny] != 1 and storage[nx][ny] == 0 :
                queue.append((nx,ny))
                visited[nx][ny] = 1
                storage[nx][ny] = storage[x][y] + 1
                day = max(day,storage[nx][ny]-1)
                count -= 1
    return day

# 저장될 때부터 안익은 토마토가 없는 경우
if count == 0:
    print('0')

else :
    day = bfs()
    # bfs를 수행한 뒤에도 안익은 토마토가 존재할 경우
    if count > 0 : 
        print('-1')
    # 토마토가 다 익을 때까지 최소 날짜       
    else : print(day)