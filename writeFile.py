# write a file
writeFile = open("myFile.txt", "w")
writeFile.write("Here is some text. ")
writeFile.write("Here is some more text. \n")
writeFile.write("And now we are done. \n\nTHE END.")

writeFile.close()
writeFile = open ("myFile.txt", "r")
print writeFile.read()
