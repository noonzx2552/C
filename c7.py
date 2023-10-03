import math
x = int(input("ความยาวรอบรูป:"))
bm = 0
sm = 0
undoor = x-2
a = undoor/3
loop =math.ceil(a)
for i in range(loop):
    bm += 2
    sm += 3

print(f"bm:{bm}")
print(f"sm:{sm}")
#if80 loop26 
#if100 loop33
