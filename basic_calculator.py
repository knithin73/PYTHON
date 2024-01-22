import os
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
os.system('clear')
operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }
def calculator():
    num1=float(input("Enter the first number\n"))
    # operation=input("Enter the operation you would like to perform\n + \n - \n *\n / \n")
    should_continue=True
    while should_continue==True:
        num2=float(input("Enter the second number\n"))
        operators=""
        for operator in operations:
            print(operator)
        operator_symbol=input("Enter the operator\n")
        cal=operations[operator_symbol]
        calculated_value=cal(num1,num2)
        print(f"{num1} {operator_symbol} {num2} = {calculated_value}")
        continue1=input(f"Type y to continue calculating with {calculated_value} or type no restart\n")
        if continue1=="y":
            should_continue=True
            num1=calculated_value
        else:
            should_continue=False
            os.system('clear')
            calculator()

calculator()