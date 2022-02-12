from collections import defaultdict
from math import ceil

def solution(fees, records):
    answer = []
    access = defaultdict(list)
    
    for record in records:
        time,num,cat= record.split()
        h,m = map(int,time.split(':'))
        access[num].append([h,m,cat])
    
    for k,v in access.items():
        if v[-1][2] == 'IN':
            access[k].append([23,59,'OUT'])
    
          
    for k,v in access.items():
        time = 0 
        for i in range(0,len(v),2):
            time += (v[i+1][0]-v[i][0])*60+ (v[i+1][1]-v[i][1])
        
        if time - fees[0] <= 0 : 
            answer.append([int(k),fees[1]])
        else :
            answer.append([int(k),fees[1]+ ceil((time - fees[0])/fees[2])* fees[3]])
            
    return [x[1] for x in sorted(answer)]