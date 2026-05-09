age = int(input("Enter Your Age: "))

if age < 5:
    print("It is Free")
elif age < 13:
    print("You are Paying $5 ")
elif age < 65:
    print("You are Paying $12 ")
else:
    print("You are Paying $8 ")
