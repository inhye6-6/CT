# DFS
_* DFS 설명 추가하기!!!!!!!!!!!!_<br>

___
## 1. 바이러스 (baekjoon 2606) 
*푼 날짜 : 2022.01.12*

<br/>

### 문제
** *생략*
</br>
### 풀이
(30860KB, 68ms)

진짜 간단한 DFS 문제~~!~! <br>

1. 연결된 컴퓨터들을 adj 리스트로 받음<br>
2. 한 컴퓨터와 연결된 컴퓨터들이 이전에 방문하지 않은 컴퓨터라면 방문하고 count를 높여줌<br>
<br>
<br>

___
# BFS
_* BFS 설명 추가하기_<br>

탐색시 BFS의 기본 def
```
from collections import deque

def bfs(x,y):
    queue = deque() 
    deque.append((x,y))

    # 노드 방문 처리
    visitied[x][y] = 1

    # 이동 범위가 상하 좌우 일때
    # 다른 조건이면 변경
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]

    while queue :
        # queue에서 pop함
        x,y = queue.popleft()
        
        # loop 돌면서 상하좌우 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 공간을 넘어가면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
            continue

            # 해당 좌표값에 방문하지 않았을 때 queue에 추가, visited 바꿔주기
            if visited[nx][ny] == 0 :
                queue.append((nx,ny))
                visited[nx][ny] = 1 
```
___
## 1. 토마토 (baekjoon 7576) 
*푼 날짜 : 2022.01.19*

<br/>

### 문제

익은 토마토와 안익은 토마토들이 창고에 보관이 됨.<br> 하루가 지나면 ***익은 토마토들의 상하좌우*** **에 있는 안익은 토마토들이 익음**.<br> 
**토마토가 혼자 저절로 익는 경우는 없음** .<br> 
창고에 보관된 **모든 토마토들이 익게 되는 최소 일수** 출력<br>
* 출력 <br>
    a) 토마토가 모두 익을 때까지의 최소 날짜 출력<br>
    b) 저장될 때부터 모든 토마토가 익어있는 상태이면 0 출력<br>
    c) 토마토가 모두 익지는 못하는 상황이면 -1을 출력
</br><br>



### 풀이

익은 토마토의 개수가 여러개라 시작점이 많아 가지고 dfs는 대박 오래 걸릴 거 같아서 bfs 사용!<br>
+) bfs는 최단거리 보장 <br><br>

(105868KB, 2580ms)
1. 처음 익은 토마토가 여러개이기 때문에 모든 익은 토마토를 queue에 넣어 놓고 시작해야함 

2. 처음에 안익은 토마토가 없을 때, BFS를 끝내도 안익은 토마토가 존재할 때
인 경우 출력을 위해 안익은 토마토를 count 해야함 <br>
count가 0 이면 '0' 출력

3. bfs를 돌림<br>
- 이때 loop안에서 팝하고 난 뒤에 visited를 갱신해주어야함 (시작점 여러개)<br>
- loop로 상하좌우를 확인해가면서 그 위치에 안익은 토마토가 있고 visited가 1인 경우 <br><br>
(1)
``` storage[nx][ny] = storage[x][y] + 1``` 로 storage의 일자를 갱신시켜주기 <br>
(2) 
```day = max(day,storage[nx][ny]-1)```를 통해 storage가 가지고 있는 일자 중 최대 저장 <br>
(3) visited, count 변경해주기 <br>

4. count가 0보다 크면 '-1' 출력, 아니면 일수(day) 출력
