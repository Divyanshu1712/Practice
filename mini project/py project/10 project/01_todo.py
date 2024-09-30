"""to do list project
1. A person can do this == Add task, Delete task, update Task to complete r not 
2. LIST details are: Name , date , discription, priority
3. cateogry wise add things it ---  project- : study: , dailt basis- :

after this we can here 
Set reminders: The app can send notifications or reminders to alert users about upcoming deadlines.
Track progress: Users can view their progress towards completing tasks and goals.
Collaborate: Some apps allow users to share tasks and collaborate with others.

"""

todo = {}

def addtask():
    ''' add task '''
    
    print("Enter all data here below.")
    global taskName
    global taskDate
    global taskDisc
    taskName = input("Enter task: ")
    taskName.lower()
    
    taskDate = input("Enter the task date: ")
    taskDisc = input("Enter the Discription: ")
    
    todo[taskName] = {
        'Date:': taskDate,
        'Discription:': taskDisc
    }

    return "Task add successfully"

def delTask(taskName):
    ''' dek task'''
    print(todo)
    print("select and copy the task name to delete.")
    del_task = input("Enter or copy the task to delete ")
    if del_task.lower() in todo.lower():
        del todo[taskName]
    else:
        print("Task not Found! ")
    return 


def edittask(taskName):
    ''' edit task'''
    taskName = input("enter the task naeme to edit det. ")
    if taskName in todo:
        print("which type of details you have to chnage")
        # slection of what to chnage.
        print("1. only edit the date ")
        print("2. only edit the disc. ")
        print("3. change both..")

        newchoice = input("Enter the number you have to change: ")
        match newchoice:
            case '1':
                newDate = input("Enter new date")
                todo[taskName] ={
                    'Date:': newDate,
                    'Discription:': taskDisc
                }
            case '2':
                newDISC = input("Enter new Discp.: ")
                todo[taskName] = {
                    'Date:': taskDate,
                    'discp:': newDISC,
                }
            case '3':
                newDate = input("Enter new date")
                newDISC = input("Enter new Discp.: ")
                todo[taskName]={
                    'Date:': newDate,
                    'Discription:': newDISC,
                }
    else:
        print("Not found!!")
                
                

def viewTask():
    '''  view task'''
    # print(todo)
    view_taskName = input("enter the task name want to see: ")
    view_taskName.lower()

    if view_taskName in todo:
        print(todo[view_taskName])
    else:
        print("Not Found.")

# main fucntion
def main():
    while True:
        print("\nTO-DO LIST")
        # print("a")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. edit Task")
        print("4. view Task")
        print("5. EXIT")

        Choice = input(" Enter the select choice: ")

        match Choice:
            case '1':
                addtask()
            case '2':
                delTask(taskName)
            case '3':
                edittask(taskName)
            case '4':
                viewTask()
            case '5':
                exit()
            case _:
                print("Invalid")


if __name__ == "__main__":
    main()
