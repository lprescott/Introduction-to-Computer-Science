'''
Created on Oct 14, 2015

@author: Team 1

Test Score Average
'''

from graphics import *

def main():
    
    win1 = GraphWin("Test Score Average", 500, 500)
    win1.setCoords(0.0, 0.0, 10.0, 10.0)

    message = Text(Point(5, 9.5), "Test Scores: ")
    message.draw(win1)

    test1 = Text(Point(2, 8.5), "Test One:")
    test1.draw(win1)
    test1Entry = Entry(Point(2,7.5), 5)
    test1Entry.setText("00.00")
    test1Entry.draw(win1)

    test2 = Text(Point(4, 8.5), "Test Two:")
    test2.draw(win1)
    test2Entry = Entry(Point(4,7.5), 5)
    test2Entry.setText("00.00")
    test2Entry.draw(win1)
    
    test3 = Text(Point(6, 8.5), "Test Three:")
    test3.draw(win1)
    test3Entry = Entry(Point(6,7.5), 5)
    test3Entry.setText("00.00")
    test3Entry.draw(win1)

    test4 = Text(Point(8, 8.5), "Test Four:")
    test4.draw(win1)
    test4Entry = Entry(Point(8,7.5), 5)
    test4Entry.setText("00.00")
    test4Entry.draw(win1)

    button = Rectangle(Point(2.5, 2.5), Point(7.5,5))
    button.draw(win1)
    buttonMessage = Text(Point(5, 3.75), "Calculate Average")
    buttonMessage.draw(win1)

    testAverageText = Text(Point(2.5, 1.5), "Test Average: ")
    testAverageText.draw(win1)

    clickingButton = True

    while clickingButton == True:
        
        mouseClick = win1.getMouse()
    
        if mouseClick.getX() > 2.5 and mouseClick.getX() < 7.5 and mouseClick.getY() > 2.5 and mouseClick.getY() < 5:
            testAverage = ((eval(test1Entry.getText()) + eval(test2Entry.getText()) + eval(test3Entry.getText()) + eval(test4Entry.getText()))/4)
            output = Text(Point(5, 1.5), testAverage)
            output.setText("%0.2f" % testAverage)
            output.draw(win1)
            buttonMessage.setText("Quit")
            clickingButton = False
            
            

        else:
            clickingButton = False
            
    mouseClick2 = win1.getMouse()
    if mouseClick2.getX() > 2.5 and mouseClick2.getX() < 7.5 and mouseClick2.getY() > 2.5 and mouseClick2.getY() < 5:
        win1.close()
   

main()
