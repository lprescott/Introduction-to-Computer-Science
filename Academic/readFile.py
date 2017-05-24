f1 = open('myFile.txt' , 'r')
count = 0
for line in f1:
    count = count + 1
print 'Line count', count

print "Name of the file: ", f1.name
print "Close or not: ", f1.closed
print "Opening mode: ", f1.mode
