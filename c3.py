import math
tree = int(input("highttree:"))
season = int(input("season:"))
loop = math.floor(season/2)
sas = season % 2 
#---------------------------------------#
for i in range(loop):
    tree += 1
    tree += tree

if sas == 1:
    tree = tree + 1
else:
    tree = tree
#--------------------------------------#
print(tree)