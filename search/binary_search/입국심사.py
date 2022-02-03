'''
이분 탐색으로 답을 찾는 작업은 작업 시간들을 비교해서 최적의 스케쥴을 찾는것이 아닙니다.

작업과정을 간략하게 말하자면 아래와 같으니 참고해보세요

처음에 middle 값을 대충 정함
middle 시간안에 처리할 수 있는 총 사람수를 구함(done_num=sum(mid//time for time in times))
[해당시간에 처리할수 있는 사람수]와 [목표 사람수]를 비교함

* [처리할수 있는 사람수]가 [처리해야되는 사람수]보다 많으면 시간을 너무 여유있게 잡았음 -> 시간을 줄여봄

* [처리할수 있는 사람수]가 [처리해야되는 사람수]보다 적으면 시간을 너무 빡빡하게 잡았음 -> 시간을 늘려봄
[처리할수 있는 사람수]와 [처리해야되는 사람수]가 같으면

* 스케쥴은 모르겠지만 아무튼 시간은 구했다! 끝!
'''

def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    
    while left <= right :
        mid = (left + right) //2
        people = 0
        
        for t in times:
            people += mid // t
            
            if people >= n :
                break
        
        if people < n :
            left = mid+1
        
        else : 
            answer = mid
            right = mid-1
    
    return answer