from Tkinter import *
import tkFont
import game

buttonName={"button1" : 0, "button2" : 1, "button3" : 2, "button4":3, "button5" : 4, "button6" : 5, "button7" : 6, "button8":7, "button9":8}
def submit(name):
    game.player_move=int(buttonName[name])
    game.user=True
    print game.player_move
    

def gui():
    root = Tk()
    root.geometry("300x300")

#myfont = tkFont.Font(family='Comic Sans MS', size=36, weight='bold')

    button1 = Button(root, text="X", bg="#333",height = 7, width = 15,command=submit("button1"))
    button2 = Button(root, text="Button 2", bg="#333",height = 7, width = 15, command=submit("button2"))
    button3 = Button(root, text="Button 3", bg="#333",height = 7, width = 15,command=submit("button3"))
    button4 = Button(root, text="Button 4", bg="#333",height = 7, width = 15,command=submit("button4"))
    button5 = Button(root, text="Button 5", bg="#333",height = 7, width = 15,command=submit("button5"))
    button6 = Button(root, text="Button 6", bg="#333",height = 7, width = 15,command=submit("button6"))
    button7 = Button(root, text="Button 7", bg="#333",height = 7, width = 15,command=submit("button7"))
    button8 = Button(root, text="Button 8", bg="#333",height = 7, width = 15,command=submit("button8"))
    button9 = Button(root, text="Button 9", bg="#333",height = 7, width = 15,command=submit("button9"))


    button1.grid(row=0, column=0,columnspan=1,sticky='EWNS')
    button2.grid(row=0, column=1,columnspan=1,sticky='EWNS')
    button3.grid(row=0, column=2,columnspan=1,sticky='EWNS')
    button4.grid(row=1, column=0,columnspan=1,sticky='EWNS')
    button5.grid(row=1, column=1,columnspan=1,sticky='EWNS')
    button6.grid(row=1, column=2,columnspan=1,sticky='EWNS')
    button7.grid(row=2, column=0,columnspan=1,sticky='EWNS')
    button8.grid(row=2, column=1,columnspan=1,sticky='EWNS')
    button9.grid(row=2, column=2,columnspan=1,sticky='EWNS')


    root.mainloop()
