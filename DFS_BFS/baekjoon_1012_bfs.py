# 유기농 배추_bfs_ver

from collections import deque


# bfs 
def bfs(graph,n,m,i,j):
    queue=deque()
    queue.append((i,j))

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while queue :
        x, y = queue.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            # 배추 밭 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 노드 방문 처리
                queue.append((nx,ny))


def bfs_solution():
    T = int(input()) # test case
    for _ in range(T):
        m, n, k = map(int,input().split()) # n*m , k = 배추 개수

        # 그래프 만들기
        graph = [ [0 for _ in range(m)] for _ in range(n)] 
        for _ in range(k): 
            x, y = map(int,input().split())
            graph[y][x] = 1

        # 지렁이 배치
        result=0
        for y in range(n):
            for x in range(m):
                if graph[y][x] == 1:
                    graph[y][x] = 0 # 노드 방문 처리
                    bfs(graph,n,m,y,x)
                    result += 1
        
        print(result)

if __name__ == '__main__':
    bfs_solution()