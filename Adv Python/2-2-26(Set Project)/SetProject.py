Entered_stu=set()
Entered_date_time=set()
Rejected_stu=set()


n=int(input("Enter the number of individual you want to enter : "))

for i in range(1,n+1):
    name = input("Enter the name : ")
    
    new_name=name.lower()
    if new_name in Entered_stu:
        print("Name already exist, Enter another name : ")
        new_name=name.upper()
        Rejected_stu.add(new_name)

    else:
       date=input("Input date and time in format - dd/mm/yy - 00:00 PM/AM ")
       Entered_date_time.add(date)
       Entered_stu.add(new_name)


print("Entered people : ",Entered_stu)
print("Entered date-time : ",Entered_date_time)

print("\nrejected people : ",Rejected_stu)

#name in lower case and remove whitespaces and input data-time 


#string function-
#remove() - remove the element if present but, give error if not present.
#discard() - didn't give error if element is not present

#print("Entered people : ",Entered_stu)
#print("Entered date : ",Entered_date_time)