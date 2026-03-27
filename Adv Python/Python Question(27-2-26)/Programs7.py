
#31. Define a function that accepts roll number and returns whether the student is present or absent.
def check(rollno):
    if roll_no=="24CSEAIML181":
        return 1
    else:
        return 0

roll_no = input("Enter the roll no. to check whether student is present or not : ")
if(check(roll_no)):
    print(f"student - {roll_no} is present")
else:
    print("student is absent")

print("\n")
#32. Define a function in python that accepts 3 values and returns the maximum of three numbers.
def FindMax(a,b,c):
    if(a>b and a>c): return a
    elif(b>a and b>c): return b
    else: return c

print("Greater number is : ",FindMax(10,20,30))


print("\n")
#33. Define a function that accepts a number and returns whether the number is even or odd.
def CheckEvenOdd(num):
    if num%2==0: return "even"
    else: return "odd"


print("given number is : ",CheckEvenOdd(10))

print("\n")
#34. Define a function which counts vowels and consonant in a word.
def CountVowCons(words):
    vowels=0
    consonants=0
    for ch in words:
        if ch in "aeiouAEIOU":
            vowels=vowels+1
        else:
            consonants=consonants+1

    print("Total number of vowels : ",vowels)
    print("Total number of Consonants : ",consonants)

word=input("Enter the word : ")
CountVowCons(word)

print("\n")
#35. Define a function that returns Factorial of a number.
def Calfact(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i

    return fact

num = int(input("Enter the number to find the factorial : "))
print(f"factorial of {num} is : ",Calfact(num))
