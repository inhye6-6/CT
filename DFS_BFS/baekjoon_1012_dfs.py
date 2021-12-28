# 유기농 배추_dfs_ver


# 그래프 만들기
def graph(n,m,k):
        graph = [ [0 for _ in range(m)] for _ in range(n)] 
        for _ in range(k): 
            x, y = map(int,input().split())
            graph[y][x] = 1
        return graph

# dfs 
def dfs(i,j):
    if i < 0 or i >= n or j < 0 or j >= m :
        return False
    
    if graph[i][j] == 1:
        graph[i][j] = 0
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)
        return True
    return False


def dfs_solution():
    T = int(input()) # test case
    for _ in range(T):
        n, m, k = map(int,input().split()) # n*m , k = 배추 개수
        graph=graph(n,m,k)

        # 지렁이 배치
        result=0
        for y in range(n):
            for x in range(m):
                if dfs(y,x) :
                    result+=1
        
        print(result)

if __name__ == '__main__':
    dfs_solution()

                



        
        



        




    
