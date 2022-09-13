num1 = float(input("Enter the firt number: "))
oper= input("Chose your operator: ")
num2 = float(input("Enter the second number: "))       

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "/":
    print(num1 / num2)
elif oper == "*":
    print(num1 * num2)
else:
    print("Invalid")
