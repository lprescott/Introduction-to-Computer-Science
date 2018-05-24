#pigLatin.py
#Team 1

import string
def main():
    #Accept User input for phrase
    phrase = raw_input("Please enter a phrase to translate into pig latin: ")

    #This splits the phrase into a list via spaces
    phraseList = phrase.split(" ")
    newList = []  #This creates a new list

    #Creates a for loop that traverses the length of phraseList
    for x in range(len(phraseList)):
        word = phraseList[x] #This creates a variable called words at x

        #This converts each word into pig latin
        finalWord = word[1:len(word)] + word[:1] + "ay"
        newList.append(finalWord) #This adds the converted word back to newList

    #Joins each converted word with space into a string    
    space = " "
    print space.join(newList)
    
main()
