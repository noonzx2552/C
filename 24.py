day =  int(input("day: "))
room = input("standard/dulux: ")
total = 0
if room == "standard":
    if 4 > day:
        total += 1000+100 * day
    else:
        total += 800+100 * day
elif room == "dulux":
    if 4 > day:
        total += 1800+100 * day
    else:
        total += 1500+100 * day    
else:
    print("error")

print(f"คุณต้องจ่ายทั้งหมด {total} บาท")    