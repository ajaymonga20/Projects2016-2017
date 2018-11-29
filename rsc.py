#FUNCTIONS

#INPUT FOR SPLIT

def split(): 
	input = ("enter your distance")

def split2(): 
	input = ("Enter your time ")

#INPUT FOR TIME
def time():
	input = ("Enter your split")

def time2():
	input = ("Enter your distance") 

#INPUT FOR DISTANCE
def distance(): 
	input = ("Enter your split")

def distance2(): 
	input = ("Enter your time")

#MAIN CODE

split()  

enter = raw_input("What do you want to calcualte? ")   

if (enter == "split"): 
	print split() 
	split2() 
elif (enter == "time"): 
	time1() 
	time2()  
elif (enter == "distance"): 
	distance1() 
	distance2()

#else: 
	#print ("Invalid entry, please type, split, distance or time") 
 
