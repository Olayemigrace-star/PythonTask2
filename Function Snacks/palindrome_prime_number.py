'''def check_if_number_is_palindrome(number):

    original = number
    remainder = 0
    value = 1
    while number > 0:
        value = number % 10
        remainder = (remainder * 10) + value
        number //= 10


    return remainder == original
    
print(check_if_number_is_palindrome(121)) '''   


def check_if_a_number_is_a_prime_number(number):
    while number < 2:
        if  i % number == 0:
            return false
    number += 1

    return number
print(check_if_a_number_is_a_prime_number(17))

