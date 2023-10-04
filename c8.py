import math
views = int(input("view: "))
days = int(input("days:"))
total = 0
likeandshare = 0
newviewer = views
for i in range(1,days+1):
    likeandshare = math.ceil(newviewer/2)
    total += likeandshare
    newviewer = likeandshare * 3

    print(f"day: {i} likeandshare: {likeandshare} newviewer: {newviewer} ")
print(f"total: {total}")