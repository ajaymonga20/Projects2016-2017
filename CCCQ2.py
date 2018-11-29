# CCC 2014 - Question #2 = Vote Count
# Ajay Monga - January 30, 2017

# Vote Count - Program to find winner in CDN Idol 

# Imports - nada 

# Functions 
def voteCount(votes): 
	a = votes.count("A") # String Method .count is awesome! 
	b = votes.count("B") 
	if (a > b): 
		return "A" 
	elif (b > a): 
		return "B" 
	else: 
		return "Tie" 

# Main Code 
votes = raw_input("Enter your votes now: ") 
print voteCount(votes) 
