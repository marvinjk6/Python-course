''' 
Try Except - It is used to handle errors
Most of the times when we're working with Python a lot of errors can occurs, this errors stops our program

ValueError - the value of the data is wrong 
NameError - when something is not defined
'''

try:
    x = int(input("Input an integer: "))
    print(x)
except:
    print("Something went wrong... Please Try again!!")
else:
    print("Everything was OK!!") ## else is executed when there's no error
finally:
    print("Try - Except finished") ## It will be executed at the end, regardless of whether there was an error or not