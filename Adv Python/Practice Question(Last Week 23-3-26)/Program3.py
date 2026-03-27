# Filter numeric values from a mixed-type tuple, attempt modification (handle error), and
# concatenate two tuples.

t1 = (10, "hello", 3.5, True, 7, "world", 2.8)

nums = tuple(x for x in t1 if type(x) in (int, float))
print("Numbers:", nums)

try:
    t1[0]=100
except:
    print("can't modify the tuple")


t2 = (100, 200)
print("Concatenated:", t1 + t2)