# Rowing split calculator APP - AJAY MONGA - Sunday, Feburary 26, 2017 

# Imports - nothing

# Functions 

'''def calc(what): #Chooses what to calculate   
	if(what == "split"): 
		time = int(input("enter your time "))
		distance = int(input("enter your distance ")) 
		ajay = ((500 * (time / distance)) * 60)
		ajay = str(ajay)
		print[-2:]     
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
'''

what = input("what do you wanna calculate? ") # User input for what they wanna calculate 

if(what == "split"): 
	time = int(input("enter your time "))
	distance = int(input("enter your distance ")) 
	ajay = ((500 * (time / distance)))
	ajay = str(round(ajay, 2))
#	number_string = str(ajay)
#	nose = print(number_string[-2:])
#	string_number = float(ajay) 
	#print ((nose * 60) + string_number)
	#print(ajay)
	number_string = str(ajay)
	nose = (number_string[-2:])
	string_number = str(ajay)
	goat = (string_number[:1]) 
	string_number = float(ajay) 
	#string_number = float(ajay)
	print (float(nose) * 0.006 + float(goat) * 1 )
	#ear = str(totalsplit) 
	#print (ear[:1] + ":" + ear[-3:]) 




'''
elif(what == "distance"): 
	print("calculating distance") 
elif(what == "time"):
	print ("calculating time") 
else:
	print ("invalid entry, please type split, time or distance") 
#print (calc(what)) # prints split
#print(split)

number_string = str(ajay)
nose = print(number_string[-2:])
string_number = float(ajay) 
print (ajay) 
print ((number_string * 60) + string_number)
 
''' 







