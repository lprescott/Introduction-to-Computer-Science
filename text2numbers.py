#text2numbers.py

def main():
    message = raw_input("Please enter the message to encode: ")
    for ch in message:
        print ord(ch),

main()

'''
Output:
Please enter the message to encode: Luke Prescott
76 117 107 101 32 80 114 101 115 99 111 116 116
'''
