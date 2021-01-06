#menu based To Do App.
while True:
    print("MY APP")
    print("====")
    print("1. Add Task")
    print("2. View All Tasks")
    print("0. To Exit")
    option=int(input("Please Choose Option:"))

    if option==1:
        n1=input("Enter Task Name:")
        print("Task added")
    elif option==2:
        n1=input("Enter Task Name:")
        print("Task added")
    elif option==0:
        print("Bye")
        break
    else:
        print("Please choose correct option")
    x=input("Do you want to continue yes or no")
    if x!='yes':
        print("exit")
        break