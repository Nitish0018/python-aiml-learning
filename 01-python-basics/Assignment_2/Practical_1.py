salary = float(input("enter your salary: "))

if salary < 30000:
    tax = salary * 0.5
elif salary <= 70000:
    tax = salary * 0.15
else:
    tax = salary * 0.25
print("salary",salary)
print("tax",tax)