#race1.py

distance = 10
timeMinutes = 43.50
timeSeconds = 43.50*60

conversionfactor = 0.621371
miles = distance * conversionfactor
print "The distance in miles is:",  str(miles)

avgtimepermileMinutes = timeMinutes/miles

avgtimepermileHours = (miles * 3600) / timeSeconds


print "The average time per mile in minutes is: ", str(avgtimepermileMinutes)
print "The average time per mile in hours is: ", str(avgtimepermileHours)

