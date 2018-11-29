# Ajay Monga - Algorithm Test - Question #1 - February 14, 2017

# Imports 

# Nothing to import



# Functions 

def not_string(str): 
	if (str[0:1] + str[0:2] + str[0:3] == "not"): # Adds the first three letters of the string to see if they equal "not"
		return  str #If those first three letters equal "not" then the code only returns the string
	else:
		return "not " + str # If the string inputed does not include the string "not" then it will print the string "not" before the string inputed 

# Main Code

str = raw_input("Type in a word: ") # This gives the user the ability to input a string of their choice

string = str  

print not_string(str) # we then call the function and tell it to print its result, using the algorithm in the function above


