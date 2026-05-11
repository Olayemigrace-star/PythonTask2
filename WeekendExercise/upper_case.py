word = input("Enter any word to count the Capital letters in it: ")
count = 0
for char in word:
    if char.isupper():
        count += 1

print(count)
