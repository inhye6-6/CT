import collections
answer = []
graph = collections.defaultdict(list)

def dfs(depart):
    
    while graph[depart] :
        dfs(graph[depart].pop(0))
        
    if not graph[depart] :
        answer.append(depart)
        return
        

def solution(tickets):
    
    for a,b in tickets :
        graph[a].append(b)

    for a in graph.keys():
        graph[a].sort()
        
        
    dfs("ICN")
    answer.reverse()
    return answer