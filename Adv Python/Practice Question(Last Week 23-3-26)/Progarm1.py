# Write a program that takes two integers, computes their sum, difference, product, and
# division, checks if they’re even/odd, and converts one to a float.


a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))


print("\nSum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)


if b != 0:
    print("Division =", a / b)
else:
    print("Division not possible (division by zero)")


if a % 2 == 0:
    print(a, "is Even")
else:
    print(a, "is Odd")

if b % 2 == 0:
    print(b, "is Even")
else:
    print(b, "is Odd")


converted = float(a)
print("\nFloat value of first number =", converted)