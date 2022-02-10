"""
앞순위 이긴거 + 내가 이긴거
"""
from collections import defaultdict
def solution(n, results):
    count=0
    win_graph = defaultdict(set)    # key가 이긴 애들
    lose_graph = defaultdict(set)   # key를 이긴 애들
    
    for x,y in results:
        win_graph[x].add(y) 
        lose_graph[y].add(x) 
    
    for i in range(1,n+1):
        for loser in win_graph[i] : # i한테 진 애들
            lose_graph[loser].update(lose_graph[i]) # i를 이긴 애들에게도 지기 때문에 추가
        for winner in lose_graph[i]: # i를 이긴 애들
            win_graph[winner].update(win_graph[i]) # i한테 진 애들에게도 이기기 때문에 추가 
        
    for i in range(1,n+1):    
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            count+=1
    
    
    return count