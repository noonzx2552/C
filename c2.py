r = int(input("radius:"))
rpm = int(input("RPM:"))

r_inch = 2*r*22/ 7 
total = 0
for i in range(rpm):
    total += r_inch
    
total = total * 0.001524
print(total)