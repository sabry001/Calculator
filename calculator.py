while True:
    num=float(input("enter number: "))
    op=input("+ -/*&^%: ")
    num2=float(input("enter number2: "))
    if op=="+":
        print(num+num2)
    elif op=="-":
        print(num-num2)
    elif op=="*":
        print(num*num2)
    elif op=="/":
        if num2 == 0:
            print("zero")
        else:
           print(num/num2)
    else:
        print("invalid option")
    print("done")

    choice=input("press q to exit: ")
    if choice=="q":
        break
