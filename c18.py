a = int(input("type : "))
print("----------A----------")
for i in range(a,0,-1):
    for j in range(i,0,-1):
        print("*", end="")
    print()
print("----------B----------")
for i in range(a):
    for j in range(i):
        print(" ", end="")
    
    for k in range(a - i):
        print("*", end="")
    print()
print("----------C----------")
for i in range(a,0,-1):
    for j in range(i,0,-1):
        print("*", end="")
    print()