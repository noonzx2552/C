total = 0
father = int(input("father : "))
mother = int(input("mother : "))
#--------------------------father----------------------#
if 7 <= father < 18:
    total += 150 * 0.7
elif father < 7:
    total += 150 * 0.2
else:
    total += 150
#--------------------------mother----------------------#
if 7 <= mother < 18:
    total += 150 * 0.7
elif mother < 7:
    total += 150 * 0.2
else:
    total += 150
#------------------------kids--------------------------#
while True:
    kid = int(input("kid[type 0 to end]"))
    if kid == 0:
        break
    elif 7 <= kid < 18:
        total += 150 * 0.7
    elif kid < 7:
        total += 150 * 0.2
    else:
        total += 150

print(total)