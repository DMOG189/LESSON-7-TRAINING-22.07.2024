# TRAINING 1 TERMS

# TERMS:

# 1. Print the smaller number three times
# 2. Print the average of two integers
# 3. Print the largest of three numbers
# 4. Convert movie duration from minutes to hours and minutes
# 5. Print the rightmost digit of a 4-digit number
# 6. Print the second rightmost digit of a 4-digit number
# 7. Print the sum of the digits of a 2-digit number
# 8. Reverse the digits of a 2-digit number
# 9. Check if a number is even or odd
# 10. Calculate income tax based on salary
# 11. Check if a person can ride a roller coaster based on age and height

# START

# 1. Print the smaller number three times
print("Exercise 1:")
num1 = float(input("Enter the first decimal number: "))
num2 = float(input("Enter the second decimal number: "))
smaller_number = min(num1, num2)
print(smaller_number)
print(smaller_number)
print(smaller_number)
print("\n" + "="*50 + "\n")

# 2. Print the average of two integers
print("Exercise 2:")
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
average = (num1 + num2) / 2
print("The average is:", average)
print("\n" + "="*50 + "\n")

# 3. Print the largest of three numbers
print("Exercise 3:")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest_number = max(num1, num2, num3)
print("The largest number is:", largest_number)
print("\n" + "="*50 + "\n")

# 4. Convert movie duration from minutes to hours and minutes
print("Exercise 4:")
minutes = int(input("Enter the movie duration in minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{hours} hour(s) and {remaining_minutes} minute(s)")
print("\n" + "="*50 + "\n")

# 5. Print the rightmost digit of a 4-digit number
print("Exercise 5:")
number = int(input("Enter a 4-digit number: "))
rightmost_digit = number % 10
print("The rightmost digit is:", rightmost_digit)
print("\n" + "="*50 + "\n")

# 6. Print the second rightmost digit of a 4-digit number
print("Exercise 6:")
number = int(input("Enter a 4-digit number: "))
second_rightmost_digit = (number // 10) % 10
print("The second rightmost digit is:", second_rightmost_digit)
print("\n" + "="*50 + "\n")

# 7. Print the sum of the digits of a 2-digit number
print("Exercise 7:")
number = int(input("Enter a 2-digit number: "))
sum_of_digits = (number // 10) + (number % 10)
print("The sum of the digits is:", sum_of_digits)
print("\n" + "="*50 + "\n")

# 8. Reverse the digits of a 2-digit number
print("Exercise 8:")
number = int(input("Enter a 2-digit number: "))
reversed_number = (number % 10) * 10 + (number // 10)
print("The reversed number is:", reversed_number)
print("\n" + "="*50 + "\n")

# 9. Check if a number is even or odd
print("Exercise 9:")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")
print("\n" + "="*50 + "\n")

# 10. Calculate income tax based on salary
print("Exercise 10:")
income = float(input("Enter your monthly salary: "))
tax = 0
if income > 50000:
    tax += (income - 50000) * 0.51
    income = 50000
if income > 35000:
    tax += (income - 35000) * 0.45
    income = 35000
if income > 25000:
    tax += (income - 25000) * 0.40
    income = 25000
if income > 18000:
    tax += (income - 18000) * 0.30
    income = 18000
if income > 12000:
    tax += (income - 12000) * 0.20
    income = 12000
if income > 6000:
    tax += (income - 6000) * 0.10
print("Your tax is:", tax)
print("\n" + "="*50 + "\n")

# 11. Check if a person can ride a roller coaster based on age and height
print("Exercise 11:")
age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))
if (8 <= age <= 18 and height > 115) or (age > 18 and height > 100):
    print("You are allowed to ride the roller coaster.")
else:
    print("You are not allowed to ride the roller coaster.")
print("\n" + "="*50 + "\n")

# END