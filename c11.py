total = int(input("ใช้กี่unit:"))
balance = 0
if total < 200:
    print(f"จ่ายค่าไฟ {total*2} bath")
elif total <= 500:
    print("จ่ายค่าไฟ 400 bath")
#--------------------------------------------------#
elif total <= 3000:
    balance = total - 500
    A = ((balance*2)*0.7) + 700 
    print(f"จ่ายค่าไฟ {A} bath")
#--------------------------------------------------#
else:
    total = ((total-200)*2)*0.7+400
    print(f"จ่ายค่าไฟ {total} bath")