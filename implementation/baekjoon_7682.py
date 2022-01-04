# 틱택토
# 29200KB, 72ms

def check(game,player):
    if game[0][0]==game[0][1]==game[0][2]==player:
        return True
    if game[1][0]==game[1][1]==game[1][2]==player:
        return True
    if game[2][0]==game[2][1]==game[2][2]==player:
        return True
    if game[0][0]==game[1][0]==game[2][0]==player:
        return True
    if game[0][1]==game[1][1]==game[2][1]==player:
        return True
    if game[0][2]==game[1][2]==game[2][2]==player:
        return True
    if game[0][0]==game[1][1]==game[2][2]==player:
        return True
    if game[2][0]==game[1][1]==game[0][2]==player:
        return True
    return False


while True:
    testcase=input()
    if testcase=="end":
        break
    game = [list(testcase)[3*i:3*i+3] for i in range(3)]
    xcnt=testcase.count('X')
    ocnt=testcase.count('O')
    dcnt=testcase.count('.')


    # X가 항상 먼저 시작하므로 최종 상태에서 
    # X의 개수는 O의 개수 + 1이거나 O의 개수와 같아야 함
    if xcnt>ocnt+1 or xcnt<ocnt :
        print("invalid")
        continue

    # X의 개수 = O의 개수 일 경우
    # O가 이겨야함
    if ocnt==xcnt:
        if check(game,"O") and not check(game,"X"):
            print("valid")
            continue
    
    # X의 개수 = O의 개수 + 1 일 수 있는 경우
    # 1) X가 이겼을 때
    # 2) 게임판이 가득차서 무승부일 때
    if ocnt+1==xcnt:
        if check(game,"X") and not check(game,"O"):
            print("valid")
            continue
            
        if dcnt == 0 and not check(game,"O"):
            print("valid")
            continue
            
    print("invalid")