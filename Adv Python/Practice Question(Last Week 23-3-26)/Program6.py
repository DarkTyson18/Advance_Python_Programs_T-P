# Convert a mixed-type tuple to a list, remove integers less than 10, and convert back to a
# tuple


t1 = (5, "hello", 12, 3.5, 8, 20, "world")


lst = list(t1)


li = [x for x in lst if not (type(x) == int and x < 10)]


t_new = tuple(li)

print("Original tuple:", t1)
print("Modified tuple:", t_new)