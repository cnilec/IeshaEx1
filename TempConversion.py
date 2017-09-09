# Take inputs from user about Temp in Deg F and the day of week for the number
# The prorgam ends when the user enters "Friday"
# The Code has to do the following
# a - Print the Temp in Deg C using C = (F-32)/1.8
# b - Print the Highest and Lowest Temp in Deg C in the Week
# c - Print the number of days which had temp less than 20 C and the number of days above of equal to 20 C
# d - Print Avg Temp in Deg C across the week

# Declare Variables
DayOfWeek = ""
TempDF = 0
TempDC = 0
TempH = 0
TempL = 10000000
TempL20 = 0
TempGE20 = 0
TempAvg = 0
CountofDays = 0
IsNumber = False

while (DayOfWeek.upper() != "FRIDAY"):

	# Take Input
	while (IsNumber == False):
		TempDF = input("Temperature in Deg F: ")
		IsNumber=TempDF.isdigit()

	while (DayOfWeek.upper() not in ("MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY")):
		DayOfWeek = input("Day of the Week :")

	# Convert to Deg C
	TempDC = ((int(TempDF)-32)/1.8)

	# Print out Deg C
	print("Temp in Deg C on "+DayOfWeek+" is "+str(TempDC))

	# Check for Highest
	if int(TempH) < int(TempDC):
		TempH = int(TempDC)

	#Check for Lowest
	if int(TempL) > int(TempDC):
		TempL = int(TempDC)

	#Count the number of days below and above 20 Deg C
	if int(TempDC) < 20:
		TempL20 = int(TempL20)+1
	else:
		TempGE20 = int(TempGE20)+1

	# Update count of days / input elements
	CountofDays = int(CountofDays) + 1

	# Update TempAvg as the sum of All days temp 
	TempAvg = int(TempAvg)+int(TempDC)
	
	# Re-Initiate Variables
	IsNumber = False
	if (DayOfWeek.upper() != "FRIDAY"):
		DayOfWeek = "" 

# Calculate Avg Temp using the TempAvg variable which has the sum of all the Temps
TempAvg = int(TempAvg)/int(CountofDays)

# print all the other outputs for requirements b, c and d
print ("Highest Temp in the Week is "+str(TempH)+" Deg C")
print ("Lowest Temp in the Week is "+str(TempL)+" Deg C")
print ("Number of days in the Week with the temperature below 20 Deg C is "+str(TempL20)+" days")
print ("Number of days in the Week with the temperature above or equal to 20 Deg C is "+str(TempGE20)+" days")
print ("Average Temperature across the week is "+str(TempAvg)+" Deg C")


