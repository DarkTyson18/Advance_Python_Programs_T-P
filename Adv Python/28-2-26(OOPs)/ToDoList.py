#add tasks, set deadlines, assign priority, and filter by project or tag
class ToDo:
    def __init__(self, task, deadline, priority, project=None, tag=None):
        self.task = task
        self.deadline = deadline
        self.priority = priority
        self.project = project
        self.tag = tag
        
    def display(self):
        print("task:", self.task)
        print("Deadline:", self.deadline)
        print("Priority:", self.priority)
        print("Project:", self.project)
        print("Tag:", self.tag)
        
tasks = []
print("\n Warehouse automation system")
#td = ToDo()
while True: 
    print("1. Make Your Schedule")
    print("2. filter by project")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        task = input("Enter your task:")
        deadline = input("Enter your deadline:")
        priority = input("Enter your priority (High/Medium/Low):")
        tag = input("Enter your tag:")

        obj = ToDo(task, deadline, priority, tag)
        tasks.append(obj)
        print("\nTask Added Successfully")

    elif choice==2:
        filter_tag = input("Enter tag to filter: ")
        print("\nFiltered by Tag:")
        for t in tasks:
            if t.tag == filter_tag:
                t.display()
            else:
                print("for given tag, No such list is found")

    elif choice==3:
        break

    else:
        print("Invalid Input")