import handler
import TicTacToeClass
import test
from Tkinter import *
import tkFont
import tkMessageBox
player_move= -99
user=False
buttonName={"button1" : 0, "button2" : 1, "button3" : 2, "button4":3, "button5" : 4, "button6" : 5, "button7" : 6, "button8":7, "button9":8}
buttons = []




def submit(num):
    #print num
    player_move=num
    user=True
    print player_move
    buttons[num].config(text="",bg="#305906",state="disabled")
    
    
    player = 'X'
        #player_move = int(raw_input("Next Move: ")) - 1
        #if player_move <0 or user==False:
           # continue
    if not player_move in board.available_moves():
        #print "bang"
        return
    board.make_move(player_move, player)
    board.show()

    if board.complete():
        print "complete"
        print "winner is", board.winner()
        tkMessageBox.showinfo('Game Over', 'No One win, Try again!!!!')
        return
    player = handler.get_enemy(player)
    computer_move = handler.determine(board, player)
    board.make_move(computer_move, player)
    buttons[computer_move].config(text="",bg="#8C191B",state="disabled")
    board.show()
    if board.winner()!=None:
        print "winner is****", board.winner()
        for index in range(9): 
            if index in board.available_moves():
                buttons[index].config(state="disabled")
        if board.winner()=="X":
            tkMessageBox.showinfo('Game Over', 'Congratulations you won the game!!!!')
        else:
            tkMessageBox.showinfo('Game Over', 'Sorry, You lost!!!!')
        return 
        

def Bclick():
    
    button1 = Button(root, text="", bg="#333",height = 7, width = 15,command=lambda:submit(0))
    button2 = Button(root, text="", bg="#333",height = 7, width = 15, command=lambda:submit(1))
    button3 = Button(root, text="", bg="#333",height = 7, width = 15,command=lambda:submit(2))
    button4 = Button(root, text="", bg="#333",height = 7, width = 15,command=lambda:submit(3))
    button5 = Button(root, text="", bg="#333",height = 7, width = 15,command=lambda:submit(4))
    button6 = Button(root, text="", bg="#333",height = 7, width = 15,command=lambda:submit(5))
    button7 = Button(root, text="", bg="#333",height = 7, width = 15,command=lambda:submit(6))
    button8 = Button(root, text="", bg="#333",height = 7, width = 15,command=lambda:submit(7))
    button9 = Button(root, text="", bg="#333",height = 7, width = 15,command=lambda:submit(8))


    button1.grid(row=0, column=0,columnspan=1,sticky='EWNS')
    button2.grid(row=0, column=1,columnspan=1,sticky='EWNS')
    button3.grid(row=0, column=2,columnspan=1,sticky='EWNS')
    button4.grid(row=1, column=0,columnspan=1,sticky='EWNS')
    button5.grid(row=1, column=1,columnspan=1,sticky='EWNS')
    button6.grid(row=1, column=2,columnspan=1,sticky='EWNS')
    button7.grid(row=2, column=0,columnspan=1,sticky='EWNS')
    button8.grid(row=2, column=1,columnspan=1,sticky='EWNS')
    button9.grid(row=2, column=2,columnspan=1,sticky='EWNS')
    
    buttons.append(button1)
    buttons.append(button2)
    buttons.append(button3)
    buttons.append(button4)
    buttons.append(button5)
    buttons.append(button6)
    buttons.append(button7)
    buttons.append(button8)
    buttons.append(button9)
    #print "bclick end"



if __name__ == "__main__":
    board = TicTacToeClass.Tic()
    root = Tk()
    root.geometry("300x300")
    root.title("Tic Tac Toe")
    board.show()
    #print "bclick"
    Bclick()

    #while not board.complete():
       
    #print "winner is", board.winner()

    root.mainloop()