def even(a,b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print (i)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
even(a,b)