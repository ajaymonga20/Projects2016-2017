def calculator(count1, count2, count3, count4):
    return  count1 + count2 + count3 + count4

count = 0

bur = input (" Please enter a burger choice ")
side = input ( " Please enter a side order choice ")
drink = input ( " Please enter a drink choice ")
dessert = input ( " Please enter a dessert choice ")

bur = int(bur)
side = int(side)
drink = int(drink)
dessert = int(dessert)



if bur == 1:
    count = 461
elif bur == 2:
    count = 431
elif bur == 3:
    count = 420
elif bur == 4:
    count = 0

if side == 1:
    count = count + 100
elif side == 2:
    count = count + 57
elif side == 3:
    count2 = count + 70
elif side == 4:
    count2 = count + 0

if drink == 1:
    count3 = 130
elif drink == 2:
    count3 = 160
elif drink == 3:
    count3 = 118
elif drink == 4:
    count3 = 0

if dessert == 1:
    count4 = 167
elif dessert == 2:
    count4 = 266
elif dessert == 3:
    count4 = 75
elif dessert == 4:
    count4 = 0


countt = count + count 2 + count3 + count4

print (calculator(count1,count2,count3,count4))


























