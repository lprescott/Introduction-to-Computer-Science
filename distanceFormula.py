#distanceFormula.py
import math

print "Enter point 1"
x1 = input("Enter the x value: ")
x1 = float(x1)
y1 = input("Enter the y value: ")
y1 = float(y1)

print "Enter point 2"
x2 = input("Enter the x value: ")
x2 = float(x2)
y2 = input("Enter the y value: ")
y2 = float(y2)

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
x1 = str(x1)
x2 = str(x2)
y1 = str(y1)
y2 = str(y2)
distance = str(distance)

print "The distance between the point ("+x1+","+y1+") and the point ("+x2+","+y2+") is: " + distance
