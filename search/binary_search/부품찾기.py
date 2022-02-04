import sys
read = sys.stdin.readline

n = int(input())
lst = list(map(int,read().split()))
lst.sort()
m = int(input())
request = list(map(int,read().split()))


def binary_search(arr,target,s,e) :
    while s<=e:
        mid =(s+e)//2
        if target ==arr[mid] :
            return mid
        elif target < arr[mid] :
            e = mid - 1
        else : 
            s = mid + 1

    return None

for target in request :

    result = binary_search(lst,target,0,n)
    
    if result == None:
        print('no',end=' ')
    else :
        print('yes',end=' ')
