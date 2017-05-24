import math

def convertTemp(degreesC):
    cel = float(degreesC)
    fahr = (9/5) * cel + 32
    print "the Farenheit temperature is: ", fahr

def missle(height, angle):
    radians = angle * (math.pi/180)

    distance = height/(math.sin(angle))
    distance = str(distance)
    radians = str(radians)

    print "The distance (in km) this missle must travel is: " + distance + " and the angle in radians is: " + radians 
    
def evenOrOdd(number):
    return number % 2 == 0
    
