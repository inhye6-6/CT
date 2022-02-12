import math
def is_prime_num(num):
    num=int(num)
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0 :
            return False
    return True

def solution(n, k):
    tmp = ''
    while n:
        tmp += str(n%k)
        n = n//k
    n=tmp[::-1]
    nums = n.split('0')
    count = 0


    for num in nums:
        if num == '' :
            continue
        if is_prime_num(num) :
            count +=1
    
    return count