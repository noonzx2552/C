import math
views = int(input("view: "))
days = int(input("days:"))

for day in range(days + 1):
    likes_and_shares = math.ceil(views/2)
    friends_shared = likes_and_shares * 3
    
    print(f"วันที่ {day}: share {likes_and_shares} / view {friends_shared}")
    
    views += friends_shared