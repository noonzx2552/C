x = int(input("x:"))
if x < 50:
    print("error!")
elif x > 200:
    print("error")
else:
    y = x-50
    total = y*6+100
    print(total)