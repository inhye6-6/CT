# 에라토스테네스의 체
# itertools permutations, combinations, product

import math
from itertools import permutations

def is_prime_num(n):
    arr = [True for _ in range(n+1)]
    
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i] == True:
            j=2
            while i*j <= n :
                arr[i*j] = False
                j += 1
    return [ i for i in range(2, n+1) if arr[i] ]
    

def solution(numbers):
    answer = 0
    lst=list(str(numbers))
    permute_lst=[]
    for i in range(len(numbers)):
        permute_lst.extend(list(map(int, map("".join, permutations(list(numbers), i + 1)))))
            
                
    number_lst = list(set(permute_lst))
    prime_lst = is_prime_num(max(number_lst))
    
    for i in number_lst :
        if i in prime_lst:
            answer+=1
    
    
    return answer