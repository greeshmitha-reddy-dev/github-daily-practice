# Day 6 - Python For Loop
# Multiplication Table

number = int(input("Enter a number: "))

print()
print("----- Multiplication Table -----")

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)