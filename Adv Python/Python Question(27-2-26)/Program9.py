#41. What does function returns by default in Python?
# <ans>  -- In Python, a function that does not have an explicit return statement, or uses return without a value, 
# automatically and implicitly returns the special value None

#42. Write a program in Python to display the Factorial of a number using if else statement?
fact=1
num = int(input("Enter the number to find the factorial : "))
for i in range(1,num+1):
    fact = fact * i

print(f"factorial of {num} is : ",fact)

print("\n")
#43. Write a Python program to reverse a number.
def RevNumb(num):
    return int(str(num)[::-1])

num = int(input("Enter the number : "))
print(f"before reverse {num} after reverse ",RevNumb(num))

print("\n")
#44. Write a program to print n natural number in descending order using a while loop.
num=int(input("Enter the n Natural number : "))
i=num
while(i>0):
    print(i,end=" ")
    i=i-1

print("\n")
#45. Write a program to display the first 7 multiples of 7.
num=7
i=1
print("7 Multiples of  7 are :")
while i<=num:
    print(num*i,end=" ")
    i=i+1