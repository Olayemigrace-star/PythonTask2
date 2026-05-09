name = input("Enter The Name of the item: ")
#price = float(input("What is the Price of The Item: "))
code = input("Enter The Promotional code of the item: ")


def when_promotional_code_equals_save10(price):
    number = 1
    real_price = 0
    if code == "SAVE10":
        number = (10 /100) * price
        real_price = price - number
    return real_price

def when_promotional_code_equals_half_off(price):
    number = 1
    real_price = 0
    if code == "HALFOFF":
        number = (50 /100) * price
        real_price = price - number
    return real_price    
    
print(when_promotional_code_equals_save10(2000))
print(when_promotional_code_equals_half_off(5600))    
