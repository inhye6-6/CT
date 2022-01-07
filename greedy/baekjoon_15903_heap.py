# 카드 합체 놀이
# heap 사용
# 32932KB, 84ms

import sys
import heapq # priority queue

input = sys.stdin.readline

n, m = map(int,input().split())
cards = list(map(int,input().split()))

# heapify(): cards list를 min heap으로 변환
heapq.heapify(cards)

for _ in range(m) :
    combine = heapq.heappop(cards) + heapq.heappop(cards) # 작은 수 두개 pop 해서 더 함
    # 더한 값 heep에 다시 넣어주기
    heapq.heappush(cards,combine) 
    heapq.heappush(cards,combine)

print(sum(cards))
