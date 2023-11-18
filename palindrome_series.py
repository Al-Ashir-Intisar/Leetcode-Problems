import math
def is_palindrome(num):
    # Convert the number to a string and check if it reads the same backward
    return str(num) == str(num)[::-1]

def generate_palindromes(limit):
    palindromes = []
    for i in range(limit):
        if is_palindrome(i):
            palindromes.append(i)
    return palindromes

# Example: Generate palindromes up to 1000
limit = 1000
palindrome_series = generate_palindromes(limit)
#print("Palindromes up to {}: {}".format(limit, palindrome_series))

