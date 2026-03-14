#excepthook(value,type,traceback)
#In Python, excepthook is a function that the interpreter calls when an exception is 
#raised and not caught by any try...except block.

# #exc_type: The exception type.
# exc_value: The exception value, which can be None.
# exc_traceback: The exception traceback, which can be None


try:
    a=0
    b=0
    div=a/b
    print(div)
except ZeroDivisionError as var:
    print(var.__class__)
    print("no issue")

#why we should not write complete code in try block
#ans. if code base is large then it may raise multiple error 

