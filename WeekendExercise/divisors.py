digit = int(input("Enter any number to see it divisors: "))

number = 1
while(number <= digit):
    if digit % number == 0:
        print("The factors are ", number)
        
    number += 1




