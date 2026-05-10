count = 0
counter = 0
for score in range(10):
    score = int(input("Enter the scores: "))

   
    if score <= 45:
        count += 1 
    elif score > 45:
        counter += 1
print(count,"is Less than 45")
print(counter, "is greater than 45")
    
