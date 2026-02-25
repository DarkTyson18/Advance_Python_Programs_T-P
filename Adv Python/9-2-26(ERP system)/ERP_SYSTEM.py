
students = {}

courses = {}

enrollments = {}

attendance = {}


while True:
    print("\n------ STUDENT MANAGEMENT SYSTEM ------")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Enroll Student in Course")
    print("4. Mark Attendance")
    print("5. View Enrolled Students")
    print("6. View Attendance Percentage")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    #ADD STUDENT
    if choice == 1:
        sid = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        students[sid] = name
        print("Student added successfully")

    #REMOVE STUDENT
    elif choice == 2:
        sid = int(input("Enter student ID to remove: "))
        if sid in students:
            del students[sid]

            # Remove from enrollments and attendance
            for cid in enrollments:
                if sid in enrollments[cid]:
                    enrollments[cid].remove(sid)
                    del attendance[cid][sid]

            print("Student removed successfully")
        else:
            print("Student not found")

    # ENROLL STUDENT
    elif choice == 3:
        sid = int(input("Enter student ID: "))
        cid = int(input("Enter course ID: "))

        if sid in students and cid in courses:
            enrollments[cid].append(sid)
            attendance[cid][sid] = []
            print("Student enrolled successfully")
        else:
            print("Invalid student or course")

    #MARK ATTENDANCE
    elif choice == 4:
        cid = int(input("Enter course ID: "))
        sid = int(input("Enter student ID: "))

        if cid in attendance and sid in attendance[cid]:
            status = input("Present? (yes/no): ")
            if status == "yes":
                attendance[cid][sid].append(True)
            else:
                attendance[cid][sid].append(False)
            print("Attendance marked")
        else:
            print("Student not enrolled in course")

    #VIEW ENROLLED STUDENTS
    elif choice == 5:
        cid = int(input("Enter course ID: "))
        print("\nStudents enrolled in", courses[cid])

        for sid in enrollments[cid]:
            print(sid, "-", students[sid])

    #ATTENDANCE PERCENTAGE
    elif choice == 6:
        cid = int(input("Enter course ID: "))
        print("\nAttendance Percentage for", courses[cid])

        for sid in attendance[cid]:
            total = len(attendance[cid][sid])
            present = attendance[cid][sid].count(True)

            if total == 0:
                percent = 0
            else:
                percent = (present / total) * 100

            print(students[sid], ":", percent, "%")

    #EXIT
    elif choice == 7:
        print("Exiting system...")
        break

    else:
        print("Invalid choice")
