correct_pin=6025
tries=3
while tries>0:
    pin=int(input("Enter your PIN:"))
    if pin==correct_pin:
        print("Access Granted!!")
        break
    else:
        tries-=1
        print(f"Wrong PIN , {tries} attempts left!!")
else:
    print("Account Locked!!")