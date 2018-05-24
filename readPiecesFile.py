f = open("myFile.txt")
next = f.read(1)
while next != "":
    print(next)
    next = f.read(1)
