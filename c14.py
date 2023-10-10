import random
round = 0
if 1000 <= ans < 1000000:
    while True:
        bot = random.randrange(9999,1000000)
        round += 1
        print(bot)
        if round >= 10000:
            print("เดาไม่ถูก")
            break
        elif bot == ans:
            print(f"คำตอบคือ : {ans} สุ่มไป {round} รอบ")
            break
else:
    print("error!")