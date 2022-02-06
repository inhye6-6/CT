def solution(N, number):
    d=[0,{N}]
    if N== number:
        return 1 

    for i in range(2,9):
        numbers = set()
        numbers.add(int(str(N)*i))
        for a in range(1,(i-1)//2+1):
            for x in d[a]:
                for y in d[i-a]:
                    numbers.add(x-y)
                    numbers.add(y-x)
                    numbers.add(x+y)
                    numbers.add(x*y)
                    if x != 0 : 
                        numbers.add(y//x)
                    if y != 0 :
                        numbers.add(x//y)
        if number in numbers :
            return i
        d.append(numbers)
    
    return -1