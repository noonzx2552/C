import random
ans = int(input("type : "))
round = 0
if 0 <= ans < 1000000:
    while True:
        round += 1
        if round >= 10000:
            print("เดาไม่ถูก")
            break
        elif ans < 10000:
            bot = random.randrange(0,10000)
            print(bot)
            if ans == bot:
                ans = str(ans).zfill(4)
                print(f"คำตอบคือ {ans} เดาไปทั้งหมด {round} รอบ ")
                break
        elif 9999 < ans < 100000:
            bot = random.randrange(9999,100000)
            print(bot)
            if ans == bot:
                ans = str(ans).zfill(5)
                print(f"คำตอบคือ {ans} เดาไปทั้งหมด {round} รอบ")
                break
        elif 99999 < ans < 1000000:
            bot = random.randrange(99999,1000000)
            print(bot)
            if ans == bot:
                ans = str(ans).zfill(6)
                print(f"คำตอบคือ {ans} เดาไปทั้งหมด {round} รอบ")
                break
else:
    print("error!")