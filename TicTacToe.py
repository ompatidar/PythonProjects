board=[" " for i in range(9)]

def print_board():
    
    r1="|{}|{}|{}|".format(board[0],board[1],board[2])
    r2="|{}|{}|{}|".format(board[3],board[4],board[5])
    r3="|{}|{}|{}|".format(board[6],board[7],board[8])
    print()
    print("#"*7)
    print(r1)
    print(r2)
    print(r3)
    print("#"*7)
    print()
def move(icon):
    print("this is your turn player {}".format(icon))
    choice=int(input("from 1-9 :").strip())
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        print()
        print("space has been taken by opposition party")
        return move(icon)
def isvict(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon)or\
       (board[3]==icon and board[4]==icon and board[5]==icon)or\
       (board[6]==icon and board[7]==icon and board[8]==icon)or\
       (board[0]==icon and board[3]==icon and board[6]==icon)or\
       (board[1]==icon and board[4]==icon and board[7]==icon)or\
       (board[2]==icon and board[5]==icon and board[8]==icon)or\
       (board[0]==icon and board[4]==icon and board[8]==icon)or\
       (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False
def isdraw():
    if " " not in board:
        return True
    else:
        return False 
while True:
    print_board()
    move("X")
    if isvict("X"):
        print("congratulations X you won the match")
        print_board()
        ag=input("Again want to play then press y else n : ").strip().lower()
        if ag=="y":
            for i in range(9):
                board[i]=" "
            print_board()
            move("X")
        else:
            break
    elif isdraw():
        print("Match has been draw")
        print_board()
        ag=input("Again want to play then press y else n : ").strip().lower()
        if ag=="y":
            for i in range(9):
                board[i]=" "
            print_board()
            move("X")
        else:
            print("Thank you , we are closing the tab")
            break
    print_board()
    move("O")
    if isvict("O"):
       print("congratulations O you won the match")
       print_board()
       ag=input("Again want to play then press y else n : ").strip().lower()
       if ag=="y":
            for i in range(9):
                board[i]=" "
            print_board()
            move("O")
       else:
           print("Thank you , we are closing the tab")
           break
    elif isdraw():
        print("Match has been draw")
        print_board()
        ag=input("Again want to play then press y else n : ").strip().lower()
        if ag=="y":
            for i in range(9):
                board[i]=" "
            print_board()
            move("O")
        else:
           print("Thank you , we are closing the tab")
           break
       
        
        
