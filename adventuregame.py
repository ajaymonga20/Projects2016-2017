# Make your own choose your own adventure game 


print("WELCOME TO MY CHOOSE YOUR OWN ADVENUTRE GAME") 
print("                                               ") 
print("It is a wednesday morning and you arrive at school at 7:30am") 
print("              ") 
print("Where do you go?")  
morning = raw_input("A - Go to the Student Centre, B - Go To The Gym, C - Leave the school: ")
if (morning == "A"): 
	print("What do you want to do in the student centre?") 
	centre = raw_input("A - Game, B - Do work, C - Watch Netflix: ") 
elif (morning == "B"): 
	print("Do you want to workout or just play sports?")
	gym = raw_input("A - workout, B - Just play sports: ")  
elif (morning == "C"):   
	print("Where do you wanna go?")
	leave = raw_input("A - The Village, B - Downtown, C - Outside of the country: ") 
else: 
	print("You Must Type A, B or C") 

if (centre == "A"): 
	print("You Should Probably Be More Productive") 
elif (centre == "B"):
	print("Sounds good but you might want to go to the library, so you aren't sucked into the gaming world") 
elif (centre == "C"): 
	print("White Collar is a good show, you should watch it")
else: 
	print("You Must Type A, B or C")  
