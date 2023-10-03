import math
tree = int(input("highttree:"))
season = int(input("season:"))
loop = math.floor(season/2)
sas = season % 2 
total = 0

if sas == 1:
    total += 1
else:
    total += 0
print(total)