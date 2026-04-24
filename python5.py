age=int(input("Enter your age: "))
if age>=18:
    print("you are an adult")
elif age>12 and age<18:
    print("you are a teenager")
elif age>5 and age<=12:
    print("you are a child")
elif age >2 and age<=5:
    print("you are a early child")
else:
    print("you are a baby")

