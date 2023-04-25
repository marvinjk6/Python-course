########## Functions are a block of code which perform a particular task
# wu use the reserved word 'def' to declare a function
# indentation is very iportant in Python 



########### When we don't know the exactly quantity of arguments we use *before the arguments
# def greetings_function(*names):
#     print("Hello, " + names[2] + " nice to meet you")

# greetings_function("Marvin", "João", "Paulo")

################ 
# def greetings_function(name, age):
#     print("Hello " + name + ", you're", age, "old, nice to meet you")

# greetings_function(name = "Gabriel", age = 13)


######## Getting user's data

name = str(input("Hello, What's your name: "))
age = int(input("How old are you: "))

def greetings_function(n, a):
    print("Welcome {},\nYou're {} years old, nice to meet you!!" .format(n, a))


# invoking the function, passing two arguments
greetings_function(name, age)