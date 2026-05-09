num_one = int(input("Enter the first number: "))
num_two = int(input("Enter the second number: "))
num_three = int(input("Enter the third number: "))

largest = num_one

if num_two > largest:
    largest = num_two
if num_three > largest:
    largest = num_three    
    
print("The largest Number is ", largest)
