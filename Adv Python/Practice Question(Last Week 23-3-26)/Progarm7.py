# Build a Student Record System using nested dictionaries/lists to add students, update marks,
# compute averages, and find toppers

students = {}

students["Ram"] = {"marks": [85, 90, 88]}
students["Dev"] = {"marks": [78, 82, 80]}
students["Om"] = {"marks": [92, 95, 94]}

#add
students["Bob"]={"marks":[80, 85, 88]}
print(students)

#Update
students["Dev"]["marks"] = [1,2,3]
print(students)

print("\nAverages:")
averages = {}
for name in students:
    marks = students[name]["marks"]
    avg = sum(marks) / len(marks)
    averages[name] = avg
    print(name, "Average =", avg)


topper = ""
highest = 0

for name in averages:
    if averages[name] > highest:
        highest = averages[name]
        topper = name


print("\nTopper:", topper, "with average", highest)

