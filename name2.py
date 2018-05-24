#name2.py

firstName = raw_input("Please enter your first name: ")
favoriteInteger = eval(raw_input("Please enter your favorite positive integer: "))
favoriteColor = raw_input("Please enter your favorite color: ")

newNum = favoriteInteger * 3
newNum = str(newNum)

print "Hello", firstName+",", "your new number is", newNum+ ".\nYour favorite color is".lstrip(' '), favoriteColor+ "."

