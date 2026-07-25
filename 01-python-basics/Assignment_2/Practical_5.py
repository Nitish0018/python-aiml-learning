n = int(input("Enter a number: "))

def sum_digit(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

print("Sum of digits", sum_digit(n))



'''
How it works
n % 10 gets the last digit.

sum += digit adds the digit to the total.

n = n // 10 removes the last digit.

The loop continues until n becomes 0.
'''