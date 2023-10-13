w = int(input("w: "))
h = int(input("h: "))
if w <= h:
    print(2*w-1)
elif w > h:
    print(h*2)
else:
    print("error!")