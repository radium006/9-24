class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
    def __repr__(self):
        return "TASK: {0}, PRIORITY: {1}".format(self.title, self.priority)

print("Welcome to Kev's TODO program!")

task_list = []

def display_tasks(tasks):
    for x in tasks:
        print(x)

while True:
    choice = input("MENU: Press A to add task, R to remove, V to view, Q to quit ").lower()

    if choice == 'q':
        break
    elif choice == 'a':
        task_name = input("Type task: ")
        priority = input("Type priority: ").upper()
        task_list.append(Task(task_name,priority))
    elif choice == 'v':
        display_tasks(task_list)
    elif choice == 'r':
        del task_list
        task_list = []
        print("List Deleted:")    
    else:
        print("Invalid input, please try again.")