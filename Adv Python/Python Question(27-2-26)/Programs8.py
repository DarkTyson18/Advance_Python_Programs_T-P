#36. Define a function that accepts lowercase words and returns uppercase words.
def convertInUpper(word):

    print(f"{word} in upper case -- ",word.upper())

wrd=input("Enter thr word : ")
convertInUpper(wrd)

print("\n")
#37. Define a function that accepts radius and returns the area of a circle.
def CircleArea(radius):
    return 3.14*radius*radius

r = int(input("Enter the radius : "))
print(f"Area of circle with radius {r} is : ",CircleArea(r))

print("\n")
# 38. What is the difference between local and global variable?
# <ans>  -- Loacl variable is defined inside the method or function and cant be accessed outside it
# while, Global variable is defined outside the method and can be accessed anywhere in the program.\


#39. What is the difference between a parameter and an argument?
# <ans>  -- variable that is defined in the function definition are parameter while, 
# the value passed to the function during function call is called the arguments. 


#40. Name three iterable object in Python?
# <ans>  -- 1. list   2.tuple  3.dictionary