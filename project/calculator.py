def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "error:cannot divide by 0"
    return a/b
while True:
    print("Enter number between 1 to 4")
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 for quiting")

    choise=int(input("Enter number of your choise"))


    if choise==1:
        num_1=int(input("enter first number"))
        num_2=int(input("enter second number"))
        result=add(num_1,num_2)
        print("Result= " ,result)
    elif choise==2:
        num_1=int(input("enter first number"))
        num_2=int(input("enter second number"))
        result=sub(num_1,num_2)
        print("Result= " ,result)
    elif choise==3:
        num_1=int(input("enter first number"))
        num_2=int(input("enter second number"))
        result=mul(num_1,num_2)
        print("Result= " ,result)
    elif choise==4:
        num_1=int(input("enter first number"))
        num_2=int(input("enter second number"))
        result=div(num_1,num_2)
        print(result)
    elif choise==5:
        break
        
    else:
        print("invalid choise")