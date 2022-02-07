"""사실상 이후의 모든 시간을 볼 필요가 없다. 계속 값이 오를 때는 그 시점들을 다 스택에 넣다가 값이 떨어지는 그 시점에서 떨어진 값보다 큰 애들을 다 빼주면서 시간을 기록하면 된다. 이렇게 구현을 할 시 for문을 한번만 돌게 되므로 시간 복잡도가 O(n)으로 감소한다."""
def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i,price in enumerate(prices):
        while stack and stack[-1][1] > price :
            v = stack.pop() 
            answer[v[0]] = i- v[0]
        stack.append([i,price])
        
    while(stack):
        v = stack.pop()
        answer[v[0]] = len(prices)-v[0]-1
    return answer