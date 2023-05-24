#uploaded on 17th may 2023 to be a tictaktoe game with computer as an opponent and score will tallied as win=1, draw=0, lose=-1
#updated on 24th may by addind a main method so that it is compatible with my program manager code

from tkinter import *
import numpy as np
import random
import TicTakToeAI1 as ai

global user
user=np.zeros(9, dtype=int)
global comp
comp=np.zeros(9,dtype=int)

win=Tk()
win.resizable(False, False)
win.title("Tic Tak Toe")

global n
n=random.randint(0,100)

global c
global C
C=0
c=0

global sco
sco=0

def compInit():
    if not n%2==1:
        Ai()

def Ai():
    global gridB, n,c,C

    s=ai.predict(gridB, user, comp)
    if not s==None:
        comp[C] = (s[0] * 3) + (s[1] + 1)
        C=C+1
        if n % 2 == 1:
            gridB[s[0],s[1]].configure(text="O", state=DISABLED)
        if n % 2 == 0:
            gridB[s[0],s[1]].configure(text="X", state=DISABLED)
    w= winCondition(comp, C)
    if w==1:
        print("comp wins")
        scoreWrite(-1)
    if c + C == 9:
        draw()
        return
def reset():
    global c, C,n
    for i in range(0,9):
        user[i]=0
        comp[i]=0
    n=n+1
    c=0
    C=0
    for children in win.winfo_children():
        s="%s"%children
        k=s.find("frame")
        if k==-1:
            continue
        for child in children.winfo_children():
            child.configure(state=NORMAL, text="", bg="SystemButtonFace")
    compInit()

def finalize(a,b,c):
    global gridF
    for i in range(0,3):
        for j in range(0,3):
            if ((j+1)+i*3)==a or ((j+1)+i*3)==b or ((j+1)+i*3)==c:
                gridB[i,j].configure(bg='Light Green')


def winCondition(user1,p):
    d=0

    for i in range(0, p):
        if user1[i]==1 or user1[i]==2 or user1[i]==3:
            d=d+1
    d=result(d)
    if d==1:
        finalize(1,2,3)
        return 1

    for i in range(0, p):
        if user1[i]==1 or user1[i]==4 or user1[i]==7:
            d=d+1
    d = result(d)
    if d == 1:
        finalize(1, 4, 7)
        return 1

    for i in range(0, p):
        if user1[i] == 1 or user1[i] == 5 or user1[i] == 9:
            d = d + 1
    d = result(d)
    if d == 1:
        finalize(1,5,9)
        return 1

    for i in range(0, p):
        if user1[i]==7 or user1[i]==8 or user1[i]==9:
            d=d+1
    d = result(d)
    if d == 1:
        finalize(9, 7, 8)
        return 1

    for i in range(0, p):
        if user1[i]==3 or user1[i]==6 or user1[i]==9:
            d=d+1
    d = result(d)
    if d == 1:
        finalize(3,6, 9)
        return 1

    for i in range(0, p):
        if user1[i]==3 or user1[i]==5 or user1[i]==7:
            d=d+1
    d = result(d)
    if d == 1:
        finalize(3,5,7)
        return 1

    for i in range(0, p):
        if user1[i]==2 or user1[i]==5 or user1[i]==8:
            d=d+1
    d = result(d)
    if d == 1:
        finalize(2,5,8)
        return 1

    for i in range(0, p):
        if user1[i]==4 or user1[i]==5 or user1[i]==6:
            d=d+1
    d = result(d)
    if d == 1:
        finalize(4,5,6)
        return 1

    return 0

def end():
    for children in win.winfo_children():
        s="%s"%children
        n=s.find("frame")
        if not n==-1:
            for child in children.winfo_children():
                child.configure(state=DISABLED)

def draw():
    global gridB
    scoreWrite(0)
    print("Draw")
    for i in range(0,3):
        for j in range(0,3):
            gridB[i,j].configure(bg='Grey' ,state=DISABLED)


def result(e):
    if e==3:
        end()
        return 1
    else:
        return 0

def check(but):
    global n
    if n%2==1:
        but.configure(text="X", state=DISABLED)
    if n%2==0:
        but.configure(text="O", state=DISABLED)

def track(n):
    global c, user
    user[c]=n
    c=c+1
    w= winCondition(user, c)
    if w==1:
        print("User wins")
        scoreWrite(1)
    Ai()

def scoreWrite(n,*args):
    global sco, var
    sco=sco+n
    var.set(f"Score: {sco}")

global gridB
global gridF
gridB={}
gridF={}

menu=Menu(win, tearoff=0)
win.configure(menu=menu)
options=Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu=options)
options.add_command(label="Reset", command=reset)

global var
var=StringVar()
var.set("Score: 0")

score=Label(win, textvariable=var)
score.grid(row=3, column=0, columnspan=3, sticky='nsew')

for i in range(0,3):
    for j in range(0,3):
        gridF[i,j]=Frame(win,highlightbackground="Black", highlightthickness=1)
        gridF[i,j].grid(column=j, row=i)
        gridB[i,j]=Button(gridF[i,j],borderwidth=0, relief=SUNKEN,cursor="hand2"
                        , width=10,height=5,command= lambda i=i, j=j: [check(gridB[i,j]), track((j+1)+(i*3))]
                        , text="")
        gridB[i,j].grid(sticky='nsew')

if __name__=='__main__':
    compInit()

win.mainloop()
