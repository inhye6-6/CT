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


def solution(n, computers):
    visited = [0]*n 
    count =0