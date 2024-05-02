# Lesson 3: Assignments | Python Lists

# 1. Python List Transformation

# Task 1: Given the list of grades. Sort the grades in descending order and display the sorted list.

# Option 1.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)
print(grades)

# Option 2.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_list = sorted(grades, reverse = True)
print(sorted_list)

# Option 3.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades = list(reversed(grades))
print(grades)

# Option 4.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades[::-1])

# Task 2: Calculate the average grade and display it.

average = sum(grades) / len(grades)
print(f'The average grade is{average: .0f}.')

# 2. Advanced List Methods and Identity Operators

# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find out which students both submitted their assignments and attended the class.

# Option 1.

for student in submitted:
    if student in attended:
        print(f'{student} both submitted their assignment and attended the class.')

# Option 2.

for student in submitted:
    for attendee in attended:
        if attendee == student:
            print(f'{attendee} both submitted their assignment and attended the class.')

# 3. Advanced Slicing Techniques

# Problem Statement: You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 
                93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 1. Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). 

# Option 1. Expected Outcome: 83, 85, 86, 87, 88, 89, 90:

# 1a:

temperatures_second_week = ', '.join(str(t) for t in temperatures[7:14])
print(temperatures_second_week)

# 1b:

extracted_temperatures = []

for t in temperatures[7:14]:
    extracted_temperatures.append(str(t))
second_week_temperatures = ', '.join(extracted_temperatures)
print(second_week_temperatures)

# Option 2. Expected Outcome is [83, 85, 86, 87, 88, 89, 90]:

# 2a:

print(temperatures[7:14])

# 2b:

temperatures_second_week = []

for i in range(7, 14):
    temperatures_second_week.append(temperatures[i])
print(temperatures_second_week)

# Task 2: Extract all the temperatures above 100. **hint** add the temperatures over 100 to a new list.

# Option 1. Slices

high_temperatures = temperatures[-6:]
print(high_temperatures)

# Option 2. New_list.append()

high_temperatures = []

for t in temperatures:
    if t > 100:
        high_temperatures.append(t)
print(high_temperatures)

# Option 3. List comprehension.

high_temperatures = [t for t in temperatures if t > 100]
print(high_temperatures)