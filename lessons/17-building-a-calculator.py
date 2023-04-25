### Building a Basic Calculator


print("================ Calculator ================")

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
operation = input("What's the operation (sum/sub/mult/div): ")

if operation == "sum":
    print("Sum: ", n1 + n2)
elif operation == "sub":
    print("Subtraction: ", n1 - n2)
elif operation == "mult":
    print("Multiplication: ", n1 * n2)
elif operation == "div":
    print("Subtraction: ", n1 / n2)
else: 
    print("You enter an invalid operation or data")