from collections import deque, Counter
def solution(n, edge):
    graph =  [[]*n for _ in range(n)]
    visited = [0]*n
    queue =  deque()
    for i,j in edge:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
        
    queue.append([0,0])
    visited[0]=1
    
    def bfs():
        depth = []
        while queue :
            i,l = queue.popleft()
            cnt = 0
            for x in graph[i]:
                if visited[x] == 1:
                    cnt+=1
                    continue
                queue.append((x,l+1))
                visited[x] = 1
                
            if cnt == len(graph[i]):
                depth.append(l)
                
        count = Counter(depth)
        return count[max(depth)]
       
        
    answer = bfs()
    return answer