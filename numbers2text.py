#numbers2text.py
import string

def main():
    inString = raw_input("Please enter the ASCII encoded message: ")
    message = ""
    for numStr in string.split(inString):
        asciiNum = eval(numStr)
        message = message + chr(asciiNum)
    print "The decoded message is: ", message
main()
