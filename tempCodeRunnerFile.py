import random

def main():
    print("ยินดีต้อนรับสู่เกมทายเลข!")
    print("คุณคิดเลขไว้ในใจระหว่าง 0 ถึง 100")
    
    lower_bound = 0
    upper_bound = 100
    guess_count = 0
    
    while True:
        # บอทเดาเลข
        bot_guess = random.randint(lower_bound, upper_bound)
        guess_count += 1
        
        # แสดงเลขที่บอทเดาและถามผู้เล่น
        print(f"Bot คิดว่าเลขของคุณคือ: {bot_guess}")
        user_input = input("คำตอบของคุณ (H=too high, L=too low, C=correct): ").strip().lower()
        
        # ตรวจสอบคำตอบของผู้เล่น
        if user_input == "c":
            print(f"Bot ทายถูก! เลขของคุณคือ {bot_guess}")
            print(f"Bot ใช้เวลาทายเลข {guess_count} ครั้ง")
            break
        elif user_input == "h":
            upper_bound = bot_guess - 1
        elif user_input == "l":
            lower_bound = bot_guess + 1
        else:
            print("กรุณาป้อนคำตอบให้ถูกต้อง (H, L, C)")

if __name__ == "__main__":
    main()
