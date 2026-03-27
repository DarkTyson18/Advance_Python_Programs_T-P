#30. Define a function that accepts 2 values and return its sum, subtraction and multiplication.
def func(a,b):
    return a+b,a-b,a*b

x,y,z = func(10,20)
print("Sum of two number : ",x)
print("Subtarction of two number : ",y)
print("Multipication of two number : ",z)