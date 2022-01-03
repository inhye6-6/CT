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

    if xcnt>ocnt+1 or xcnt<ocnt :
        print("invalid")
        continue

    if ocnt==xcnt:
        if check(game,"O") and not check(game,"X"):
            print("valid")
            continue
    if ocnt+1==xcnt:
        if check(game,"X") and not check(game,"O"):
            print("valid")
            continue
            
        if dcnt == 0 and not check(game,"O"):
            print("valid")
            continue
            
    print("invalid")