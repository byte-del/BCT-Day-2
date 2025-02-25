def add(num1, num2):
    add=num1+num2
def sub(num1,num2):
    sub=num1-num2
def mul(num1,num2):
    mul=num1*num2
def div(num1,num2):
    div=num1/num1
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
elif choice == "3":
    print("Result:", num1 * num2)
elif choice == "4":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid input")
