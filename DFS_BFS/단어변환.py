# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0]*len(words)
    
    if target not in words :
        return answer
    
    queue = deque()
    
    def bfs():
        count=0
        queue.append((begin,count))
        
        while queue:
            cur, count = queue.popleft()
            if cur == target :
                return count
            for i in range(len(words)):
                if visited[i] == 1:
                    continue
                cnt = 0
                for a,b in zip(cur,words[i]):
                    if a != b :
                        cnt +=1
                if cnt == 1 :
                    queue.append((words[i],count+1))
    
    return bfs()