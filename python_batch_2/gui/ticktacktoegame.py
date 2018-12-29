from tkinter import *
from tkinter import messagebox
import tkinter

top = tkinter.Tk()

count = 0
frequency = {}
board = []
#top.geometry("100x100")
def hello():
    messagebox.showinfo("Say Hello", "Hello Wo   rld")

def checkWinner(num):
    global board
    row1 = (board[0][0] ==num and board[0][1] ==num and board[0][2] ==num)
    row2 = (board[1][0] ==num and board[1][1] ==num and board[1][2] ==num)
    row3 = (board[2][0] ==num and board[2][1] ==num and board[2][2] ==num)

    col1 = (board[0][0] ==num and board[1][0] ==num and board[2][0] ==num)
    col2 = (board[0][1] ==num and board[1][1] ==num and board[2][1] ==num)
    col3 = (board[0][2] ==num and board[1][2] ==num and board[2][2] ==num)

    diag1 =  (board[0][0] ==num and board[1][1] ==num and board[2][2] ==num)
    diag2 =  (board[0][2] ==num and board[1][1] ==num and board[2][0] ==num)

    if ( row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2):
        return 1
    else:
        return 0


def checkFinalWinner():
    flag = checkWinner(0)
    if flag == 1:
        return 0

    flag = checkWinner(1)
    if flag == 1:
        return 1
    return -1



def initGrid():
    global board
    for i in range(0,3):
        tmp = []
        for j in range(0,3):
            tmp.append(-1)
        board.append(tmp)

def setLabel(bt, x,y):
    global count
    global board
    count = count + 1
    if count%2 == 0:
        bt.set("X")
        board[x][y] = 1
    else:
        bt.set("O")
        board[x][y] = 0

def checkDuplicateCall(btn_no):
    global frequency
    if btn_no in frequency:
        return 1
    else:
        return 0

def checkFinalWinnerAndEnd():
    winner = checkFinalWinner()
    if winner == 0:
        messagebox.showinfo("Hello", "O has won the game . Congrats")
    elif winner == 1:
        messagebox.showinfo("Hello", "X has won the game . Congrats")


def action1():
    global frequency
    flag = checkDuplicateCall(1)
    if flag == 1:
        pass
    else:
        setLabel(btn1_text,0,0)
        frequency[1] = ""
        checkFinalWinnerAndEnd()

def action2():
    global frequency
    flag = checkDuplicateCall(2)
    if flag == 1:
        pass
    else:
        setLabel(btn2_text,0,1)
        frequency[2] = ""
        checkFinalWinnerAndEnd()

def action3():
    global frequency
    flag = checkDuplicateCall(3)
    if flag == 1:
        pass
    else:
        setLabel(btn3_text,0,2)
        frequency[3] = ""
        checkFinalWinnerAndEnd()

def action4():
    global frequency
    flag = checkDuplicateCall(4)
    if flag == 1:
        pass
    else:
        setLabel(btn4_text,1,0)
        frequency[4] = ""
        checkFinalWinnerAndEnd()

def action5():
    global frequency
    flag = checkDuplicateCall(5)
    if flag == 1:
        pass
    else:
        setLabel(btn5_text,1,1)
        frequency[5] = ""
        checkFinalWinnerAndEnd()

def action6():
    global frequency
    flag = checkDuplicateCall(6)
    if flag == 1:
        pass
    else:
        setLabel(btn6_text,1,2)
        frequency[6] = ""
        checkFinalWinnerAndEnd()

def action7():
    global frequency
    flag = checkDuplicateCall(7)
    if flag == 1:
        pass
    else:
        setLabel(btn7_text,2,0)
        frequency[7] = ""
        checkFinalWinnerAndEnd()

def action8():
    global frequency
    flag = checkDuplicateCall(8)
    if flag == 1:
        pass
    else:
        setLabel(btn8_text,2,1)
        frequency[8] = ""
        checkFinalWinnerAndEnd()

def action9():
    global frequency
    flag = checkDuplicateCall(9)
    if flag == 1:
        pass
    else:
        setLabel(btn9_text,2,2)
        frequency[9] = ""
        checkFinalWinnerAndEnd()

initGrid()
btn1_text = tkinter.StringVar()
B1 = Button(top, textvariable=btn1_text, command = action1, height=13, width=26)
btn1_text.set("")
B1.grid(row=0,column=0)

btn2_text = tkinter.StringVar()
B2 = Button(top, textvariable=btn2_text, command = action2, height=13, width=26)
btn2_text.set("")
B2.grid(row=0,column=1)

btn3_text = tkinter.StringVar()
B3 = Button(top, textvariable=btn3_text, command = action3, height=13, width=26)
btn3_text.set("")
B3.grid(row=0,column=2)

btn4_text = tkinter.StringVar()
B4 = Button(top, textvariable=btn4_text, command = action4, height=13, width=26)
btn4_text.set("")
B4.grid(row=1,column=0)

btn5_text = tkinter.StringVar()
B5 = Button(top, textvariable=btn5_text, command = action5, height=13, width=26)
btn5_text.set("")
B5.grid(row=1,column=1)

btn6_text = tkinter.StringVar()
B6 = Button(top, textvariable=btn6_text, command = action6, height=13, width=26)
btn6_text.set("")
B6.grid(row=1,column=2)

btn7_text = tkinter.StringVar()
B7 = Button(top, textvariable=btn7_text, command = action7, height=13, width=26)
btn7_text.set("")
B7.grid(row=2,column=0)

btn8_text = tkinter.StringVar()
B8 = Button(top, textvariable=btn8_text, command = action8, height=13, width=26)
btn8_text.set("")
B8.grid(row=2,column=1)

btn9_text = tkinter.StringVar()
B9 = Button(top, textvariable=btn9_text, command = action9, height=13, width=26)
btn1_text.set("")
B9.grid(row=2,column=2)


top.mainloop()