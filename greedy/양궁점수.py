
#시뮬레이션 ver
from itertools import  combinations_with_replacement as comb
from copy import deepcopy

def cmp(a,b):
    return a[::-1]>b[::-1]

def solution(n, info):
    ret = [-1]*12
    for c in comb(range(11), n):
        arr=[0]*12
        score = 0
        for x in c : arr[x]+=1
        for i in range(11):
            if arr[i] > info[i]:
                score += 10-i
            elif info[i] != 0 :
                score -= 10-i
        if score <=0 : continue
        arr[11]=score
        if cmp(arr,ret):
            ret=deepcopy(arr)
    if ret[0] == -1 : return [-1]
    ret=ret[:-1]
    return ret

# greedy ver