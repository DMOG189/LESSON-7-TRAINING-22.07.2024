# TRAINING 3 DATA PROCESS

# DATA PROCESS:

# 1. Sum numbers until -99 is entered
# 2. Find the highest and lowest numbers until a negative number or 0 is entered
# 3. Display the index of the highest number among 5 inputs
# 4. Multiply two numbers using addition only
# 5. Raise a number to a power using multiplication only
# 6. Check if a digit appears in a number
# 7. Find the greatest common divisor (GCD) of two numbers
# 8. Check if a number is prime

# START

# 1. Sum numbers until -99 is entered
print("Exercise 1:")
total_sum = 0
first_input = True

while True:
    num = int(input("Enter a number (enter -99 to stop): "))
    if num == -99:
        if first_input:
            total_sum = None
        break
    total_sum += num
    first_input = False

print("Sum of the numbers:", total_sum)
print("\n" + "="*50 + "\n")

# 2. Find the highest and lowest numbers until a negative number or 0 is entered
print("Exercise 2:")
first_input = True
highest = None
lowest = None

while True:
    num = int(input("Enter a number (enter a negative number or 0 to stop): "))
    if num <= 0:
        if first_input:
            highest = None
            lowest = None
        break
    if first_input:
        highest = lowest = num
        first_input = False
    else:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

print("Highest number:", highest)
print("Lowest number:", lowest)
print("\n" + "="*50 + "\n")

# 3. Display the index of the highest number among 5 inputs
print("Exercise 3:")
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

highest_index = numbers.index(max(numbers)) + 1
print("The highest number was entered at position:", highest_index)
print("\n" + "="*50 + "\n")

# 4. Multiply two numbers using addition only
print("Exercise 4:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

product = 0
for _ in range(abs(num2)):
    product += abs(num1)

if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
    product = -product

print("The product of the two numbers is:", product)
print("\n" + "="*50 + "\n")

# 5. Raise a number to a power using multiplication only
print("Exercise 5:")
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1
for _ in range(abs(exponent)):
    result *= base

if exponent < 0:
    result = 1 / result

print(f"{base} raised to the power of {exponent} is: {result}")
print("\n" + "="*50 + "\n")

# 6. Check if a digit appears in a number
print("Exercise 6:")
number = input("Enter a number: ")
digit = input("Enter a digit to check: ")

if digit in number:
    print("True")
else:
    print("False")
print("\n" + "="*50 + "\n")

# 7. Find the greatest common divisor (GCD) of two numbers
print("Exercise 7:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(f"The greatest common divisor of {num1} and {num2} is: {gcd(num1, num2)}")
print("\n" + "="*50 + "\n")

# 8. Check if a number is prime
print("Exercise 8:")
num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# END