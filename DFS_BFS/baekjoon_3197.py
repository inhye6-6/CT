# 백조의 호수
 
# dfs TLE


r,c = map(int, input().split())
lake = []
swan = [] # 위치
count = 0
for i in range(r):
    lst = list(input())
    lake.append(lst)
    if 'L' in lst :
        swan.append([i,lst.index('L')])

x1,y1=swan[0]
x2,y2=swan[1]        
y= min(y1,y2)
ob_y =abs(y1-y2)
        
def melt(i,j):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
   
    for n in range(4):
        nx = i+dx[n]
        ny = j+dy[n]
        if nx<0 or nx>=r or ny<0 or ny>=c :
            continue
        lake[nx][ny]='.'

def check():
    if lake[x1][y:y+ob_y] == ['.']*ob_y and [lake[i][y2] for i in range(x1,x2+1)] == ['.']*(x2-x1):
        return True
    if lake[x2][y:y+ob_y] == ['.']*ob_y and [lake[i][y1] for i in range(x1,x2+1)] == ['.']*(x2-x1):
        return True
    return False

while True :
    if check() :
        break
    
    count+=1
    for i in range(r):
        for j in range(c):
            if lake[i][j]!='X':
                melt(i,j)
print(count)            
