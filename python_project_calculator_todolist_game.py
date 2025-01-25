# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     if b==0:
#         return "error:cannot divide by 0"
#     return a/b
# while True:
#     print("Enter number between 1 to 4")
#     print("Enter 1 for addition")
#     print("Enter 2 for subtraction")
#     print("Enter 3 for multiplication")
#     print("Enter 4 for division")
#     print("Enter 5 for quiting")

#     choise=int(input("Enter number of your choise"))


#     if choise==1:
#         num_1=int(input("enter first number"))
#         num_2=int(input("enter second number"))
#         result=add(num_1,num_2)
#         print("Result= " ,result)
#     elif choise==2:
#         num_1=int(input("enter first number"))
#         num_2=int(input("enter second number"))
#         result=sub(num_1,num_2)
#         print("Result= " ,result)
#     elif choise==3:
#         num_1=int(input("enter first number"))
#         num_2=int(input("enter second number"))
#         result=mul(num_1,num_2)
#         print("Result= " ,result)
#     elif choise==4:
#         num_1=int(input("enter first number"))
#         num_2=int(input("enter second number"))
#         result=div(num_1,num_2)
#         print(result)
#     elif choise==5:
#         break
        
#     else:
#         print("invalid choise")



# To-Do List App

# tasks=[]
# def add_task(task):
#     if task in tasks:
#         print("task already exists")
#     else:
#         tasks.append(task)
        

# def remove_task(task):
#     if task in tasks:
#         tasks.remove(task)
#         print("task removed successfully")
#     else:
#         print("task does not exists")
# def task_completed(task):
#     if task in tasks:
#         tasks[tasks.index(task)] += "(completed)"
#         print("task marked as completed successfully")
#     else:
#         print("task does not exists")

# while True:
#     print("enter your choise")
#     print("enter 1 to add task")
#     print("enter 2 to remove task")
#     print("enter 3 to mark the task completed")
#     print("enter 4 to quit")
#     choise=int(input("Enter your choise"))

#     if choise==1:
#         task=input("enter task to add to list")
#         add_task(task)
#     elif choise==2:
#         task=input("enter task to be removed")
#         remove_task(task)
#     elif choise==3:
#         task=input("enter the task you want to mark as completed")
#         task_completed(task)
#     elif choise==4:
#         break
#     else:
#         print("Invalid choise")




import random
def play_game():
    choises=["rock","paper","scissors"]
    user_choise=input("enter your choise")
    comp_choise=random.choice(choises)
    if user_choise not in choises:
        print("invalid choise")
        return
    print("computer's choise" , comp_choise)
    if user_choise==comp_choise:
        print("its a tie")
    elif (user_choise == "rock" and comp_choise == "scissors") or \
            (user_choise == "paper" and comp_choise == "rock") or \
            (user_choise == "scissors" and comp_choise == "paper"):
        print("You win!")
    else:
        print("computer wins")

play_game()

    
