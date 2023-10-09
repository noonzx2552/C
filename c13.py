import random 
low = 0
high = 100
roud = 0

while True:
    bot = random.randint(low,high)
    roud += 1

    print(f"bot:{bot}")
    user = str(input("[high/low/correct]:"))

    if user == "correct":
        print(f"เลขของคุณคือ {bot}")
        print(f"สุ่มไป {roud} รอบ")
        break
    elif user == "high":
        high = bot - 1
    elif user == "low":
        low = bot + 1
    else:
        print("tryagain![high/low/correct]")    