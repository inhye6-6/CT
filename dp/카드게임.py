#baekjoon 11062
# 근우-> 왼쪽을 선택한거랑, 오른쪽을 선택한거 중에 max , 명우 -> min
import sys


def pickCard(turn,left,right) :
    if left > right :
        return 0
    if dp[left][right] : 
        return dp[left][right]
    
    if turn :
        score = max(pickCard(False,left+1,right)+cards[left],pickCard(False,left,right-1)+cards[right])
        dp[left][right] = score
        return score
    else :
        score = min(pickCard(True,left+1,right),pickCard(True,left,right-1))
        dp[left][right] = socre
        return score    


T = int(input())
for _ in range(T) :
    N = int(input())
    cards = list(map(int,sys.stdin.readline().split()))
    dp = [[0]*N for _ in range(N)]
    pickCard(True,0,N-1)
    
    print(dp[0][N-1])
    
    