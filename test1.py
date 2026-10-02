name = input("Enter student name: ")

mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    result = "Pass"
else:
    result = "Fail"

print(f"Student: {name}")
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Grade: {grade}")
print("Marks:")

for mark in [mark1, mark2, mark3]:
    print(f"{mark}")

print(f"Result: {result}")