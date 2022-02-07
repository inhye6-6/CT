# 가운데 수 찾기
# 36872KB, 288ms
import sys
import heapq
input = sys.stdin.readline

n = int(input())
min_heap = []
max_heap=[]

for i in range(n) :
    k=int(input())
    if len(min_heap)==len(max_heap) :
        heapq.heappush(max_heap,-k)
    else : heapq.heappush(min_heap,k)

    if min_heap and min_heap[0] < -max_heap[0] :
        tmp_min = -heapq.heappop(max_heap)
        tmp_max = -heapq.heappop(min_heap)
        heapq.heappush(min_heap,tmp_min)
        heapq.heappush(max_heap,tmp_max)

    print(-max_heap[0])