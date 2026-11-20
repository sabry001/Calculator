def calculator(a,b):
    return a + b
def calcular(a,b):
    return a - b
def cal(a,b):
    return a * b
def calcu(a,b):
    if b == 0:
        return "zero"
    return a / b
    

while True:
    num=float(input("enter number: "))
    op=input("+ -/*&^%: ")
    num2=float(input("enter number2: "))
    if op=="+":
        print(calculator(num,num2))
    elif op=="-":
        print(calcular(num,num2))
    elif op=="*":
        print(cal(num,num2))
    elif op=="/":
        print(calcu(num,num2))
    else:
        print("invalid option")
    print("done")

    choice=input("press q to exit: ")
    if choice=="q":
        break
