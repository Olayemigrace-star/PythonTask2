num_one = int(input("Enter the value of \'x\': "))
num_two = int(input("Enter the value of \'y\': "))

if num_one > 0 and num_two > 0:
    print("Q1")
if num_one < 0 and num_two > 0:
    print("Q2")    
if num_one < 0 and num_two < 0:
    print("Q3")        
if num_one > 0 and num_two < 0:
    print("Q4")        
if num_one == 0 and num_two == 0:
    print("Origin")     
if num_one != 0 and num_two == 0:
    print("X-axis")         
if num_one == 0 and num_two != 0:
    print("Y-axis")         
    
    
