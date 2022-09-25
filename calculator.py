def add(a,b):
    return a+b;

def sub(a,b):
    return a-b;

def mul(a,b):
    return a*b;

def div(a,b):
    return a/b;

operator = {"+":add,"-":sub,"*":mul,"/":div}

print("---starting calculator---")
while True:
    number1 = float(input("enter number:"))
    continueWithPrevious = False
    while not continueWithPrevious:
        operation = input("Enter operation:")
        number2 = float(input("enter number:"))
        calculation = operator[operation]
        result = calculation(number1,number2)
        print(f"{number1} {operation} {number2} = {result}")
        continuation = input("Do you want to continue with prevoius result(yes or no):")
        if(continuation == "yes"):
            number1 = result
        else:
            continueWithPrevious = True
    continueCalculation = input("Do you want to continue calculation(yes or no):")
    if(continueCalculation == "yes"):
        continue
    else:
        print("---exiting calculator---")
        break
