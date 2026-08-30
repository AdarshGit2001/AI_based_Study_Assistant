num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
operator = input("Enter Operator: ")

if(operator == '+'):
    print(f"Result = ", num1+num2)

elif(operator == '-'):
    print(f"Result = ", num1-num2)

elif(operator == '*'):
    print(f"Result = ", num1*num2)

elif (operator == '/'):
    if(num2==0):
        print("Cannot divided by Zero.")
    else:
        print(f"Result = ", num1/num2)

else:
    print("Invalid Operator.")