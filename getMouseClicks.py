from graphics import *
win = GraphWin("Click Me!")
p = win.getMouse()
print "You clicked (%d, %d)" % (p.getX(), p.getY())
