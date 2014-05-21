from graphics import *
from math import *
            

def createShapes(win):

    cir1 = Circle(Point(250,250), 200)
    #cir1.setFill('black')
    cir1.setWidth(5)
    #cir1.setOutline('black')
    cir1.draw(win)
    
    hrHand =  Line(Point(250, 250), Point(250,350))
    #hrHand.setFill('red')
    hrHand.setWidth(10)
    hrHand.draw(win)
    
    minHand =  Line(Point(250, 250), Point(250,450))
    #minHand.setFill('yellow')
    minHand.setWidth(7)
    minHand.draw(win)

    x = 250
    y = 450
    R = 200
    x2 = 250 
    y2 = 350
    
    secHand =  Line(Point(250, 250), Point(250,450))
    #secHand.setFill('orange')
    secHand.setWidth(5)
    secHand.draw(win)
    
    for i in range(600):

        #i = 60
        angle = (pi/30)*i
        B = (pi-angle)/2    
        longSide = sqrt( ( 2*(R**2) ) - ( 2* (R**2) * ( cos(angle) ) ) )
        print longSide
    
        dx = longSide*sin(B)
        dy = longSide*cos(B)
        
        if angle < pi:
            secHand.undraw()
            secHand = Line(Point(250,250), Point(x+abs(dx),y-abs(dy)))
            
            time.sleep(0.5)
            secHand.draw(win)
            secHand.setWidth(5)

        else:
            secHand.undraw()
            secHand = Line(Point(250,250), Point(x-abs(dx),y-abs(dy)))
            
            time.sleep(0.5)
            secHand.draw(win)
            secHand.setWidth(5)
        

            if i > 60:
                if angle < pi:
            
                    minHand = Line(Point(250,250), Point(x+abs(dx),y-abs(dy)))
                    time.sleep(0.5)
                    minHand.undraw()
                    minHand.draw(win)

                else:
            
                    minHand = Line(Point(250,250), Point(x-abs(dx),y-abs(dy)))
                    minHand.undraw()
                    time.sleep(0.5)
                    minHand.draw(win)
            

def main():
    win = GraphWin(500,500,500)
    win.yUp()
    createShapes(win)
    
    
    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()




main()
