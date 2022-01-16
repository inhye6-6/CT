import sys
import heapq
input = sys.stdin.readline

n = int(input())
min_heap = []
max_heap=[]

for i in range(n) :
    k=int(input())
    if len(min_heap)==len(max_heap) :
        heapq.heappush(max_heap,(-k,k))
    else : heapq.heappush(min_heap,(k,k))

    if min_heap and min_heap[0][1] < max_heap[0][1] :
        tmp_min = heapq.heappop(max_heap)[1]
        tmp_max = heapq.heappop(min_heap)[1]
        heapq.heappush(min_heap,(tmp_min,tmp_min))
        heapq.heappush(max_heap,(-tmp_max,tmp_max))

    print(max_heap[0][1])