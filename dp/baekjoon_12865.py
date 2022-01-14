import sys
input = sys.stdin.readline

n,k = map(int,input().split())
items = [tuple(map(int,input().split())) for _ in range(n)]
d = [[0]*
items.sort(key= lambda x : (x[0],-x[1]))

w = 0
v = 0
max_v=0



for i in range(n-1):
    w = items[i][0]
    v = items[i][1]
