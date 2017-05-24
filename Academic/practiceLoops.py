#practiceLoops.py
import random

def main():

    try:
        num = int(input("insert a number: "))
        counter = 1

        while counter <= num:
            print counter
            counter = counter + 1

    except:
        print("Your input(s) was/were not all numbers.")

    try:
        x = 0
        maxx = 0
        minn = 999
        positiveInt = int(input("Enter a positive integer"))
    

        while x <= positiveInt:
            a = random.randint(1,999)
            print a

            if a > maxx:
                maxx = a

            if a < minn:
                minn = a
            
            x = x + 1

        print "The max is:", maxx
        print "The min is:", minn

    except:
        print("Your input(s) was/were not all numbers.")

    try:    
        number = 1
        total = 0

        while number > 0:
            number = float(input("Enter a postive number (negative to quit): "))
            if number > 0:
                total = total + number
            
        print "Sum =", total

    except:
        print("Your input(s) was/were not all numbers.")

    try:
        for row in range (6):
            for col in range (4):
                print "*",
            print " "

    except:
        print("Your input(s) was/were not all numbers.")

main()
