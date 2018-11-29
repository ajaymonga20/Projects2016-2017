

def to_calc(split, distance, time ):  
	if (split == "yes" or distance == "no" or time == "no"):
		return True  
	elif (split == "no" or distance == "yes" or time == "no"):
		return True 
	elif (split == "no" or distance == "no" or time == "yes"):     
 		return False   


split = raw_input("Do you want to calculate split? (type yes, or no ): ") 
distance = raw_input("Do you want to calculate distance? (type yes, or no ): ")  
time = raw_input("Do you want to calculate time? (type yes, or no ): ")  

#def to_calc2():  

calc = to_calc(split, distance, time) 
 

if (calc == True): 
	print var1 and var2
else: 
	print var3


var1 = split2 = raw_input("Do you want to calcualte split (type yes, or no ): ")
var2 = distance2 = raw_input("Do you want to calculate distance (type yes, or no): ")
var3 = time2 = raw_input("what is your split?" ) 

#split2 = raw_input("Do you want to calcualte split (type yes, or no ): ") 
#distance2 = raw_input("Do you want to calculate distance (type yes, or no): ")  

#time2 = raw_input("what is your split?" ) 


calc = to_calc(split, distance, time)  


def to_calc2():  
	if (calc == True): 
		return split2 and distance2  
	else: 
		return 
			


#calc2 = to_calcxx

###if (calc == True): 
	return    


#def calc1(split, distance): 
	

#def calc2(split, time): 

#def calc3(time, distance): 

'''

split = 500 * distance / time
distance = (time/split) * 500
split = 500 * (time/distance)
time = split * (distance/500)
 
''' 
