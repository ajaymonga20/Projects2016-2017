# Funtions 


def authenticateMe(user, password, secretuser, secretpass): 
	if (user == secretuser and password == secretpass): 
		return True 
	else: 
		return False 

secretUser = "ajay.monga"
secretPass = "hockey" 

# Main Code 

for i in range(4): 
	user = raw_input("Enter your user  name: ") 
	password = raw_input("Enter your password: ") 
	if (i == 3): 
		print("You have attempted to log in 4 times. Your account is locked.") 
	elif (authenticateMe(user, password, secretUser, secretPass) == True): 
		print("Welcome you have been authenticated") 
		break 
	else: 
		print("incorrect credentials try again") 
