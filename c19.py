x = int(input("type : "))
for i in range (x,0,-2):
    for j in range ((x-i) // 2):
        print(" ", end="")

    for k in range(i):
        print("*", end="")
    print()