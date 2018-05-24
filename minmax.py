#minmax.py
#Luke Prescott

import random

def main():
    rand1 = random.randrange(0, 999)
    rand2 = random.randrange(0, 999)
    rand3 = random.randrange(0, 999)

    print "The first random number is: ", rand1
    print "The second random number is: ", rand2
    print "The third random number is: ", rand3

    if rand1 > rand2 and rand1 > rand3:
        print "The max is: ", rand1
        if rand2 < rand3:
            print "The min is: ", rand2
        else:
            print "The min is: ", rand3

    elif rand2 > rand1 and rand2 > rand3:
        print "The max is: ", rand2
        if rand1 < rand3:
            print "The min is: ", rand1
        else:
            print "The min is: ", rand3

    elif rand3 > rand2 and rand3 > rand1:
        print "The max is: ", rand3
        if rand2 < rand1:
            print "The min is: ", rand2
        else:
            print "The min is: ", rand1

main()
