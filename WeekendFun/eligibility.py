total_bill = float(input("What is your Total Bill: "))
is_member = (input("Are you a Member, \"Yes\" or \"No\": "))

if total_bill >= 1000:
    if is_member == "Yes":
        print("10% Off")
    else:
        print("5% Off")        
else:
    print(total_bill, "No Discount")
