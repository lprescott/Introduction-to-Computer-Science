from graphics import *
newWin = GraphWin("Face", 500, 500)
center = Point(250, 250)

Head = Circle(center, 200)
leftEye = Circle(Point(175, 150), 20)
rightEye = Circle(Point(325, 150), 20)
Mouth = Oval(Point(175, 300), Point(325, 310))

Head.setFill("Yellow")
leftEye.setFill("Black")
rightEye.setFill("Black")
Mouth.setFill("Black")

Head.draw(newWin)
leftEye.draw(newWin)
rightEye.draw(newWin)
Mouth.draw(newWin)

newWin.getMouse()
newWin.close()
