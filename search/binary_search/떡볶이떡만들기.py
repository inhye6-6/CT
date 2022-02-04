# 기준 : 적어도 m만큼 가져가는 절단기 높이의 최대값을 구하는 것이니까 절단기 높이를 크게 만들어야함
import sys
input = sys.stdin.readline

n , m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = 0
s = 0
e = arr[-1]

while s <= e :
    mid = (s+e) //2
    cut = 0 # 총 자른 떡의 길이
    
    for x in arr :
        diff = x-mid
        if  diff > 0 :
            cut += diff
        
        if cut > m :
            break
    
    if cut > m : # 절단기 높이를 작게 잡은 것
        s = mid + 1
    
    else :
        answer = mid
        e = mid - 1

print(answer)

    
