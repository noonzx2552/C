r = int(input("radius:"))
rpm = int(input("RPM:"))

r_inch = 2*r*22/7 
cm = r_inch * 2.54 * rpm
km = cm / 100000
kmperhr = km * 60
    
print(kmperhr)
