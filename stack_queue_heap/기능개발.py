def solution(progresses, speeds):
    
    answer = []
    while progresses :
        count=0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

            
        for i in range(len(progresses)):
            if progresses[0] < 100 :
                break
            count+=1
            progresses.pop(0) 
            speeds.pop(0)
            
        if count != 0 :
                answer.append(count)     
            
    return answer