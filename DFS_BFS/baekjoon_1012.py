# 유기농 배추

def dfs(graph,n,m,x,y):
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph,n,m,x-1,y)
        dfs(graph,n,m,x,y-1)
        dfs(graph,n,m,x+1,y)
        dfs(graph,n,m,x,y+1)
        return True
    return False

def solution():
    T = int(input())
    for _ in range(T):
        n, m, k = map(int,input().split())
        graph = [ [0 for _ in range(m)] for _ in range(n)]
        for kk in range(k): 
            x, y = map(int,input().split())
            graph[x][y] = 1

        result=0
        for x in range(n):
            for y in range(m):
                if dfs(graph,n,m,x,y) :
                    result+=1
        
        print(result)

if __name__ == '__main__':
    solution()

                



        
        



        




    
