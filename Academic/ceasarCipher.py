#ceasarCipher.py

def main():
    plainText = raw_input("Please enter a string of plain text: ")
    keyValue = int(raw_input("Please enter the value of the key: "))
    list1 = []
    
    for ch in plainText:
        list1.append(ord(ch))
    for x in list1:
        x = x + keyValue
    
    message = ""
    for numStr in list1:
        message = message + chr(numStr)
    print "The encoded message is: ", message

main()
