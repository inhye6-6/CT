# 이분탐색 기준이 중요 : 여기선 n개의 돌을 징검다리에서 제거 했을 때 "최소거리" >> 즉 mid를 최소거리로 만들어야함
# sort한 뒤에 각각 distance에서 왔다갔다하면서 돌사이의 거리를 구하고 그게 mid보다 크면 제거


def solution(distance, rocks, n):
    rocks.sort()
    answer = 0 
    start = 0
    end = distance

    while start <= end :
        mid = (start+end) //2
        cnt = 0 
        pre_rock = 0

        for rock in rocks :
            diff = rock - pre_rock
            if diff < mid :
                cnt +=1
            else :
                pre_rock = rock
            
            if cnt > n :
                break
        
        if cnt > n : # 없애야할 바위가 더 많으므로 기준 값을 줄여야함
            end = mid -1
        
        else :
            answer = mid
            start = mid+1
   
   
    return answer