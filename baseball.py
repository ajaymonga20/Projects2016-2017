# AJAY MONGA - BASEBALL ANALYTICS EQUATION - APRIL 9, 2017 

def calculate(bb, k, h, hbp, ibb, gdp):
	#return (bb + 0.00) and (k + 0.00) and (h + 0.00) and (hbp + 0.00) and (ibb + 000) and (gdp + 0.00) 
	#return ((bb-k) + (h-k) + hbp + ibb) / gdp
	return (((bb + 0.00) - (k + 0.00)) + ((h + 0.00) - (k + 0.00)) + (hbp + 0.00) + (ibb + 0.00)) / (gdp + 0.00) 

bb = input("Enter walks ") 
k = input("Enter Strikeouts ") 
h = input("Enter hits ") 
hbp = input("Enter hit by pitches ") 
ibb = input("Enter intentional walks ") 
gdp = input("Enter double plays grounded into ") 

print calculate(bb, k, h, hbp, ibb, gdp) 
  
