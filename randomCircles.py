from graphics import *
import random

def main():
    
    win1 = GraphWin("Random Circles", 500, 500)
    win1.setCoords(0.0, 0.0, 10.0, 10.0)
    
    for i in range(50):
        circle = Circle(Point(random.randrange(0,10), random.randrange(0,10)), random.randrange(1, 5))
        r = random.randrange(0,255)
        g = random.randrange(0,255)
        b = random.randrange(0,255)
        color = color_rgb(r,g,b)
        circle.setFill(color)
        circle.draw(win1)

    win1.getMouse()
    win1.close()

main()
