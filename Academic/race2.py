#race2.py

distance = eval(raw_input("What is the distance of the race in kilometers?"))
timeMinutes = eval(raw_input("How long did it take you to finish in minutes?"))

                    
timeSeconds = (timeMinutes*60)

conversionfactor = 0.621371
miles = float(distance * conversionfactor)
print "The distance in miles is:",  str(miles)

avgtimepermileMinutes = timeMinutes/miles

avgtimepermileHours = (miles * 3600) / timeSeconds


print "The average time per mile in minutes is: ", str(avgtimepermileMinutes)
print "The average time per mile in hours is: ", str(avgtimepermileHours)

