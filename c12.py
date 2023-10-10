num = int(input("type:"))
d = num
round = 0
while True:
    a = num % 2
    num = num // 2
    round += 1
    if num == 1:
        break
    a = str(a)
    s = a [::-1]
    print(s,end='')
final_sas = (num*2+a)-2
print(final_sas,end='')
print("1")

#---------------------------------#
s = ''
num = d
while True:
    a = num % 16
    num = num // 16
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
if num < 10:
    s = str(num) + s
elif num == 10:
        s = "A" + s
elif num == 11:
        s = "B" + s
elif num == 12:
        s = "C" + s
elif num == 13:
        s = "D" + s
elif num == 14:
        s = "E" + s
elif num == 15:
        s = "F" + s
print(s)
