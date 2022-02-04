
import collections

def solution(genres, plays):
    total_dic = collections.defaultdict(list)
    for i,(g,p) in enumerate(zip(genres,plays)):
        total_dic[g].append([i,p])
        total_dic[g].sort(key = lambda x: (-x[1],x[0]))

    total_plays=[]
    for g,lst in total_dic.items():
        total_plays.append([g,sum(lst[i][1] for i in range(len(lst)))])

    total_plays.sort(key = lambda x: -x[1])
    answer = []
    for genre,_ in total_plays :
        for x in total_dic[genre][:2]:
            answer.append(x[0])

    return answer
