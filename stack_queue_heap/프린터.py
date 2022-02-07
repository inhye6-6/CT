# 중요도 클수록 중요 -> max heap
import heapq

def solution(priorities, location):
    heap=[[priorities[i],i] for i in range(len(priorities))]
    
    answer = 0
    while heap :
        x=heap[0]        
        if x[0] < max(map(lambda x :x[0],heap)):
            heap.append(x)
            heap.pop(0)
        else :
            a=heap.pop(0)
            answer+=1
            if a[1] == location:
                return answer