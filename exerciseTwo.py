#Team 1
#exerciseTwo.py

def main():
    
    input = raw_input("Please enter a list of integers on one line separated by commas: ")
    inputList = input.split(",")
    
    overList = []
    
    for i in range(len(inputList)):
        if int(inputList[i]) > 100:
            overList.append("Over")
        else:
            overList.append(inputList[i])

    print overList
            

main()
