x = int(input("type : "))
for i in range(1, x+1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("#---------------------#")
for i in range(x,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
print("#---------------------#")
for i in range(1,x+1):
  for j in range(x - i):
    print(" ",end=" ")
  for j in range(1,i + 1):
    print(j,end=" ")
  print()