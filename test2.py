number = int(input("Enter an integer: "))
if number > 0:
    sign = "Positive"
elif number < 0:
    sign = "Negative"
else:
    sign = "Zero"
if number % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"
if number % 3 == 0:
    divisible_3 = "Yes"
else:
    divisible_3 = "No"
if number % 5 == 0:
    divisible_5 = "Yes"
else:
    divisible_5 = "No"

if number % 3 == 0 and number % 5 == 0:
    both = "Yes"
else:
    both = "No"

print(f"Number: {number}")
print(f"Type: {sign}")
print(f"Even or Odd: {even_odd}")
print(f"Divisible by 3: {divisible_3}")
print(f"Divisible by 5: {divisible_5}")
print(f"Divisible by both 3 and 5: {both}")