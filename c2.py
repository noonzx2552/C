r = int(input("radius:"))
rpm = int(input("RPM:"))

r_inch = 2*r*22/ 7 
cmpermin = r_inch * 2.54 * rpm
kmperhr = 0.0006 * cmpermin
    
print(kmperhr)