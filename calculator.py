x=int(input("Enter the first number:"))
operator= input("enter the operator (+,-,*,/,%) : ")
y=int(input("Enter the Second numberx"))

if operator=="+":
    print(x + y)
elif operator=="-":
    print(x - y)
elif operator=="*":
    print(x * y)
elif operator=="/":
    print(x / y)
elif operator=="%":
    print(x % y)
else:
    print("Incorrect operator")