#uploaded on 17th may 2023 to find the best moves for the computer in a tic tak toe - moves are chosen in the order of preference: winning move > users winning move > random move
#updated on 24th may by addind a main method so that it is compatible with my program manager code

from random import *
from tkinter import *
def predict(moves, user,comp):
    p=WinCheck(moves, comp)
    if not p==(-1,-1):
        return p
    p= WinCheck(moves, user)
    if not p==(-1,-1):
        return p
    s=rando(moves)
    return s

def rando(moves):
    try:
        i=randint(0,2)
        j=randint(0,2)
        o=(i,j)
        if moves[o[0], o[1]]["state"]==DISABLED:
            return rando(moves)
        return o
    except RecursionError:
        return

def WinCheck(moves,user):
    for i in user:
        s=recurring(user,i)
        if s==(-1,-1) or moves[s[0],s[1]]["state"]==DISABLED:
            continue
        else:
            return s
    return(-1,-1)

def recurring(user, i):
    row=int((i-1)/3)
    if i==0:
        return (-1,-1)
    if not i%3==0:
        column=(i%3)-1
    else:
        column=2

    for j in range(0,3):
        if j==column:
            continue
        for k in user:
            if k==(row*3)+(j+1):
                return (row,3-(column+j))

    for j in range(0,3):
        if j==row:
            continue
        for k in user:
            if k==(j*3)+(column+1):
                return (3-(j+row),column)

    if column==row:
        for j in range(0,3):
            if j==column:
                continue
            for k in user:
                if k==(3*j)+(j+1):
                    return(3-(row+j),3-(column+j))

    if column==2-row:
        for j in range(0,3):
            if j==column:
                continue
            for k in user:
                if k==(3*(2-j))+(j+1):
                    return(3-(row+2-j),3-(column+j))

    return (-1,-1)

def main():
    pass
