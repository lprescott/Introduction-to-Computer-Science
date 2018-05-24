#bankBalance.py
#Team 1

startingBalance = 500
totalDeposits = 0
totalWithdrawals = 0

deposits = open("deposits.txt", "r")

for line in deposits:
    number1 = line[:len(line)-1]
    number1 = float(number1)
    totalDeposits = totalDeposits + number1

withdrawals = open("withdrawals.txt", "r")

for line in withdrawals:
    number2 = line[:len(line)-1]
    number2 = float(number2)
    totalWithdrawals = totalWithdrawals + number2

endingBalance = startingBalance + totalDeposits - totalWithdrawals

print "The total amount deposited was: $", totalDeposits
print "The total amount withdrawn was: $", totalWithdrawals
print "The balance is: $", endingBalance
