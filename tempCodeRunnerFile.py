import math 
#w กว้าง h ยาว
w = int(input("W:"))
h = int(input("H:"))
L = 0
S = 0
ribbon = 2(w+h)
a = (ribbon-2)/3
loop =math.ceil(a)
for i in range(loop):
    L += 2
    S += 3

print(f"เสาใหญ่:{L}")
print(f"เสาเล็ก:{S}")