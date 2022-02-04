"""
중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫

갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 
"""
import math
def solution(brown, yellow):
    total = brown + yellow
    # 카펫은 yellow의 가로 세로보다 +2 많음

    for j in range(1,int(math.sqrt(yellow))+1):
        if yellow % j != 0 :
            continue

        i = yellow // j
        if (i+2)*(j+2) == total:
            return [(i+2),(j+2)]
            
