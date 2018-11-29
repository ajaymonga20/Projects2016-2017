# Rowing split calculator APP - AJAY MONGA - Sunday, Feburary 26, 2017 

# Imports - nothing

# Functions 

def calc(what): #Chooses what to calculate   
	if(what == "split"): 
		time = int(input("enter your time "))
		distance = int(input("enter your distance ")) 
		print((500 * (time / distance)) * 60)     
	elif(what == "distance"): 
		print("calculating distance") 
	elif(what == "time"):
		print ("calculating time") 
	else:
		print ("invalid entry, please type split, time or distance") 
def split(time, distance): 
	time = input("Enter your time ") 
	distance = input ("Enter your distance") 
# Main Code

what = input("what do you wanna calculate? ") # User input for what they wanna calculate 
print (calc(what).str) # prints split


print(split)


