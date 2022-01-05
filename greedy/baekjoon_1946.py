# 신입사원
# 57384KB,	3772ms

import sys

input = sys.stdin.readline

t=int(input())
for _ in range(t):
    
    n=int(input())
    total=[tuple(map(int,input().split())) for _ in range(n)]

    total=sorted(total)
    interview = total[0][1]
    count = 1
    
    for i in range(1,n):
        if total[i][1]< interview :
            count+=1
            interview = total[i][1]

    print(count)
