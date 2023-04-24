# list
countries = ['United Kingdom', 'Ghana', 'Nigeria', 'Australia', 'China']
print(countries)
print(countries[2][0]) # select the third value of the list and catch its first letter (Nigeria - N)
print(countries[1:]) # this syntax brings the specific value and all the value after it in the list
print(countries[1:3]) # this syntax brings a range (1 2)  the (3) value is ignored

# type of a particular variable
print(type(countries))

# changing an a specific value of the list
countries[0] = 'Jamaica'

# catching the last value of a list, we use -1 bute note that for the first we use 0
print('Last element:', countries[-1])

# length
print(len(countries))

## Checking the types of the values in a list
# another way to create a list is using the list()
maria = list(('Maria', 18, True))
print(type(maria[0]))
print(type(maria[1]))
print(type(maria[2]))


