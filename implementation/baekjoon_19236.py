import sys
from copy import deepcopy
input = sys.stdin.readline

arr = [[None]*4 for _ in range(4)]
fish_idx=[None]*16
dx=[-1,-1,0,1,1,1,0,0]
dy=[0,-1,-1,-1,0,1,1,-1]

for i in range(4):
    testcase=list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = [testcase[2*j],testcase[2*j+1]-1]
        fish_idx[testcase[2*j]-1]=(i,j)


def turn_left(direction):
    return (direction+1)%8

def move_fish(arr,fish_idx, shark_x, shark_y):

    for i in range(16):
        if not fish_idx[i]:
            continue
        x, y = fish_idx[i]
        direction = arr[x][y][1]
        
        for _ in range(8):
            nx= x+dx[direction]
            ny = y+dy[direction]

            if nx<0 or nx>=4 or ny<0 or ny>=4  or (nx == shark_x and ny == shark_y):
                direction=turn_left(direction)
                continue

            arr[x][y][1]=direction
            arr[x][y], arr[nx][ny]= arr[nx][ny],arr[x][y]
            fish_idx[i], fish_idx[arr[nx][ny][0]-1] = (nx,ny),(x,y)
            break

def eat_fish(arr,fish_idx,shark_x,shark_y,total):
    global result
    arr = deepcopy(arr)

    total += arr[shark_x][shark_y][0]
    
    fish_idx[arr[shark_x][shark_y][0]]=None
    arr[shark_x][shark_y][0]== 0 
     
    move_fish(arr, fish_idx, shark_x, shark_y)
    
    p_move = []
    direction = arr[shark_x][shark_y][1]
    
    for _ in range(4):
        shark_nx = shark_x+ dx[direction]
        shark_ny =shark_y+ dy[direction]
        
        if shark_nx < 0 or shark_nx>=4 or shark_ny < 0  or shark_ny >=4 or arr[shark_nx][shark_ny][0] == 0:
            continue
        p_move.append((shark_nx, shark_ny))
     
    if not p_move :
        result = max(result, total)
        return 
    

    for i,j in p_move:
        eat_fish(arr,fish_idx,i,j)
        

result = 0
eat_fish(arr,fish_idx,0,0,0)
print(result)