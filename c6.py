prime = int(input("primenumber:"))

if prime == 1:
    print("ไม่เป็นจำนวนเฉพาะ!")
elif prime == 2:
    print("เป็นจำนวนเฉพาะ")
else:
    is_prime = True
    for i in range(2, prime):
        if prime % i == 0:
            is_prime = False
            break

    if is_prime:
        print("เป็นจำนวนเฉพาะ")
    else:
        print("ไม่เป็นจำนวนเฉพาะ")