print("\033[33m====== Create Your Account ======\033[m")

username = input("Enter username: ")
password = input("Enter password: ")


print("\033[32m====== Your account has been created successfully ======\033[m")
print("\033[30m Login now!! \033[m")

checkUsername = input("Enter username: ")
checkPassword = input("Enter Password: ")

if username == checkUsername and password == checkPassword:
    print("\033[32m Logged in successfully!! \033[m")
else:
    print("\033[31m Username or Password invalid \033[m")