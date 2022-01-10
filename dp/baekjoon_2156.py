# 포도주 시식
# 30860KB, 80ms
################

## 1. i 번째 포도주를 마시는 경우 
#### 1) n-2번째 포도주를 마시고 n-1번째 포도주를 마시지 않는 경우 
#### --> d[i-2]+arr[i]
#### 2) n-2번째 포도주를 마시지 않고 n-1번째 포도주를 마시는 경우 
####    --> d[i-3]+arr[i-1]+arr[i]

## 2. i 번째 포도주를 마시지 않는 경우



import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
d = [0]*n

d[0] = arr[0]

if n > 1 :
    d[1] = arr[0]+arr[1]

if n > 2 :
    d[2] = max(d[0]+arr[2],arr[1]+arr[2],d[1])

for i in range(3,n) :
    d[i] = max(d[i-2]+arr[i],d[i-3]+arr[i-1]+arr[i],d[i-1])
    
print(d[n-1])    