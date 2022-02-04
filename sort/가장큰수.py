
def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(
        key = lambda x: x*3, reverse= True #1000까지라 9->999로 바꿔서 비교
    )
    
    answer = str(int(''.join(numbers))) # '000' 같은 거 -> 0으로 바꿔주기
    return answer