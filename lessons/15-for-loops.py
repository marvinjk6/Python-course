## For loops - for loops is used to interating over a sequence
## this sequence can be a List, a tuple, dictionary even a String and range of numbers

# for letter in "hello":
#     print(letter)


###### list
#fighters = ["Anderson Silva", "Khabib Nurmagomedov", "John Jones", "Minoutauro", "Cigano"]
# for fighter in fighters:
#     print(fighter)
#     if fighter == "John Jones":
#         break  ## we can brek the loop with a condition


###### range
for x in range(4):
    print(x)
print("--------------")

for x in range(3, 7):
    print(x)
print("--------------")

for x in range(7):
    print(x)
else:
    print("Else is executed when the for loop ends!!!")
