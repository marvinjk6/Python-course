#### If statement is used to execute code with determined conditions

# age = int(input("How old are you? "))

# if age <= 10:
#     print("You're a child")
# elif age <= 17:
#     print("You're a teenager")
# else:
#     print("You're an adult")

######################## and keyword - both needs to be correct return true
# gender = "female"
# age = 18

# if gender == "male" and age >=18:
#     print('You\'re a male and an adult')
# elif gender == "female" and age >= 18:
#     print('You\'re a female and an adult') # a way to use ' inside of '' is using \ before
# else: 
#      print("You're not and adult")

########################### or keyword - only one condition needs to be true to return true

# if gender == "male" or age < 15:
#     print(True)
# else:
#     print(False)


sentence = input("What's the sentence? ")

if len(sentence) > 10:
    print("The sentence is greater than 10")
elif len(sentence) == 10:
    print("The sentence is equal to 10")
else:
    print("The sentence is minor than 10")

print("Sentence Lenght:", len(sentence))
