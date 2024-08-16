# TRAINING 4 COMPLEX LOOP A


# COMPLEX LOOP:

# 1. Temperature Data Collection and Analysis

# START

# 1. Temperature Data Collection and Analysis

temperatures = []

print("Enter the average temperatures for each month in 2023 (Tel Aviv):")

for i in range(12):
    while True:
        try:
            temp = input(f"Enter the temperature for month {i + 1}: ")
            temp = float(temp)

            if temp < 5 or temp > 40:
                print("data wrong")
                break

            if len(temperatures) >= 1 and temperatures[-1] == 0 and temp == 0:
                print("Two consecutive zero temperatures detected, ignoring this input.")
                continue

            temperatures.append(temp)
            break

        except ValueError:
            print("Invalid input, please enter a numeric value.")

    if len(temperatures) != i + 1:
        break

if len(temperatures) == 12:
    print("correct data")

    average_temp = sum(temperatures) / len(temperatures)
    print(f"The average temperature for 2023 is: {average_temp:.2f}°C")

    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)
    print(f"The highest temperature recorded: {highest_temp}°C")
    print(f"The lowest temperature recorded: {lowest_temp}°C")
else:
    print("Temperature data collection was incomplete.")


# END