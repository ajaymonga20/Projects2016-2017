
def coordinates(a,b,c,d,t):
    if(c - a) or (d - b) == t:
        return "Y"
    else:
        return "N"

a = input()
b = input()
c = input()
d = input()
t = input()

print coordinates(a,b,c,d,t)


