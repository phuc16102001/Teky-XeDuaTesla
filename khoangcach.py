from math import*
def distance(cona,conb):
    chieudai=cona.xcor()-conb.xcor()
    chieurong=cona.ycor()-conb.ycor()
    dis=sqrt(chieudai**2+chieurong**2)
    return dis
