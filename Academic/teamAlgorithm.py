#teamAlgorithm

avgtimepermile = 0
avgspeedmph = 0

distance = 10
timeMinutes = 43.50
timeSeconds = 43.50*60


conversionfactor = 0.621371
miles = distance * conversionfactor
print miles

avgtimepermileMinutes = timeMinutes/miles

avgtimepermileHours = (miles * 3600) / timeSeconds




print avgtimepermileMinutes
print avgtimepermileHours


#avgspeedmph = 
