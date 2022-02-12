def solution(s):
    dic = {'zero':'0','one':'1','two':"2",'three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    num=[str(a) for a in range(10)]
    k=''
    answer = ''
    for i in s :
        
        if i in num :
            answer+=i
            continue
        k+=i
        try :
            answer+= dic[k]
            k=''
        except :
            pass
            
    answer = int(answer)
    return answer

    def solution(s):
        dic = {'zero':'0','one':'1','two':"2",'three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

        for k,v in dic.items():
            s=s.replace(k,v)
        s=int(s)
        return s