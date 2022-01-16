
# 40684KB, 816ms
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
d = {0:0}

for _ in range(n):
    c_w,c_v= map(int,input().split())
    tmp = {}
    for w, v in d.items() :
        if (c_w + w) <= k and (c_v + v) > d.get(c_w + w ,0) :
            tmp[c_w + w] = c_v + v
    d.update(tmp)

print(max(d.values()))