from graphics import *
newWin = GraphWin("Shapes")
center = Point(100,100)
redCircle = Circle(center, 30)
redCircle.setFill("red")
redCircle.draw(newWin)
newWin.getMouse()
newWin.close()
