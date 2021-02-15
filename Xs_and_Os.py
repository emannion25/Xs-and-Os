#Xs and Os
import random
from graphics import *

def clear_items(win):
    for i in range(len(win.items)):
        win.items[0].undraw()

def drawX(point):
    X=Text(point,'X')
    X.setSize(36)
    X.draw(win)

def drawO(point):
    O=Text(point,'O')
    O.setSize(36)
    O.draw(win)

def is_winner(player_set):
    for triple in winner_triple:
        if (triple[0] in player_set) and (triple[1] in player_set) and (triple[2] in player_set):
            L=Line(coords[triple[0]],coords[triple[2]])
            L.setFill('red')
            L.setWidth(2)
            L.draw(win)
            return True
    return False

def check_pairs(player_set):
    for triple in winner_triple:
        if (triple[0] in player_set) and (triple[1] in player_set) and (triple[2] in available):
            return triple[2]
        if (triple[0] in player_set) and (triple[2] in player_set) and (triple[1] in available):
            return triple[1]
        if (triple[1] in player_set) and (triple[2] in player_set) and (triple[0] in available):
            return triple[0]
    return 0

def user_turn(shape):
    if len(available)<1:
        return []
    choice=0
    while choice not in available:
        click=win.getMouse()
        x,y=click.getX(),click.getY()
        if y>=4:
            if x<=2: choice=1       
            elif x<=4: choice=2
            else: choice=3
        elif y>=2:
            if x<=2: choice=4
            elif x<=4: choice=5
            else: choice=6
        else:
            if x<=2: choice=7
            elif x<=4: choice=8
            else: choice=9
            
    available.remove(choice)
    user_squares.append(choice)
    
    if shape==0:
        drawO(coords[choice])
    else:
        drawX(coords[choice])

    if is_winner(user_squares):
        available.clear()
        global winner
        winner='user'
        print('User wins')
        T=Text(coords[0],'You win!')
        T.draw(win)
    return 0

def com_turn(shape):
    if len(available)<1:
        return []
    choice=check_pairs(com_squares)
    if choice<1:
        choice=check_pairs(user_squares)
    if choice<1:
        choice=random.choice(available)
        
    available.remove(choice)
    com_squares.append(choice)
    
    if shape==0:
        drawO(coords[choice])
    else:
        drawX(coords[choice])

    if is_winner(com_squares):
        available.clear()
        global winner
        winner='com'
        print('Com wins')
        T=Text(coords[0],'You Lose!')
        T.draw(win)
    return 0

def main():
    global win,coords,available,user_squares,com_squares,winner_triple,winner
    #Create grid
    win=GraphWin(title="X's and O's",width=300,height=300)
    w,h=300,300
    x,y=650,50 #Postion on screen
    win.master.geometry('%dx%d+%d+%d' % (w,h,x,y))
    win.setCoords(0,0,6,6)

    coords=[Point(3,5.8),Point(1,5),Point(3,5),Point(5,5),
                         Point(1,3),Point(3,3),Point(5,3),
                         Point(1,1),Point(3,1),Point(5,1)]
    #Choose shape
    Text(coords[5],'Choose\n Shape').draw(win)
    drawX(coords[4])
    drawO(coords[6])
    Line(Point(3,6),Point(3,3.5)).draw(win)
    Line(Point(3,0),Point(3,2.5)).draw(win)
    click=win.getMouse()
    x,y=click.getX(),click.getY()

    clear_items(win)

    if x<3: user_shape=1
    else: user_shape=0
    com_shape=(user_shape+1)%2

    #Choose player 1
    Text(coords[5],'Play\n First?').draw(win)
    Text(coords[4],'Yes').draw(win)
    Text(coords[6],'No').draw(win)
    Line(Point(3,6),Point(3,3.5)).draw(win)
    Line(Point(3,0),Point(3,2.5)).draw(win)
    click=win.getMouse()
    x,y=click.getX(),click.getY()

    clear_items(win)
    
    if x<3: player1='user'
    else: player1='com'

    #Insert outline
    Line(Point(0,2),Point(6,2)).draw(win)
    Line(Point(0,4),Point(6,4)).draw(win)
    Line(Point(2,0),Point(2,6)).draw(win)
    Line(Point(4,0),Point(4,6)).draw(win)

    #---Initialize---
    available=[1,2,3,
               4,5,6,
               7,8,9]
    winner_triple=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],
                   [2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    user_squares=[]
    com_squares=[]
    winner=None

    #---Begin Game---
    if player1=='user':
        while len(available)>0:
            user_turn(user_shape)            
            com_turn(com_shape)    
    else:
        while len(available)>0:             
            com_turn(com_shape)
            user_turn(user_shape)      

    if winner==None:
        print('Draw')
        Text(coords[0],'Draw!').draw(win)
    #Pause before end
    win.getMouse()
    win.close()

if __name__=='__main__':
    main()
