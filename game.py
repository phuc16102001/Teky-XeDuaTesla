from turtle import*
from math import*
from random import*
score=0
dscar=[]
def play():
    win.bgpic("duongdua.gif")
    scorePen.penup()
    scorePen.goto(-300,300)
    scorePen.hideturtle()

    
    bmw.penup()
    bmw.shape("xeduabmw.gif")
    bmw.goto(0,-300)

    boughtnewcar()
    boughtnewcar()


    
    lose=False
    while(lose==False):
        for i in range(len(dscar)):
            xebo=dscar[i]
            bodi(xebo)
            if(distance(xebo,bmw)<50):
                lose=True
        delay(100)
    win.bgpic("thua.gif")
    bmw.hideturtle()
    for i in range(len(dscar)):
        xebo=dscar[i]
        xebo.hideturtle()

def distance(cona,conb):
    chieudai=cona.xcor()-conb.xcor()
    chieurong=cona.ycor()-conb.ycor()
    dis=sqrt(chieudai**2+chieurong**2)
    return dis
def boughtnewcar():
    xebo=Turtle()
    xebo.penup()
    xebo.shape("bo.gif")
    xebo.goto(randint(-170,170),400)
    xebo.speed(0)
    dscar.append(xebo)
def gotoleft():
    global bwm
    x=bmw.xcor()
    y=bmw.ycor()
    if bmw.xcor()>-170:
        x-=30
    bmw.goto(x,y)
def gotoright():
    global bwm
    x=bmw.xcor()
    y=bmw.ycor()
    if bmw.xcor()<170:
        x+=30
    bmw.goto(x,y)
def updatescore():
    global score
    score+=50
    scorePen.clear()
    scorePen.write(score)
def bodi(bo):
    x=bo.xcor()
    y=bo.ycor()
    y-=10
    bo.goto(x,y)
    if(y<-400):
        bo.hideturtle()
        bo.goto(randint(-170,170),400)
        bo.showturtle()
        updatescore()
win=Screen()    
win.setup(710,800)
win.bgpic("huongdankhachhang.gif")
win.addshape("xeduabmw.gif")
win.addshape("bo.gif")
scorePen=Turtle()
bmw=Turtle()
win.onkey(gotoleft,("a"))
win.onkey(gotoright,("d"))
win.onkey(play,("Return"))
win.listen()

