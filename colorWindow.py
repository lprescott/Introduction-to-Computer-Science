'''
Created on Oct 14, 2015

@author: Luke Prescott
'''

from graphics import *

def main():
    
    win1 = GraphWin("Color the window.", 500, 500)
    win1.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click a button, or anywhere else to exit.")
    message.draw(win1)
    
    #button1
    button1 = Rectangle(Point(3, 1), Point(4,2))
    button1.setFill("red4")
    button1.draw(win1)
    button1Text = Text(Point(3.5, 1.5), "Red")
    button1Text.setTextColor("red")
    button1Text.draw(win1)
    
    #button2
    button2 = Rectangle(Point(4.5, 1), Point(5.5,2))
    button2.setFill("green4")
    button2.draw(win1)
    button2Text = Text(Point(5, 1.5), "Green")
    button2Text.setTextColor("green")
    button2Text.draw(win1)
    
    #button3
    button3 = Rectangle(Point(6, 1), Point(7,2))
    button3.setFill("blue4")
    button3.draw(win1)
    button3Text = Text(Point(6.5, 1.5), "Blue")
    button3Text.setTextColor("blue")
    button3Text.draw(win1)

    clickingButton = True

    while clickingButton == True:
        
        mouseClick = win1.getMouse()
    
        if mouseClick.getX() > 3 and mouseClick.getX() < 4 and mouseClick.getY() > 1 and mouseClick.getY() < 2:
            win1.setBackground("red")
    
        elif mouseClick.getX() > 4.5 and mouseClick.getX() < 5.5 and mouseClick.getY() > 1 and mouseClick.getY() < 2:
            win1.setBackground("green")
        
        elif mouseClick.getX() > 6 and mouseClick.getX() < 7 and mouseClick.getY() > 1 and mouseClick.getY() < 2:
            win1.setBackground("blue")

        else:
            clickingButton = False


    win1.close()
    
main()

