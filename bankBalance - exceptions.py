#bankBalance.py
#Team 1

def main():

    balance = eval(raw_input("What is your bank account balance?"))

    if balance < 200:
        extrafee = 15
    else:
        extrafee = 0
        
        


    
    charge = 12

    checks = eval(raw_input("How many checks did you write this month?"))

    if checks < 20:
        fee = .10
    elif 20 <= checks <= 39:
        fee = .08
    elif 40 <= checks <= 59:
        fee = .06
    elif 60 <= checks <= 100:
        fee = .14
    else:
        print "you are outside the range of checks."

    totalFees = charge + (checks * fee) + extrafee

    accountBalance = balance - totalFees
    

    print "The total amount of fees for the month are $", totalFees

    print "Your account balance is $", accountBalance
    


main()
