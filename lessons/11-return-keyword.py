## Return statement in Python function
# the return statement gives us an output or an feedback of what's been executed

#### input function receives the data as a String, we need to change the type of the data acording of what we want to do, in this case we want an Integer or Float data

# 

num1 = float(input("Digit first number: "))
num2 = float(input("Digit second number: "))


def sum(n1, n2):
    print("this code will be shown") 
    return n1 + n2
    print("this won't be shown, because the return statement ends the function")

print(sum(num1, num2))