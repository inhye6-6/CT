from heapq import heappush, heappop
def solution(jobs):
    jobs.sort(key=lambda x :(x[0],x[1]))
    start = -1 # job 시작 시점
    answer, end, i = 0,0,0 #답, job 끝날 시점(다음 job이 시작될 시점), 처리하는 수 확인
    heap = []
    
    while i < len(jobs) :
        # 현재 시점에서 들어갈 수 있는 job
        for j in range(len(jobs)):
            if start < jobs[j][0] <= end :
                heappush(heap,[jobs[j][1],jobs[j][0]]) # 현재 들어갈 수 있는 job 넣기
        if heap:
            current = heappop(heap)
            start = end
            end += current[0]
            answer += end-current[1]
            i+=1 # job을 하나 수행함
        else : 
            end += 1  # 다음 job이 아직 도착하지 않았을 때 +1
                
    
    return answer//len(jobs)