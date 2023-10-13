a = input("type : ")
for i in range(1, len(a) + 1):
    print(a[:i])
print("#-------------------------------#")
for i in range(1, len(a) + 1):
    print(a[::i])