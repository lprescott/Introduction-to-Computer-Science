from graphics import *
def main():
    win = GraphWin("Draw a Star", 500, 500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on five points")
    message.draw(win)

    #Get and draw three vertices of star
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5.draw(win)

    #Use Polygon object to draw the star
    star = Polygon(p1,p2,p3,p4,p5)
    star.setFill("yellow")
    star.setOutline("yellow1")
    star.draw(win)

    #Wait fo another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
