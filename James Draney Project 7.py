#James Draney
#Letsgetit
#email: james.draney1@marist.edu

from graphics import *
import math



def distance(point,circle):
    x=point.getX()-circle.getCenter().getX()
    y=point.getY()-circle.getCenter().getY()
    dist=math.sqrt(x*x+y*y)

    return dist<=circle.getRadius()

def main ():
    win = GraphWin()

    white=Circle(Point(50,50),50)
    white.setFill("white")
    white.draw(win)

    blue=Circle(Point(50,50),40)
    blue.setFill("blue")
    blue.draw(win)

    black=Circle(Point(50,50),30)
    black.setFill("black")
    black.draw(win)

    red=Circle(Point(50,50),20)
    red.setFill("red")
    red.draw(win)

    yellow=Circle(Point(50,50),10)
    yellow.setFill("yellow")
    yellow.draw(win)

    score=0
    total=0
    
    for i in range(5):
        mouse=win.getMouse()
        if(distance(mouse,yellow)):
            score=9
        elif(distance(mouse,red)):
            score=7
        elif(distance(mouse,black)):
            score=5
        elif(distance(mouse,blue)):
            score=3
        elif(distance(mouse,white)):
            score=1
        else:
            score+=0

        print("Score: ", score)

        total+=score
        
        print("Total points: ", total)

        win.getMouse()
main()

