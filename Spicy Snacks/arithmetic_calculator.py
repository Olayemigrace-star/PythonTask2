num_one = float(input("Enter the first value: "))
num_two = float(input("Enter the Second value: "))
operator = input("Enter the Arithmetic Operator You want to make use of,(+, -, *, /): ")
add = num_one + num_two
subtract = num_one - num_two
multiply = num_one * num_two
divide = num_one / num_two

if operator == "+":
    print(add)
if operator == "-":
    print(subtract)
if operator == "*":
    print(multiply)
if operator == "/":
    print(divide)
    



