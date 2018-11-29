# AJAY MONGA -- QUESTION 2 -- COM SCI TEST -- FEBRUARY 14, 2017

# imports 

# Nothing to Import 

# Functions

def caught_speeding(speed, birthday): 
	if (speed <= 60) and (birthday == False): # Returns 0 if the speed is less than 60 
		return 0 
	elif (speed >= 61) and (speed <= 80) and (birthday == False): # If the speed is in the range of 61-80 and it is not their birthday, it returns a 1
		return 1
	elif (speed > 81) and (birthday == False): # If the speed is any integer larger than 81 and not their birthday, then it returns 2
		return 2 
	elif (birthday == True) and (speed <= 65): # If it is their birthday and their seed is 65 or lower then it returns 0
		return 0 
	elif (birthday == True) and (speed >= 66) and (speed <=  85): # If it is their birthday and they are between 66-85, then it returns 1
		return 1
	elif (birthday == True) and (speed >= 86): # If it is their birthday, but are going any faster than 86 then it returns 2
		return 2 

def input_string(birthday):

 # This small function tells the system that if user answers "yes" to the promt, then to convert that to True or False for the caught_speeding function
	

def input_string(birthday):
	if (birthday == "yes") 
		return True 
	elif (birthday == "no"): 
		return False 

# Main Code


speed = input("what is your speed? ") # This asks for the speed, it is input for integers
birthday = raw_input("Is it your birthday? answer: yes or no ") # This asks for if it is your birthday or not, this is raw_input for strings



input_string(birthday) # This calls the function to convert the "yes" or "no" to True or False
print caught_speeding(speed, birthday)  # This prints the result from the caught_speeding function

 
