# minheap maxheap해서 빼고 set으로 교집합 찾기

from heapq import heappop,heappush
def solution(operations):
    answer = []
    minheap=[]
    maxheap=[]
    heap = []
    for operation in operations :
        op, num = operation.split()
        
        if op == "I":
            heappush(minheap,int(num))
            heappush(maxheap,-int(num))

        else :
            if not heap :
                continue
            if num == '1' :
                if -(heappop(maxheap)) not in heap :
                    heappop(maxheap)
            else :
                if heappop(minheap) not in heap :
                    heappop(minheap)
        
        heap = set(minheap)&set(map(lambda x:-x,maxheap))         
                
    if heap :
        return [max(heap),min(heap)]
    else : 
        return [0,0]