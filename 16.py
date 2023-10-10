num = int(input("type:"))
final = num
round = 0
s = ''
while True:
    a = num % 16
    num = num // 16
    round += 1
    if a < 10:
        s = str(a) + s
    elif a == 10:
        s = "A" + s
    elif a == 11:
        s = "B" + s
    elif a == 12:
        s = "C" + s
    elif a == 13:
        s = "D" + s
    elif a == 14:
        s = "E" + s
    elif a == 15:
        s = "F" + s
    if num < 16:
        break
s = str(num) + s
print(s)