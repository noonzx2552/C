fight = input(("เชียงใหม่/ภูเก็ต: "))
level = input(("economy/business: "))
food = input(("oneway/return: "))
total = 0
if level == "economy":
    if fight == "เชียงใหม่":
        if food == "oneway":
            total += 1500 + 300
        elif food == "return":
            total += 2800 + 500
        else:
            print("error")
    elif fight == "ภูเก็ต":
        if food == "oneway":
            total += 1200 + 300
        elif food == "return":
            total += 2000 + 500
        else:
            print("error")
elif level == "business":
    if fight == "เชียงใหม่":
        if food == "oneway":
            total += 2800
        elif food == "return":
            total += 5000
        else:
            print("error")
    elif fight == "ภูเก็ต":
        if food == "oneway":
            total += 2200
        elif food == "return":
            total += 4000
        else:
            print("error")
else: 
    print("error")  

print(f"ยอดใช้จ่ายรวมของคุณ {total} บาท")