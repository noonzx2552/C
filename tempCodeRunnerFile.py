import math
tree = int(input("highttree:"))
season = int(input("season:"))
loop = math.floor(season/2)
sas = season % 2 
total = 0
for i in range(loop):
    total += 1
    total += 2 * season  

if sas == 1:
    total += 1
else:
    total += 0
print(total)