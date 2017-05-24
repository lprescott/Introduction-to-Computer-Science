#Team 1
#Quiz

def main():

    name = raw_input("What is your name? ")
    print "Hi!", name
    print "Good Luck!"

    countRight = 0
    
    #Question 1
    questionOne = eval(raw_input("What's the name for excessive bodily hair growth in women? \n1. Hirsutism \n2. Androgyny \n3. Masculinism \n4. Feminization \n"))
    if questionOne == 1:
        print "Correct!"
        countRight = countRight + 1
    else:
        print "Sorry Wrong."


    
    
    #Question 2
    questionTwo = eval(raw_input("How many bones are there in a giraffes neck? \n1. 10 \n2. 13 \n3. 7 \n4. 50 \n"))
    if questionTwo == 3:
        print "Correct!"
        countRight = countRight + 1
    else:
        print "Sorry Wrong."


    
    #Question 3
    questionThree = eval(raw_input("What is Elvis Presley's middle name? \n1. Johny \n2. Aaron \n3. Frank \n4. Neutron \n"))
    if questionThree == 2:
        print "Correct!"
        countRight = countRight + 1
    else:
        print "Sorry Wrong."



    #Question 4
    questionFour = eval(raw_input("You start with 9,000 coins and give away 1,000 every day. How many days untill you have 4,000 coins? \n"))
    if questionFour == 5:
        print "Correct!"
        countRight = countRight + 1                                  
    else:
        print "Sorry Wrong."



    #Question 5
    questionFive = raw_input("Finish this sentence: Winter is ______! *Hint: GOT \n")
    if questionFive == "coming":
        print "Correct!"
        countRight = countRight + 1
    elif questionFive == "Coming":
        print "Correct!"
        countRight = countRight + 1
    else:
        print "Sorry Wrong."



    score = float((countRight/5.0) * 100)
    
    print  'You got', countRight, 'right. Your score is: ', score, "%"   
    

main()
