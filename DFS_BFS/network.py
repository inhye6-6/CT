def solution(n, computers):
    visited = [0]*n 
    count =0
    
    def dfs(i):
        visited[i] = 1
        nonlocal count
        
        for j,value in enumerate(computers[i]):
            if value == 1 and visited[j] == 0 :
                dfs(j)
                count+=1 
    
    for i in range(n):
        dfs(i)
            
    return n-count



from collections import deque
def solution(n, computers):
    visited = [0]*n 
    answer =0
    queue = deque()
    
    def bfs(x):
        #nonlocal queue
        
        while queue:
            x=queue.popleft()
            for y in range(n):
                if visited[y]==0 and computers[y][x]==1:
                    visited[y]=1
                    queue.append(y)
                    
    
    for i in range(n):
        if visited[i] == 0 :
            queue.append(i)
            bfs(i)
            answer+=1

    return answer