"""word = ("Practice")
for char in reversed(word):
    print(char, end=(" "))
    """
    
word = "practice"
reversed_word = ""
    
for character in word:
    reversed_word = character + reversed_word 
print(reversed_word)



