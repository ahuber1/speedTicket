# File:        speedTicket.py
# Author:      Andrew Huber
# Date:        October 26, 2016
# Section:     03
# E-mail:      ahuber1@umbc.edu
# Description: YOUR DESCRIPTION GOES HERE AND HERE
#              YOUR DESCRIPTION CONTINUED SOME MORE
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself.

# --------------------------------------------------------------------------------#
# ----------------------------------- NEW CODE -----------------------------------#
# --------------------------------------------------------------------------------#

def isInt(aString):
	for character in aString:
		if not character.isdigit():
			return False
	return True

# --------------------------------------------------------------------------------#
# ----------------------------------- NEW CODE -----------------------------------#
# --------------------------------------------------------------------------------#

def main():

	# --------------------------------------------------------------------------------#
	# ----------------------------------- NEW CODE -----------------------------------#
	# --------------------------------------------------------------------------------#

	# Get speed limit
	valid = False

	# Create and initialize variables
	speedLimit = ""
	drivingSpeed = ""

	while not valid:
		speedLimit = input("What is the speed limit in MPH (integers only)? ")
		if not isInt(speedLimit) or int(speedLimit) < 0 :
			print("Invalid input.")
		else:
			valid = True

	print() # adds blank line to make it easier to read

	valid = False

	# Get driving speed
	while not valid:
		drivingSpeed = input("What is the driving speed in MPH (integers only)? ")
		if not isInt(drivingSpeed) or int(drivingSpeed) < 0:
			print("Invalid input.")
		else:
			valid = True

	print() # adds blank line to make it easier to read

	# Convert speedLimit and drivingSpeed to ints
	speedLimit = int(speedLimit)
	drivingSpeed = int(drivingSpeed)

	# --------------------------------------------------------------------------------#
	# ----------------------------------- NEW CODE -----------------------------------#
	# --------------------------------------------------------------------------------#

	speedDifference = drivingSpeed - speedLimit

	# If they were speeding by less than 10 MPH (including not speeding), print
	if speedDifference < 10:
		print("You were over the speed limit by", speedDifference, "MPH")
		print("You recieve no ticket... this time.")

	# If they were speeding by 10 to 25 MPH
	elif speedDifference >= 10 and speedDifference <= 25:
		print("You were over the speed limit by", speedDifference, "MPH")
		print("You receive a ticket for a $75 fine.")

	# If they were speeding by more than 25 MPH, but less than 30 MPH, print
	elif speedDifference > 25 and speedDifference < 30:
		print("You were over the speed limit by", speedDifference, "MPH")
		print("You receive a ticket for a $150 fine.")

	# If they were speeding by 30 MPH or more, print
	else:
		print("You were over the speed limit by", speedDifference, "MPH")
		print("You recieve a ticket or a $500 fine, and a mandatory court date.")

	# print empty line
	print("")

main()
