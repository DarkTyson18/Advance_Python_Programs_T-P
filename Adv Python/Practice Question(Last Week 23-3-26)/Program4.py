# Create a student marks dictionary, then add, update, delete entries, and display keys, values,and items.
marks_of_student={'s1':'50','s2':'60','s3':'70','s4':'80','s5':'90','s6':'100'}
print(marks_of_student)

#adding
marks_of_student['s7']=85
print(marks_of_student)

#update
marks_of_student.update({'s1':'55',})
print(marks_of_student)

#delete
del marks_of_student['s4']

# Display results
print("\nUpdated dictionary:", marks_of_student)
print("Keys:", marks_of_student.keys())
print("Values:", marks_of_student.values())
print("Items:", marks_of_student.items())