def solution(arrows):
    answer = 0
    x,y=100000, 100000
    visited = [[False] *200000 for _ in range(200000)]
    visited[x][y]=1
    
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]
    
    for i in arrows :
        nx=x+dx[i]
        ny=y+dy[i]
        if visited[nx][ny] == 1 :
            answer+=1
        else : visited[nx][ny] = 1 
        
    return answer