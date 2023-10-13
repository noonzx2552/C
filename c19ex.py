n = int(input("type : "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(2):
    for j in range(n - 1):
        print(" ", end="")
    print("***")
