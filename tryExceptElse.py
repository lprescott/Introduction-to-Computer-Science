def main():
    x = raw_input("enter x integer")
    y = raw_input("enter y integer")

    try:
        x = int(x)
        y = int(y)

    except NameError:
        print("Your input(s) was/were not all numbers.")

    except SyntaxError:
        print("Your input(s) was/were syntactically incorrect.")
        
    except:
        print("Something went wrong.")
    
    else:
        
        if x ==y:
            print "x and y are equal"
            
        if x < y:
            print "x is less than y"
            
        else:
            print "x is greater than y"


main()
