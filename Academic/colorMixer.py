#colorMixer
#Luke Prescott and Michael Lim

def main():
    
    color1 = raw_input("What is the first primary color? (red, blue or yellow): ")
    color2 = raw_input("What is the second primary color? (red, blue or yellow): ")

    if color1 == "yellow" or color1 == "blue" or color1 == "red":
        if color2 == "yellow" or color2 == "blue" or color2 == "red":
            print "Colors are accepted."

            #code
            if color1 == "red" and color2 == "blue":
                print "Your secondary color is purple."

            elif color1 == "blue" and color2 == "red":
                print "Your secondary color is purple."

            elif color1 == "red" and color2 == "yellow":
                print "Your secondary color is orange."

            elif color1 == "yellow" and color2 == "red":
                print "Your secondary color is orange."

            elif color1 == "blue" and color2 == "yellow":
                print "Your secondary color is green."

            elif color1 == "yellow" and color2 == "blue":
                print "Your secondary color is green."
            
        else:
            print "Colors are not accepted."
    else:
        print "Colors are not accepted."

main()
