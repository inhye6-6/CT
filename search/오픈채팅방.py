
def solution(record):
    users={}
    actions = {"Enter":"님이 들어왔습니다.","Leave":"님이 나갔습니다."}
    records = []
    for alarm in record :
        if alarm.find('Leave') == -1:
            action, user, nickname =alarm.split()
            users[user]=nickname
        else : 
            action , user = alarm.split()
        
        records.append((action,user))
            
    answer = []       
    for act, uid in records :
        if act != 'Change':
            answer.append(users[uid]+ actions[act])
    
    return answer


def solution(record):
    users={}
    actions = {"Enter":"님이 들어왔습니다.","Leave":"님이 나갔습니다."}
    records = []
    for alarm in record :
        if alarm.find('Leave') == -1:
            action, user, nickname =alarm.split()
            users[user]=nickname
            
    answer = []       
    for alarm in record :
        if alarm.split()[0] != 'Change':
            answer.append(users[alarm.split()[1]]+ actions[alarm.split()[0]])
    
    return answer