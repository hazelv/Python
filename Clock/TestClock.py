from graphics import *
import time
import os

#This method will draw the clock face.
def drawClock( win ):
    #Draw outer circle
    outline= Circle(Point(250,250), 200)
    outline.setWidth(2)
    outline.draw(win)

    center= Circle(Point(250,250), 5)
    center.setWidth(2)
    center.draw(win)
    #@secHand: var for the second hand on clock
    secHand =  Line(Point(250, 250), Point(250,450))
    secHand.setWidth(2)
    secHand.draw(win)
    #@minHand: var for the minute hand on clock
    minHand =  Line(Point(250, 250), Point(250,450))
    minHand.setWidth(3)
    minHand.draw(win)
    #@hrHand: var for the hour hand on clock
    hrHand= Line(Point(250,250), Point(250,350))
    hrHand.setFill('red')
    hrHand.setWidth(6)
    hrHand.draw(win)
    #Draw hour hand, minute hand, second hand
    secHand.delete(self.id)
    minHand.delete(self.id)
    hrHand.delete(self.id)
    secHand.undraw()
    minHand.undraw()
    hrHand.undraw()
    
def drawSecPic( win ):
    outline= Circle(Point(250,250), 200)
    outline.setWidth(2)
    outline.draw(win)

    center= Circle(Point(250,250), 5)
    center.setWidth(2)
    center.draw(win)

    secHand =  Line(Point(250, 250), Point(350,300))
    secHand.setWidth(2)
    secHand.draw(win)

    minHand =  Line(Point(250, 250), Point(100,450))
    minHand.setWidth(3)
    minHand.draw(win)

    hrHand= Line(Point(250,250), Point(300,200))
    hrHand.setFill('red')
    hrHand.setWidth(6)
    hrHand.draw(win)
    
#def cls():
    #os.system("clear")
    
def main():
    #runs code
    win = GraphWin("Greatest Clock Ever", 500, 500)
    win.yUp()
    drawClock(win)
    time.sleep(4)
    #cls()
    drawSecPic(win)
    
    win.promptClose(win.getWidth()/2, 20)

main()
