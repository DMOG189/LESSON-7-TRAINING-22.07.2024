# TRAINING 2 LOOP

# LOOP EX:

# 1. Display all natural numbers from 1 to top (inclusive)
# 2. Display all integers between two numbers (inclusive) in ascending order
# 3. Display all even numbers from 0 to n (inclusive)
# 4. Display all natural numbers up to max (inclusive) that are divisible by den

# START

# 1. Display all natural numbers from 1 to top (inclusive)
print("Exercise 1:")
top = int(input("Enter a natural number (positive integer) for 'top': "))

for i in range(1, top + 1):
    print(i, end=" ")
print("\n" + "="*50 + "\n")

# 2. Display all integers between two numbers (inclusive) in ascending order
print("Exercise 2:")
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1, num2 + 1):
    print(i, end=" ")
print("\n" + "="*50 + "\n")

# 3. Display all even numbers from 0 to n (inclusive)
print("Exercise 3:")
n = int(input("Enter a natural number (positive integer) 'n': "))

for i in range(0, n + 1, 2):
    print(i, end=" ")
print("\n" + "="*50 + "\n")

# 4. Display all natural numbers up to max (inclusive) that are divisible by den
print("Exercise 4:")
max_num = int(input("Enter the maximum number (natural number) 'max': "))
den = int(input("Enter the divisor 'den': "))

for i in range(den, max_num + 1, den):
    print(i, end=" ")
print("\n" + "="*50 + "\n")

# END