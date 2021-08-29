def add (n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul (n1,n2):
    return n1*n2

def div (n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}


def calculator():
    """ a recursive function"""
    num1=float(input("Enter the first number: "))
    continuecal=True
    while continuecal:
        num2=float(input("Enter the second number: "))
        for operend in operations:
            print(operend)
        op=input("Enter the operation you want to perform: ")

        func=operations[op]
        answer=func(num1,num2)

        print(f"{num1} {op} {num2} = {answer}")

        continuecal=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")
        if continuecal=="y":
            num1=answer
            continuecal=True
        else: 
            continuecal=False
            calculator()
        
calculator()