# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)

    n = 0
    while K > scoville[0] :
        if len(scoville)<=1:
            return -1
        n+=1
        heapq.heappush(scoville,heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        
    return n